# Spatial Statistics

Spatial statistics studies observations whose locations, neighborhoods, or measurement regions affect the question being answered. The purpose is to represent how information is shared across space, what quantity each observation measures, and what can be learned at unobserved locations. A map helps display the data, but the statistical model must explain what is random and how the measurements relate to the target.

Consider three maps with exactly the same plotted coordinates. The first shows temperatures at monitoring stations, the second shows the locations of trees, and the third shows district admission rates at district centroids. Their dots look alike, but they require different probability models. In the first, a measured value is random at a sampling site; in the second, the locations and often their count are random; in the third, each value summarizes a region and population.

## Start with the Observation and Its Support

| Spatial object | Example | What the observation represents | Typical model ingredients |
|---|---|---|---|
| Point-referenced measurement | Soil pH at a sampling site | A measured value near a specified coordinate | Mean, spatial covariance, measurement error |
| Areal observation | Disease rate by district | Counts and a denominator over a region | Regional mean, population or exposure, neighborhood structure |
| Point pattern | Tree stems or event locations | Events inside an observation window | Intensity, count distribution, interaction, detection |
| Raster or gridded field | Temperature on pixels | Values or averages over cells | Cell support, covariance, spatial resolution |

The **support** of a measurement is the point, area, volume, or population it represents. A district average placed at a centroid is not a point measurement of the underlying field at that centroid. A one-kilometer pixel also averages variation that a small sensor may detect. Matching coordinates does not make these observations interchangeable.

For a continuous field Z, an area average is $Z_A=|A|^{-1}\int_A Z(s)\,ds$. Its variance depends on covariance between every pair of positions in A:

$$
\operatorname{Var}(Z_A)
=\frac1{|A|^2}\int_A\int_A C(s,t)\,ds\,dt.
$$

This is the mathematical reason that averaging can smooth a map. Independent small-scale fluctuations partly cancel; common fluctuations across the entire area do not. Changing support therefore changes the random variable and its covariance, not just the plotting resolution. Redrawing regional boundaries can also change predictor averages, outcome averages, and fitted associations, producing the scale and zoning forms of the modifiable areal unit problem.

For rates, preserve the denominator. Ten cases among 100 people and ten among 10,000 people are equal counts but very different observed rates and sampling precisions. A model of counts with population exposure is often a more faithful representation than a model that treats both reported rates as equally precise numerical measurements.

## Coordinates Describe Position; Distance Describes a Mechanism

A coordinate reference system defines how numerical positions relate to Earth. Longitude and latitude are angles. One degree of longitude is approximately 111.2 km at the equator and 55.6 km at latitude 60°, so ordinary Euclidean distance in degree coordinates has no single conversion to physical distance.

A suitable local projection permits planar calculations in meters or another stated unit. For broad geographic regions, a spherical or ellipsoidal geodesic can better represent surface separation. Neither geometry automatically represents the mechanism of interest. Pollution may follow groundwater flow, animals may move through a resistance landscape, and travel may be constrained by a road network. Two sites separated by a short straight line can be weakly connected along those routes.

Distance enters neighbor definitions, covariance functions, and validation splits. It therefore affects which information the analysis treats as shared. A covariance formula must also be valid on the chosen geometry: replacing Euclidean distance with an arbitrary travel-time distance does not automatically preserve positive semidefiniteness. Physical relevance and mathematical validity are both needed.

## Nearby Observations Can Share Information

Suppose two measurements each have variance four and correlation 0.8. The variance of their average is

$$
\operatorname{Var}\left(\frac{Z_1+Z_2}{2}\right)
=\frac14(4+4+2\times0.8\times4)=3.6.
$$

With independent measurements, it would be two. Treating strongly related readings as independent replicates can therefore overstate the precision of an average. Adding many instruments in one small patch may measure that patch well while providing limited coverage of a wider region.

Dependence can help a different task. Knowing a nearby measurement can reduce uncertainty about an unsampled site. If the mean is known to be 10, the observed value is 12, and its correlation with the target is 0.8 under an equal-variance Gaussian model, the best linear prediction is $10+0.8(12-10)=11.6$. Its error variance is $4(1-0.8^2)=1.44$.

These two results are consistent. Correlation makes observations partially redundant for estimating a shared mean, while making one observation informative about another. The calculation being performed determines whether that shared information reduces or increases the relevant uncertainty relative to an independence calculation.

## Separate Geographic Mean Change from Residual Dependence

Write a point-referenced observation as $Y(s)=m(s)+U(s)+\epsilon(s)$, with mean m, residual field U, and measurement error $\epsilon$. Broad mean variation is **first-order structure**. Covariance among deviations from that mean is **second-order structure**. In a point process, intensity plays the first-order role, while pair structure describes arrangement beyond intensity.

A simple transect shows why the distinction matters. Suppose $Y(s)=5+s+\epsilon(s)$, with independent errors of mean zero and variance 0.25. Neighboring raw values tend to be similar because their means are similar, even though errors at different sites are independent. At a nonzero separation h,

$$
\frac12E[(Y(s+h)-Y(s))^2]
=0.25+\frac{h^2}{2}.
$$

