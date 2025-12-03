"""
Dataframe utilities using Narwhals for backend-agnostic operations.

This module provides a unified interface for dataframe operations that works
with both Polars (preferred) and Pandas backends via Narwhals.

Example usage:
    import polars as pl
    from sportypy.data.frames import wrap_frame, to_native

    # Create a Polars dataframe
    df = pl.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

    # Wrap it for Narwhals operations
    nw_df = wrap_frame(df)

    # Perform operations using Narwhals API
    result = nw_df.select("x", "y").filter(nw.col("x") > 1)

    # Convert back to native format
    native_df = to_native(result)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

import narwhals as nw
from narwhals.typing import IntoFrame

if TYPE_CHECKING:
    import pandas as pd
    import polars as pl

T = TypeVar("T", bound=IntoFrame)


def wrap_frame(df: IntoFrame) -> nw.DataFrame[IntoFrame]:
    """
    Wrap a native dataframe (Polars or Pandas) in a Narwhals DataFrame.

    Parameters
    ----------
    df : IntoFrame
        A Polars DataFrame, Pandas DataFrame, or other Narwhals-compatible frame.

    Returns
    -------
    nw.DataFrame
        A Narwhals DataFrame wrapping the input.
    """
    return nw.from_native(df)


def to_native(df: nw.DataFrame[T]) -> T:
    """
    Convert a Narwhals DataFrame back to its native format.

    Parameters
    ----------
    df : nw.DataFrame
        A Narwhals DataFrame.

    Returns
    -------
    IntoFrame
        The native dataframe (Polars or Pandas).
    """
    return df.to_native()


def create_empty_frame(
    schema: dict[str, type], *, backend: str = "polars"
) -> nw.DataFrame[IntoFrame]:
    """
    Create an empty dataframe with a given schema.

    Parameters
    ----------
    schema : dict[str, type]
        Column names mapped to Python types (int, float, str, bool).
    backend : str, default "polars"
        Backend to use: "polars" (default) or "pandas".

    Returns
    -------
    nw.DataFrame
        An empty Narwhals DataFrame with the specified schema.

    Raises
    ------
    ValueError
        If an unsupported backend is specified.
    """
    if backend == "polars":
        import polars as pl

        type_map = {int: pl.Int64, float: pl.Float64, str: pl.Utf8, bool: pl.Boolean}
        pl_schema = {col: type_map.get(dtype, pl.Utf8) for col, dtype in schema.items()}
        native_df = pl.DataFrame(schema=pl_schema)
    elif backend == "pandas":
        import pandas as pd

        type_map = {int: "int64", float: "float64", str: "object", bool: "bool"}
        pd_schema = {col: type_map.get(dtype, "object") for col, dtype in schema.items()}
        native_df = pd.DataFrame(columns=list(schema.keys())).astype(pd_schema)
    else:
        raise ValueError(f"Unsupported backend: {backend}. Use 'polars' or 'pandas'.")

    return nw.from_native(native_df)


def concat_frames(
    frames: list[nw.DataFrame[T]], *, how: str = "vertical"
) -> nw.DataFrame[T]:
    """
    Concatenate multiple Narwhals DataFrames.

    Parameters
    ----------
    frames : list[nw.DataFrame]
        List of Narwhals DataFrames to concatenate.
    how : str, default "vertical"
        Concatenation method: "vertical" (row-wise) or "horizontal" (column-wise).

    Returns
    -------
    nw.DataFrame
        Concatenated DataFrame.
    """
    return nw.concat(frames, how=how)


__all__ = [
    "nw",
    "wrap_frame",
    "to_native",
    "create_empty_frame",
    "concat_frames",
]
