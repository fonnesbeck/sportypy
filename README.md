# SportyPy: Probabilistic Modeling for Sports Analytics

This plan outlines the structure and key components for implementing the Python library, **SportyPy**, designed to support sports analytics models, mirroring the modular, probabilistic, and high-level structure of analogous libraries like CausalPy and PyMC-Marketing.

SportyPy will be designed around several core analytical pillars frequently used in professional sports analytics, particularly those utilizing complex modeling techniques like hierarchical models, causal inference, and latent variable projections.

---

## SportyPy Implementation Plan

### I. Foundational Architecture and Dependencies

The library will leverage Python's strong data science ecosystem, utilizing core libraries for performance and data management.

| Component | Description | Supporting Source Concepts |
| :--- | :--- | :--- |
| **Language & Core Stack** | Python, relying on **NumPy** for numerical efficiency and **pandas** for flexible data manipulation (DataFrames). | Standard data science toolkit. |
| **Statistical Backend** | Given the goal of modeling complex, often hierarchical systems, the backend should support **Bayesian inference and probabilistic programming** (PPL) or advanced generalized linear models. This is key for modeling latent skills and uncertainty. | Stan/ADVI optimization for projections, Bayesian Hierarchical Logistic Regression for Catcher Framing/Pickoff value, Multivariate t distribution for robustness against outliers. |
| **Modularity & Extensibility** | The library will be modular, with distinct sub-modules for different analytical concerns (e.g., `sportypy.projections`, `sportypy.spatial`). It should offer **high-level wrappers** for defining complex models (like hierarchical regressions or deep learning architectures). | Multiple model types are used in sources, including Logistic Regression, Random Forest, SVM, DNNs, CNNs, LSTMs, and AutoGluon. SportyPy should abstract these techniques. |

### II. Core Modeling Modules

SportyPy will feature dedicated modules for the high-level components requested: Aging Curves/Projections, Selection Bias Adjustments, and Spatial Models.

#### 1. `sportypy.projections` (Latent Skills and Aging Curves)

This module will enable long-term performance forecasting, which is critical for simulation and player valuation.

*   **Latent Skill Modeling:** Implement a structure for framing "true skill" as a **latent quantity** (analogous to scout tool grades like "power" or "contact"). This mirrors the methodology used in Batting and Pitching projections.
    *   *Feature Set:* Define inputs $Y_{rhijk}$ (observed metrics) and model latent skills $\gamma_{rhij}$ based on performance indicators.
    *   *Emission Matrix:* Incorporate the concept of a design matrix **B** which maps latent skills to observable performance metrics, distinguishing between identified and associated skills for interpretability.

*   **Aging Curves (`.aging`):** Provide tools for applying and estimating the age-related drift in latent skills ($\alpha_j$).
    *   Aging curves are parameterized as polynomial functions of age to capture expected improvement or decline over time.
    *   The model should support computing projections over arbitrary lengths for simulation of **full career trajectories**.

*   **Probabilistic Output:** Ensure projections return both a mean and **variance** for the rate of Runs Above Average (RAA), allowing analysts to measure **risk in predictions** about total future value.

#### 2. `sportypy.causal` (Selection Bias and Level Adjustments)

This module implements techniques to adjust performance metrics for contextual factors and quality of competition.

*   **Level Adjustment (`.level_adjust`):** Implement the causal inference framework to derive **level-independent measures of performance**.
    *   The framework relies on modeling the **promotion propensity score** ($p_{it}$) using non-parametric models like **Gradient Boosting Models (GBMs)**, which helps capture residual talent information not explained by performance at the origin level.
    *   The module will apply causal-based estimators (like the inverse probability of promotion/censoring weights) to mitigate **selection bias** inherent when comparing performance across different levels of play (e.g., Minor League Baseball to MLB).

*   **Value Neutrality:** Tools to create metrics that are agnostic to factors such as **park, team, and environmental effects**.

#### 3. `sportypy.spatial` (Spatial and Trajectory Models)

This module will provide methods for predicting outcomes based on spatial coordinates or trajectories, crucial for detailed performance analysis in many sports.

*   **Pitch/Ball Trajectory Models:** Implement wrappers for modeling pitch outcomes given pitch characteristics and trajectories.
    *   Utilize generalized linear models (GLMs) with spatial effects learned as functions of trajectory parameters.
    *   The models should support computationally efficient methods like the Hierarchical Gaussian Process (HGP) framework, which uses a linear basis approximation for scalability.

*   **Defensive/Fielding Range:** Components to evaluate player performance on balls in play based on expected results given batted ball characteristics.
    *   Support **Statcast Out Models** (Catch-Out/Force-Out) that predict the log-odds of an out using HGPs, accounting for fielder-specific spatial and linear effects.

### III. Utility and Infrastructure Modules

#### 4. `sportypy.value_attribution` (Value Metrics and Context)

This module handles the core quantification of value changes during a game.

*   **Markov Chain Modeling:** Tools for modeling Base-Out State (BOS) transitions to calculate **expected runs scored** from a given state. This calculation forms the foundational expected run value $V(i)$ for many pitch outcomes.
*   **Hierarchical Attribution:** Implement a framework for attributing value to individual players (batter, pitcher, catcher) by comparing actual results to predictions from a league-average player, using **Hierarchical Mixed Effects Models**. This can be applied to:
    *   Play Value (change in BOS run state).
    *   Pitch Value (change in Base-Out-Count-Run state).
    *   Pickoff Value and Stolen Base Value, accounting for pitcher, catcher, and runner contributions.

*   **Availability/Temporal Models:** Include functionality for modeling time-dependent latent states, such as player availability (fitness/injury risk), possibly using **Hidden Markov Models (HMM)** to capture state persistence and predict long-term injury expectations based on observed play states (Start, Play, Rest, IL).

#### 5. `sportypy.predict` (Model Wrappers)

This module will offer high-level wrappers for prediction, analogous to scikit-learn or AutoGluon, focused on sports outcome prediction.

*   **Regression and Classification:** Implement wrappers for common models used in sports prediction, such as **Logistic Regression** (for binary outcomes like win/loss or shot make/miss), Linear Regression, and Generalized Linear Models (GLMs) like **Poisson Regression** (useful for modeling count data like goals or corner kicks).
*   **Ensemble & Deep Learning:** Simple APIs for applying complex models that capture nonlinear relationships, such as **Random Forest**, **Support Vector Machines (SVM)**, and Deep Neural Networks (DNNs).
*   **Head-to-Head Matchups:** Tools to structure inputs for predicting team matchups, drawing on features like team performance aggregates (shooting, turnovers, rebounding) and Elo ratings.

#### 6. `sportypy.data` (Data Acquisition and Preprocessing)

This module handles seamless integration with external sports data sources.

*   **Data Connectors:** Provide utilities for connecting to common public APIs and specialized libraries (e.g., leveraging `nba_api`, `nflfastR`, `sportsreference`, or `py_football` concepts) to collect and parse statistics.
*   **Preprocessing Utilities:** Functions for standard tasks like feature standardization and normalization, as well as domain-specific feature creation (e.g., True Shooting Percentage, Rushing Yards Over Expected, Completion Percentage Over Expected).

***

The proposed SportyPy library acts as a sophisticated toolbox, integrating proven methods like Hierarchical Gaussian Processes for spatial analysis and Causal Inference for bias adjustment, encapsulated within flexible Python classes. It is modeled after the probabilistic approach seen in the advanced baseball projection systems that quantify true talent ($\gamma$) and future uncertainty.
