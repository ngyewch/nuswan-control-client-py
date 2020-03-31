from marshmallow import Schema, fields


class Point2DSchema(Schema):
    x = fields.Float()
    y = fields.Float()


class GeofenceUpdateReqSchema(Schema):
    # msg_type = fields.Str(data_key='msgType')
    vehicle_id = fields.Str(data_key='vehicleId')
    msg_id = fields.Str(data_key='msgId')
    geofence_coordinates = fields.List(fields.Nested(Point2DSchema()), data_key='geoFenceCoordinates')


class MissionPointSchema(Schema):
    m_point_id = fields.Int(data_key='mPointId')
    loc_x = fields.Float(data_key='locX')
    loc_y = fields.Float(data_key='locY')
    loc_z = fields.Float(data_key='locZ')
    m_point_type = fields.Str(data_key='mPointType')
    m_point_params = fields.Dict(fields.Str(), fields.Float(), data_key='mPointParams')
    m_point_payloads = fields.Dict(fields.Str(), fields.Int(), data_key='mPointPayloads')
    m_point_props = fields.Dict(fields.Str(), fields.Float(), data_key='mPointProps')


class MissionSchema(Schema):
    mission_id = fields.Int(data_key='missionId')
    m_timeout = fields.Int(data_key='mTimeout')
    m_points = fields.List(fields.Nested(MissionPointSchema()), data_key='mPoints')


class MissionMsgSchema(Schema):
    # msg_type = fields.Str(data_key='msgType')
    vehicle_id = fields.Str(data_key='vehicleId')
    msg_id = fields.Str(data_key='msgId')
    geofence_coordinates = fields.List(fields.Nested(Point2DSchema()), data_key='geoFenceCoordinates')
    missions = fields.List(fields.Nested(MissionSchema()))


class MissionCommandsSchema(Schema):
    # msg_type = fields.Str(data_key='msgType')
    vehicle_id = fields.Str(data_key='vehicleId')
    msg_id = fields.Str(data_key='msgId')
    timestamp = fields.Int()
    mission_id = fields.Int(data_key='missionId')
    mission_command = fields.Str(data_key='missionCommand')
