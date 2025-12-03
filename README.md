# SportyPy: Probabilistic Modeling for Sports Analytics

SportyPy is a Python library for sports analytics, built on **PyMC** for Bayesian inference and probabilistic modeling. It provides a modular, high-level interface for hierarchical models, causal inference, and latent variable projections—techniques frequently used in professional sports analytics.

---

## SportyPy Implementation Plan

### I. Foundational Architecture

The library leverages Python's data science ecosystem with PyMC as the core modeling engine.

| Component | Description | Supporting Source Concepts |
| :--- | :--- | :--- |
| **Language & Core Stack** | Python, relying on **NumPy** for numerical efficiency and **pandas** for flexible data manipulation (DataFrames). | Standard data science toolkit. |
| **Statistical Backend** | **PyMC** serves as the probabilistic programming foundation, providing MCMC sampling, variational inference, and GPU acceleration via PyTensor. This enables hierarchical Bayesian models for latent skills, uncertainty quantification, and robust inference with heavy-tailed distributions. | ADVI optimization for projections, Bayesian Hierarchical Logistic Regression for Catcher Framing/Pickoff value, Multivariate t distribution for robustness against outliers. |
| **Modularity & Extensibility** | The library is modular, with distinct sub-modules for different analytical concerns (e.g., `sportypy.projections`, `sportypy.spatial`). It offers **high-level wrappers** built on PyMC model classes for defining complex hierarchical models. | SportyPy abstracts PyMC model construction into domain-specific APIs. |

### II. Core Modeling Modules

SportyPy features dedicated modules for high-level components: Aging Curves/Projections, Selection Bias Adjustments, and Spatial Models.

#### 1. `sportypy.projections` (Latent Skills and Aging Curves)

This module enables long-term performance forecasting using PyMC's hierarchical modeling capabilities.

*   **Latent Skill Modeling:** Implements "true skill" as a **latent quantity** (analogous to scout tool grades like "power" or "contact") using PyMC's latent variable framework.
    *   *Feature Set:* Define inputs $Y_{rhijk}$ (observed metrics) and model latent skills $\gamma_{rhij}$ based on performance indicators.
    *   *Emission Matrix:* Incorporates a design matrix **B** mapping latent skills to observable performance metrics, distinguishing between identified and associated skills for interpretability.

*   **Aging Curves (`.aging`):** Tools for applying and estimating age-related drift in latent skills ($\alpha_j$) using PyMC's Gaussian Process and spline components.
    *   Aging curves are parameterized as polynomial or spline functions of age to capture expected improvement or decline over time.
    *   The model supports computing projections over arbitrary lengths for simulation of **full career trajectories**.

*   **Probabilistic Output:** All projections return posterior distributions via PyMC's `InferenceData` objects, providing both point estimates and **full uncertainty quantification** for risk assessment in predictions about total future value.

#### 2. `sportypy.causal` (Selection Bias and Level Adjustments)

This module implements causal inference techniques using PyMC for Bayesian propensity modeling.

*   **Level Adjustment (`.level_adjust`):** Implements the causal inference framework to derive **level-independent measures of performance**.
    *   The framework models the **promotion propensity score** ($p_{it}$) using PyMC's flexible regression capabilities, capturing residual talent information not explained by performance at the origin level.
    *   Applies Bayesian causal estimators (inverse probability weighting with posterior uncertainty) to mitigate **selection bias** when comparing performance across different levels of play (e.g., Minor League Baseball to MLB).

*   **Value Neutrality:** Tools to create metrics agnostic to **park, team, and environmental effects** using hierarchical partial pooling in PyMC.

#### 3. `sportypy.spatial` (Spatial and Trajectory Models)

This module provides methods for predicting outcomes based on spatial coordinates or trajectories using PyMC's Gaussian Process framework.

*   **Pitch/Ball Trajectory Models:** Wrappers for modeling pitch outcomes given pitch characteristics and trajectories.
    *   Utilizes PyMC's GLM and GP modules with spatial effects learned as functions of trajectory parameters.
    *   Supports the Hierarchical Gaussian Process (HGP) framework with HSGP (Hilbert Space GP) approximations for computational efficiency.

*   **Defensive/Fielding Range:** Components to evaluate player performance on balls in play based on expected results given batted ball characteristics.
    *   Supports **Statcast Out Models** (Catch-Out/Force-Out) that predict the log-odds of an out using PyMC HGPs, accounting for fielder-specific spatial and linear effects.

### III. Utility and Infrastructure Modules

#### 4. `sportypy.value_attribution` (Value Metrics and Context)

This module handles quantification of value changes during a game using PyMC for hierarchical attribution.

*   **Markov Chain Modeling:** Tools for modeling Base-Out State (BOS) transitions to calculate **expected runs scored** from a given state. This forms the foundational expected run value $V(i)$ for many pitch outcomes.
*   **Hierarchical Attribution:** PyMC-based framework for attributing value to individual players (batter, pitcher, catcher) by comparing actual results to predictions from a league-average player, using **Hierarchical Mixed Effects Models**. This applies to:
    *   Play Value (change in BOS run state).
    *   Pitch Value (change in Base-Out-Count-Run state).
    *   Pickoff Value and Stolen Base Value, accounting for pitcher, catcher, and runner contributions.

*   **Availability/Temporal Models:** Functionality for modeling time-dependent latent states, such as player availability (fitness/injury risk), using PyMC's **Hidden Markov Model** implementations to capture state persistence and predict long-term injury expectations based on observed play states (Start, Play, Rest, IL).

#### 5. `sportypy.predict` (Model Wrappers)

This module offers high-level PyMC-based wrappers for Bayesian prediction in sports analytics.

*   **Regression and Classification:** Wrappers for Bayesian versions of common sports prediction models using PyMC's `bambi` integration:
    *   **Logistic Regression** for binary outcomes (win/loss, shot make/miss)
    *   **Poisson/Negative Binomial Regression** for count data (goals, corner kicks)
    *   **Ordinal Regression** for ranked outcomes
*   **Ensemble Methods:** APIs for Bayesian Model Averaging and stacking using PyMC's model comparison tools (`arviz.compare`, `arviz.loo`).
*   **Head-to-Head Matchups:** Tools to structure inputs for predicting team matchups, incorporating team performance aggregates (shooting, turnovers, rebounding) and Elo ratings with full posterior uncertainty.

#### 6. `sportypy.data` (Data Acquisition and Preprocessing)

This module handles integration with external sports data sources.

*   **Data Connectors:** Utilities for connecting to common public APIs and specialized libraries (e.g., `nba_api`, `nflfastR`, `sportsreference`, `py_football`) to collect and parse statistics.
*   **Preprocessing Utilities:** Functions for standard tasks like feature standardization and normalization, as well as domain-specific feature creation (e.g., True Shooting Percentage, Rushing Yards Over Expected, Completion Percentage Over Expected).
*   **PyMC Integration:** Data preparation utilities that output PyMC-ready coordinate dictionaries and data containers for hierarchical indexing.
