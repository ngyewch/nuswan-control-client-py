import time
import uuid
from typing import Dict, List

from .schema import GeofenceUpdateReqSchema, MissionMsgSchema, MissionCommandsSchema


class Request:

    def __init__(self, msg_type: str, vehicle_id: str, *, msg_id: str = str(uuid.uuid4())):
        self.vehicle_id = vehicle_id
        self.msg_id = msg_id
        self.msg_type = msg_type


class Point2D:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Point3D:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class MissionPoint:

    def __init__(self, *, m_point_id: int, loc: Point3D, m_point_type: str, m_point_params: Dict[str, float],
                 m_point_payloads: Dict[str, int], m_point_props: Dict[str, float]):
        self.m_point_id = m_point_id
        self.loc_x = loc.x
        self.loc_y = loc.y
        self.loc_z = loc.z
        self.m_point_type = m_point_type
        self.m_point_params = m_point_params
        self.m_point_payloads = m_point_payloads
        self.m_point_props = m_point_props


class Mission:

    def __init__(self, *, mission_id: int, m_timeout: int, m_points: List[MissionPoint]):
        self.mission_id = mission_id
        self.m_timeout = m_timeout
        self.m_points = m_points


class GeofenceUpdateReq(Request):
    __schema__ = GeofenceUpdateReqSchema()

    def __init__(self, vehicle_id: str, *, msg_id: str = str(uuid.uuid4()), geofence_coordinates: List[Point2D]):
        Request.__init__(self, 'GeofenceUpdateReq', vehicle_id, msg_id=msg_id)
        self.geofence_coordinates = geofence_coordinates


class MissionMsg(Request):
    __schema__ = MissionMsgSchema()

    def __init__(self, vehicle_id: str, *, msg_id: str = str(uuid.uuid4()), geofence_coordinates: List[Point2D],
                 missions: List[Mission]):
        Request.__init__(self, 'MissionMsg', vehicle_id, msg_id=msg_id)
        self.geofence_coordinates = geofence_coordinates
        self.missions = missions


class MissionCommands(Request):
    __schema__ = MissionCommandsSchema()

    def __init__(self, vehicle_id: str, *, msg_id: str = str(uuid.uuid4()),
                 timestamp: int = int(round(time.time() * 1000)), mission_id: int, mission_command: str):
        Request.__init__(self, 'MissionCommands', vehicle_id, msg_id=msg_id)
        self.timestamp = timestamp
        self.mission_id = mission_id
        self.mission_command = mission_command