The expected half-squared difference grows with distance because the trend contributes $h^2/2$. Removing the correct trend leaves semivariance 0.25 at all distinct sites. A distance pattern in raw differences alone therefore does not establish a correlated residual process.

Trend and residual structure are not always identifiable cleanly from a finite map. A flexible smooth mean and a long-range random field can explain similar patterns. Scientific covariates, sampling design, model restrictions, and sensitivity analysis help assess that ambiguity; calling a fitted component “spatial” does not resolve it.

## A Neighborhood Matrix and a Covariance Model Have Different Jobs

A spatial weights matrix W defines how other observed values contribute to a location's neighborhood summary. With the convention $(Wx)_i=\sum_jw_{ij}x_j$, a binary row produces a neighbor sum, while a nonnegative row normalized to one produces a weighted average. Rook adjacency, queen adjacency, distance thresholds, and nearest-neighbor graphs encode different relationships.

A covariance matrix C instead describes joint stochastic variation. Its entries have units of the measured variable squared, and every linear combination must have nonnegative variance. A symmetric adjacency matrix can have negative eigenvalues and cannot generally be used directly as a covariance matrix.

Moran's I uses W to compare weighted products of centered observations with overall variation. Its reference distribution requires a null mechanism, such as exchangeable assignments of observed values to fixed locations. It is not an ordinary correlation coefficient with a universal range, and its common finite-sample randomization expectation is $-1/(n-1)$ for zero-diagonal weights. Local statistics describe configurations such as high-high or low-high; significance requires additional calibration and attention to multiple testing.

Geostatistics uses covariance or semivariogram models for point-referenced values. Under constant mean and second-order stationarity, the semivariogram satisfies $\gamma(h)=C(0)-C(h)$. Nugget, partial sill, scale, and directional behavior describe different features of this model. An empirical variogram estimates those relationships from pair differences, whose contributions are dependent because sites appear in multiple pairs.

## Prediction Requires Both a Target and a Mean Assumption

Kriging chooses weights using dependence among the observations as well as their dependence with a target. Two observations equally close to the target can receive different weights because one is more redundant with the remaining data. Ordinary kriging preserves an unknown constant mean, simple kriging uses a specified known mean, and universal kriging preserves a chosen trend basis.

The prediction target can be a latent field value, a new noisy reading, or a block average. A new instrument reading contains noise that an error-free latent target does not. A block average uses covariance integrated over the block. Its uncertainty includes covariance between point prediction errors, so averaging pointwise variances does not give a block prediction variance.

The usual kriging variance treats covariance parameters and model choices as fixed. Small reported variance can coexist with poor prediction if the mean, range, anisotropy, boundary behavior, or nugget interpretation is wrong. Gaussian assumptions justify particular probability intervals; the best-linear-predictor property by itself supplies a variance criterion rather than an exact tail distribution.

Spatial regression adds predictors to the mean and can represent correlated residuals through GLS, a spatial error model, or another covariance construction. A SAR outcome model instead links jointly determined responses. Its predictor impacts propagate through $(I-\rho W)^{-1}$, so a structural coefficient alone is not a complete direct or indirect association. Modeling spatial dependence can improve precision or prediction, but causal conclusions still need a defensible account of exposure assignment, confounding, and selection.

## Event Density Is Not an Event Probability

For a point process, intensity $\lambda(s)$ is an expected count density, with units such as events per square kilometer. It can exceed one. Probabilities are obtained through the count model and integration over a region, not by treating the intensity value as a probability.

For example, a homogeneous Poisson intensity of two events per square kilometer gives expected count six in a three-square-kilometer region. The probability of no event there is $e^{-6}\approx0.00248$. Conditional on a total count, homogeneous Poisson locations are uniform over the observed window; an inhomogeneous intensity gives conditional location density proportional to that intensity instead.

K and nearest-neighbor summaries assess spacing relative to a model, with edge correction because the window hides some possible neighbors. A dense patch can be caused by high environmental intensity or greater observation effort, rather than event-to-event attraction. Randomizing marks among fixed events asks yet another question, preserving the location pattern while testing the mark arrangement.

## Validate the Information Conditions That Will Actually Occur

A held-out measurement surrounded by nearby training measurements assesses an interpolation problem. Holding out a region or removing nearby training observations with a buffer assesses a different problem. Scores can change even for a correct model because the uncertainty remaining at the target changes with available neighbors.

Fit response-derived features, trend and covariance parameters, and tuning choices within the training stages of the procedure being evaluated. An external covariate map available at deployment can be legitimate test-site information; a held-out response hidden inside a precomputed neighborhood average is leakage. For geographic transfer, examine predictor overlap as well as distance, since a nearby site can still have unfamiliar environmental conditions.

Report losses at the relevant unit of use. Equal-observation, equal-region, and population-weighted scores can differ substantially. Fold-level errors, target-to-training distances, retained training sizes, and interval coverage show what an average score conceals. Repeated folds do not create independent landscapes, and resampling observed conditions cannot establish performance in an environmental regime absent from the data.
