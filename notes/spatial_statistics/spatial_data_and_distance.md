# Spatial Data, Support, and Distance

Spatial analysis begins before any spatial statistic is computed. The first decisions are what the spatial observation represents, which coordinate system is being used, what spatial support each value summarizes, and which notion of distance is scientifically meaningful.

## Spatial Data Objects

Three objects recur throughout this unit.

### Areal or lattice data

A value is attached to a region or cell:

$$
y_i \quad \text{for region } A_i.
$$

Examples include unemployment by county, disease incidence by district, or crop yield by field. Neighborhood is often based on shared boundaries or centroid distance.

### Point-referenced measurements

A quantity is measured at sampling locations:

$$
Z(s_i), \qquad s_i \in \mathbb{R}^2.
$$

Examples include soil pH, rainfall, or pollution measured at monitoring stations. Here the locations are usually treated as design points and the random field $Z(s)$ is the object of interest.

### Point patterns

The observed outcome is the set of locations itself:

$$
\{s_1,\ldots,s_N\}.
$$

Examples include tree locations, earthquake epicenters, or incident locations. The number of events and their positions are random.

## Coordinate Reference Systems

Longitude and latitude are angular coordinates on the Earth. A Euclidean distance such as

$$
\sqrt{(\Delta \text{longitude})^2+(\Delta \text{latitude})^2}
$$

is measured in degrees, not kilometers, and the physical length represented by a degree of longitude changes with latitude.

For local planar analysis, a suitable projected coordinate reference system makes Euclidean distance interpretable in meters or another linear unit. For large geographic extents, great-circle/geodesic distances may be more appropriate.

The companion script [`spatial_data_and_distance.py`](../../scripts/spatial_statistics/spatial_data_and_distance.py) contrasts degree-space distance with a great-circle calculation.

## Spatial Support

**Support** is the region over which a measurement is defined.

A temperature sensor may approximate point support. A satellite pixel is an area average. A county unemployment rate summarizes an administrative polygon. Two variables observed at the same centroid can still have different support.

Changing support can change:

- variance;
- apparent smoothness;
- correlation;
- regression coefficients;
- detected clusters.

This is one reason spatial aggregation is not a harmless data-cleaning step.

## Scale and the MAUP

For areal data, results can depend on how boundaries are drawn and on the level of aggregation. This is the **modifiable areal unit problem (MAUP)**.

It has two related forms:

- **scale effect:** results change when small regions are aggregated into larger regions;
- **zoning effect:** results change when boundaries are redrawn while using roughly the same number of regions.

A spatial result should therefore name the spatial unit to which it applies.

## Distance Is a Modeling Choice

Euclidean distance is appropriate when straight-line proximity is scientifically meaningful. Other applications may require:

- road-network distance;
- travel time;
- river-network distance;
- ecological resistance distance;
- great-circle distance;
- directional or anisotropic distance.

Changing the metric changes which observations are considered close and therefore changes weights, covariance models, and validation blocks.

## Boundary Effects

Observations near the edge of a study region have less surrounding space observed than interior observations. This matters especially for point-process summaries and neighborhood construction.

The boundary is part of the observation process, not merely a plotting detail.

## Before Modeling

Record explicitly:

1. the spatial object being modeled;
2. the coordinate system and units;
3. the support of each observation;
4. the study-region boundary;
5. the scientific distance or neighborhood definition;
6. the spatial scale at which the conclusion is intended to hold.

Only after these choices are clear should the analysis proceed to [spatial weights](spatial_weights.md), [geostatistics](geostatistics.md), or [point processes](point_processes.md).
