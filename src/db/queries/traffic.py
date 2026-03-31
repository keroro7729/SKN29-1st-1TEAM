from __future__ import annotations

from datetime import datetime


def list_road_names() -> str:
    return """
        SELECT road_name
        FROM pp_road
        ORDER BY road_name
    """


def dow_hour_pattern() -> str:
    return """
        SELECT
            DAYOFWEEK(t.datetime) AS dow,
            HOUR(t.datetime) AS hour,
            AVG(t.volume) AS avg_volume,
            AVG(s.speed) AS avg_speed_kmh,
            COUNT(*) AS samples
        FROM PP_traffic t
        JOIN pp_road r
          ON r.road_id = t.road_id
        LEFT JOIN pp_speed s
          ON s.road_id = t.road_id
         AND s.direction = t.direction
         AND s.datetime = t.datetime
        WHERE t.datetime >= %s
          AND t.datetime < %s
          AND (%s = '전체' OR r.road_name = %s)
        GROUP BY dow, hour
        ORDER BY dow, hour
    """


def dow_hour_pattern_params(*, start_dt: datetime, end_exclusive: datetime, road_name: str) -> tuple:
    return (start_dt, end_exclusive, road_name, road_name)

