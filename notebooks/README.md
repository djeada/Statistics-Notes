# Notebooks

The notebooks mirror the same curriculum as [`notes/`](../notes/README.md) and [`scripts/`](../scripts/README.md). They are the interactive layer: use them when simulation, repeated sampling, model comparison, or exploratory computation adds more value than a static example.

| Unit | Notebooks |
|---|---|
| Foundations | [`foundations/`](foundations/) |
| Probability | [`probability/`](probability/) |
| Random Variables & Distributions | [`random_variables_and_distributions/`](random_variables_and_distributions/) |
| Joint Distributions & Covariance | [`joint_distributions_and_covariance/`](joint_distributions_and_covariance/) |
| Sampling & Sampling Distributions | [`sampling_and_sampling_distributions/`](sampling_and_sampling_distributions/) |
| Estimation | [`estimation/`](estimation/) |
| Hypothesis Testing & Confidence Intervals | [`hypothesis_testing_and_confidence_intervals/`](hypothesis_testing_and_confidence_intervals/) |
| Regression | [`regression/`](regression/) |
| Resampling & Model Assessment | [`resampling_and_model_assessment/`](resampling_and_model_assessment/) |
| Time Series | [`time_series/`](time_series/) |
| Spatial Statistics | [`spatial_statistics/`](spatial_statistics/) |
| Extensions | [`extensions/`](extensions/) |

## Working with the notebooks

Launch Jupyter from the repository root after installing `requirements.txt`:

```bash
jupyter notebook
```

New curriculum notebooks use deterministic random seeds and are written so their code cells can be executed from top to bottom. Older notebooks are preserved as content-identical moves wherever possible.
