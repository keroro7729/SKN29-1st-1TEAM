from __future__ import annotations

from datetime import datetime


def base_volume_speed_join() -> str:
    return """
        SELECT
            r.road_name AS road_name,
            t.datetime AS dt,
            t.volume AS volume,
            s.speed AS speed
        FROM PP_traffic t
        JOIN pp_road r
          ON r.road_id = t.road_id
        JOIN pp_speed s
          ON s.road_id = t.road_id
         AND s.direction = t.direction
         AND s.datetime = t.datetime
        WHERE t.datetime >= %s
          AND t.datetime < %s
          AND t.volume IS NOT NULL
          AND s.speed IS NOT NULL
          AND (%s = '전체' OR r.road_name = %s)
    """


def base_volume_speed_join_params(
    *, start_dt: datetime, end_exclusive: datetime, road_name: str
) -> tuple:
    return (start_dt, end_exclusive, road_name, road_name)

