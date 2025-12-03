"""
SportyPy: A Python library for sports analytics with probabilistic modeling.

SportyPy provides tools for:
- Latent skill modeling and aging curves (projections)
- Selection bias adjustments and level adjustments (causal)
- Spatial and trajectory models (spatial)
- Value attribution and context modeling (value_attribution)
- High-level prediction wrappers (predict)
- Data acquisition and preprocessing (data)
"""

__version__ = "0.1.0"

from sportypy import causal, data, predict, projections, spatial, value_attribution

__all__ = [
    "__version__",
    "projections",
    "causal",
    "spatial",
    "value_attribution",
    "predict",
    "data",
]
