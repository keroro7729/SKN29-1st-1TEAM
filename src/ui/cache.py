"""Streamlit 캐시 유틸.

- 기본 TTL: 30분
- UI 레이어에서만 사용 (서비스 레이어는 Streamlit에 의존하지 않도록 유지)
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar, overload

import streamlit as st

DEFAULT_TTL_SECONDS = 60 * 30

F = TypeVar("F", bound=Callable[..., Any])


@overload
def cache_data(func: F) -> F: ...


@overload
def cache_data(*, ttl: int = DEFAULT_TTL_SECONDS, **kwargs: Any) -> Callable[[F], F]: ...


def cache_data(func: F | None = None, *, ttl: int = DEFAULT_TTL_SECONDS, **kwargs: Any):
    """`st.cache_data` 기본 TTL(30분) 래퍼."""

    def _decorator(f: F) -> F:
        return st.cache_data(ttl=ttl, **kwargs)(f)

    if func is None:
        return _decorator
    return _decorator(func)

