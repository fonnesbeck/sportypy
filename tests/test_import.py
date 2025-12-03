"""Basic import tests for SportyPy."""

import pytest


def test_import_sportypy():
    """Test that sportypy can be imported."""
    import sportypy

    assert sportypy.__version__ == "0.1.0"


def test_import_submodules():
    """Test that all submodules can be imported."""
    from sportypy import causal, data, predict, projections, spatial, value_attribution

    assert projections is not None
    assert causal is not None
    assert spatial is not None
    assert value_attribution is not None
    assert predict is not None
    assert data is not None
