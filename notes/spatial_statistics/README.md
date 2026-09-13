# Spatial Statistics

Spatial statistics studies observations whose dependence is related to location. The right starting chapter depends on what kind of spatial object is observed.

## Choose by Data Type

| Spatial data | Start here | Typical question |
|---|---|---|
| Locations of events themselves | **[Point Processes](point_processes.md)** | Are events clustered, inhibited, or consistent with a reference point process? |
| Measurements attached to regions or neighboring units | **[Spatial Autocorrelation](spatial_autocorrelation.md)** | Are nearby areas more similar than expected under spatial randomness? |
| A continuous quantity observed at sampled coordinates | **[Geostatistics](geostatistics.md)** | How does similarity change with distance, and how can values be interpolated? |

## Prerequisites and Connections

Covariance and correlation provide useful background: see **[Correlation and Regression](../correlation_and_regression/README.md)**. Spatial dependence plays a role analogous to serial dependence in **[Time Series Analysis](../time_series_analysis/README.md)**: observations that are close in space or time often cannot be treated as independent replicates.

## Terminology Boundary

Do not use “spatial autocorrelation,” “geostatistics,” and “point process” interchangeably. They can all describe spatial dependence, but they model different data objects and answer different questions. Identifying the observed spatial object is the first modeling decision.