#!/usr/bin/env python3

from nuswan_control.client import Client
from nuswan_control.model import Point2D, GeofenceUpdateReq, MissionMsg, MissionPoint, Mission, Point3D, MissionCommands


def test(client: Client):
    geofence_coordinates = [
        Point2D(0, 0),
        Point2D(10, 0),
        Point2D(10, 10),
        Point2D(0, 10)
    ]

    req1 = GeofenceUpdateReq("swan2", geofence_coordinates=geofence_coordinates)
    client.send(req1)

    req2 = MissionMsg("swan2", geofence_coordinates=geofence_coordinates,
                      missions=[Mission(mission_id=1, m_timeout=3600, m_points=[
                          MissionPoint(m_point_id=1, loc=Point3D(3, 3, 0),
                                       m_point_type="org.arl.jc2.mtt.SimpleMT",
                                       m_point_params={
                                           "CruisingSpeed": 2_0
                                       },
                                       m_point_payloads={
                                           "SIDESCAN": 5
                                       },
                                       m_point_props={
                                           "endHeading": -1.0
                                       }),
                          MissionPoint(m_point_id=2, loc=Point3D(6, 6, 0),
                                       m_point_type="org.arl.jc2.mtt.LawnMowerMT",
                                       m_point_params={
                                           "CruisingThrust": 1.0
                                       },
                                       m_point_payloads={
                                           "DTLA": 2
                                       },
                                       m_point_props={
                                           "xLength": 50.0,
                                           "yLength": 50.0,
                                           "moweWidth": 50.0,
                                           "moweBearing": 0.0
                                       })
                      ])])
    client.send(req2)

    req3 = MissionCommands("swan2", mission_id=1, mission_command="RUN")
    client.send(req3)


def main():
    client = Client()

    try:
        test(client)
    finally:
        client.close()


if __name__ == "__main__":
    main()
