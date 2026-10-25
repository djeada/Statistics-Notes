# Spatial Statistics

Spatial statistics studies observations whose locations, distances, neighborhoods, or spatial supports are part of the probability model. Nearby measurements can share environmental influences, and neighboring regions can affect one another. Treating every row as an independent replicate can then overstate information and produce uncertainty estimates or validation scores that do not match the intended task.

## Identify what is random

| Spatial object | Example | What the model describes | Useful representation |
|---|---|---|---|
| Areal or lattice observations | Disease rate by district | Values associated with regions | Regions and a neighborhood graph |
| Point-referenced measurements | Soil pH at sampled coordinates | Measured values at sampling sites | A random field and covariance model |
| Point pattern | Tree or event locations | The event locations themselves | Intensity and interaction |
| Raster or gridded field | Temperature over grid cells | Values or averages on cells | A field with explicit cell support |

In point-referenced data, sampling locations are often conditioned on and the measured quantity is modeled. In a point process, the locations themselves are outcomes. A dense group of measurements can therefore reflect an intensive sampling design, whereas a dense group of events can be a feature of the process being studied. Confusing the two leads to inappropriate summaries of clustering.

## Coordinates, distance, and support

A coordinate reference system describes how locations are represented. A distance metric describes how separation is measured. Longitude and latitude are angles, so a Euclidean distance in degrees is usually unsuitable as a physical distance. A projected coordinate system can make local metric calculations convenient, while a geodesic distance may be preferable over larger regions.

Support is the region or volume represented by a value. A point reading, a pixel average, and a district rate are different observations even when they are drawn at the same map coordinate. Averaging over a region smooths fine-scale variation, and changing boundaries can change apparent associations. A spatial analysis should state the measurement support as well as the coordinates.

## Mean structure and dependence

Broad variation in a mean or intensity is first-order structure. Dependence between departures from that mean is second-order structure. An unmodeled geographic trend can make nearby values look similar without establishing a stationary residual covariance. Detrending and substantive covariates help separate those mechanisms, although the separation is always conditional on the chosen model.

Spatial weights describe a neighborhood graph, such as contiguity or a distance threshold. They do not automatically define a valid covariance function. Covariance and variogram models instead specify stochastic relationships across separations and must satisfy validity conditions. Point-process models use intensity for event density and interaction summaries for structure beyond that density.

## From description to prediction

Spatial autocorrelation measures summarize how observed values relate across a chosen neighborhood system. Global summaries can conceal local differences, and local significance maps introduce multiple comparisons. The weights, null model, and permutation scheme are part of the meaning of the result.

Geostatistics uses random fields and variograms to describe point-referenced measurements. Nugget, sill, range, and directional dependence express different features of a covariance model. Kriging converts that model into prediction weights and a conditional uncertainty calculation. Its reported variance is conditional on the fitted covariance assumptions and usually omits uncertainty in estimated covariance parameters.

Spatial regression separates covariate associations from residual dependence or modeled spillover. In a spatial lag model, feedback through neighboring responses means that a coefficient is not automatically the complete marginal effect. Point-process analysis addresses a different target: where events occur and whether their arrangement departs from an appropriate intensity model.

## Match validation to geographic use

Random folds can assess interpolation when held-out locations remain close to training sites. Geographic blocks or buffers assess tasks with greater separation, such as transfer to another region. Neither split is universally correct: each estimates performance under a different relationship between training and prediction locations.

A practical workflow is to define the spatial object and target, inspect coordinates and support, model the broad mean or intensity, choose a dependence representation, diagnose residual structure, and validate at the separation relevant to deployment. Prediction uncertainty and error summaries should state those assumptions explicitly.

The numerical examples use the repository's NumPy, SciPy, statsmodels, and scikit-learn environment and expose core formulas directly. Dedicated packages such as PySAL, GeoPandas, PyKrige, GSTools, and `spatstat` provide additional spatial tools. Their conventions still require checking: distance units, weight normalization, variogram parameterization, and the meaning of prediction variance can differ between implementations.
