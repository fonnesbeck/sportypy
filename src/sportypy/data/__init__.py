"""
Data acquisition and preprocessing utilities.

This module provides:
- Data connectors for sports APIs
- Preprocessing utilities (standardization, normalization)
- Domain-specific feature creation
- Polars-based dataframe utilities
"""

from sportypy.data.frames import (
    concat_frames,
    create_empty_frame,
    nw,
    pl,
    to_native,
    wrap_frame,
)

__all__ = [
    "nw",
    "pl",
    "wrap_frame",
    "to_native",
    "create_empty_frame",
    "concat_frames",
]
