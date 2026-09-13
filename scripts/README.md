# Scripts

The runnable examples mirror the same dependency-aware curriculum as [`notes/`](../notes/README.md). Each unit directory contains small, standalone programs that make one statistical idea concrete.

| Unit | Scripts |
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

## Running an example

From the repository root:

```bash
python scripts/estimation/point_estimation.py
python scripts/time_series/forecast_backtesting.py
```

Scripts favor deterministic random seeds and explicit printed summaries so they can be rerun and compared easily. Plot-oriented historical examples remain available where visualization is central to the concept.
