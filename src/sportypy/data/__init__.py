"""
Data acquisition and preprocessing utilities.

This module provides:
- Data connectors for sports APIs
- Preprocessing utilities (standardization, normalization)
- Domain-specific feature creation
- Narwhals-based dataframe utilities (Polars preferred, Pandas supported)
"""

from sportypy.data.frames import (
    concat_frames,
    create_empty_frame,
    nw,
    to_native,
    wrap_frame,
)

__all__ = [
    "nw",
    "wrap_frame",
    "to_native",
    "create_empty_frame",
    "concat_frames",
]
