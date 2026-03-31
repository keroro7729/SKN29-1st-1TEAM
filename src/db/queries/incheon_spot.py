from __future__ import annotations


def summary_kpis(*, table: str) -> str:
    # table은 내부에서만 사용(화이트리스트)하도록 서비스에서 고정된 값만 넘깁니다.
    return f"""
        SELECT
            COUNT(*) AS n_rows,
            COALESCE(SUM(a.occrrnc_cnt), 0) AS sum_occ,
            COALESCE(SUM(a.caslt_cnt), 0) AS sum_caslt,
            COALESCE(SUM(a.dth_dnv_cnt), 0) AS sum_dth,
            COALESCE(SUM(a.se_dnv_cnt), 0) AS sum_se,
            COALESCE(SUM(a.sl_dnv_cnt), 0) AS sum_sl
        FROM {table} a
    """


def by_district(*, table: str) -> str:
    return f"""
        SELECT
            COALESCE(NULLIF(TRIM(a.sido_sgg_nm), ''), '(미상)') AS district,
            SUM(a.occrrnc_cnt) AS occrrnc_cnt,
            SUM(a.caslt_cnt) AS caslt_cnt,
            SUM(a.dth_dnv_cnt) AS dth_dnv_cnt
        FROM {table} a
        GROUP BY district
        ORDER BY occrrnc_cnt DESC
        LIMIT 30
    """


def top_spots(*, table: str) -> str:
    return f"""
        SELECT
            a.spot_nm AS spot_nm,
            SUM(a.occrrnc_cnt) AS occrrnc_cnt,
            SUM(a.caslt_cnt) AS caslt_cnt,
            SUM(a.dth_dnv_cnt) AS dth_dnv_cnt
        FROM {table} a
        GROUP BY a.spot_nm
        ORDER BY occrrnc_cnt DESC
        LIMIT %s
    """

