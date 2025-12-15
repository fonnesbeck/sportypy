"""
Dataframe utilities using Polars.

This module provides utilities for working with Polars DataFrames,
including Narwhals wrappers for interoperability with other libraries.

Example usage:
    import polars as pl
    from sportypy.data.frames import wrap_frame, to_native

    # Create a Polars dataframe
    df = pl.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

    # Wrap it for Narwhals operations (useful for library interop)
    nw_df = wrap_frame(df)

    # Perform operations using Narwhals API
    result = nw_df.select("x", "y").filter(nw.col("x") > 1)

    # Convert back to Polars
    native_df = to_native(result)
"""

from __future__ import annotations

from typing import Any, Literal

import narwhals as nw
import polars as pl

ConcatMethod = Literal[
    "vertical",
    "vertical_relaxed",
    "horizontal",
    "diagonal",
    "diagonal_relaxed",
    "align",
]


def wrap_frame(df: pl.DataFrame | pl.LazyFrame) -> nw.DataFrame[Any]:
    """
    Wrap a Polars dataframe in a Narwhals DataFrame.

    This is useful for interoperability with libraries that use Narwhals.

    Parameters
    ----------
    df : pl.DataFrame | pl.LazyFrame
        A Polars DataFrame or LazyFrame.

    Returns
    -------
    nw.DataFrame
        A Narwhals DataFrame wrapping the input.
    """
    return nw.from_native(df)


def to_native(df: nw.DataFrame[Any]) -> pl.DataFrame:
    """
    Convert a Narwhals DataFrame back to Polars.

    Parameters
    ----------
    df : nw.DataFrame
        A Narwhals DataFrame.

    Returns
    -------
    pl.DataFrame
        The native Polars DataFrame.
    """
    return df.to_native()  # type: ignore[return-value]


def create_empty_frame(schema: dict[str, type]) -> pl.DataFrame:
    """
    Create an empty Polars dataframe with a given schema.

    Parameters
    ----------
    schema : dict[str, type]
        Column names mapped to Python types (int, float, str, bool).

    Returns
    -------
    pl.DataFrame
        An empty Polars DataFrame with the specified schema.

    Example
    -------
    >>> df = create_empty_frame({"id": int, "name": str, "score": float})
    >>> df.schema
    {'id': Int64, 'name': Utf8, 'score': Float64}
    """
    type_map = {int: pl.Int64, float: pl.Float64, str: pl.Utf8, bool: pl.Boolean}
    pl_schema = {col: type_map.get(dtype, pl.Utf8) for col, dtype in schema.items()}
    return pl.DataFrame(schema=pl_schema)


def concat_frames(
    frames: list[pl.DataFrame], *, how: ConcatMethod = "vertical"
) -> pl.DataFrame:
    """
    Concatenate multiple Polars DataFrames.

    Parameters
    ----------
    frames : list[pl.DataFrame]
        List of Polars DataFrames to concatenate.
    how : ConcatMethod, default "vertical"
        Concatenation method: "vertical", "vertical_relaxed", "horizontal",
        "diagonal", "diagonal_relaxed", or "align".

    Returns
    -------
    pl.DataFrame
        Concatenated DataFrame.
    """
    return pl.concat(frames, how=how)


__all__ = [
    "nw",
    "pl",
    "wrap_frame",
    "to_native",
    "create_empty_frame",
    "concat_frames",
]
