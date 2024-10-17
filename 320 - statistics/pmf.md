# Poisson Distribution

The Poisson distribution is a probability distribution that describes how many times an event is likely to occur within a specified period of time. It is used for independent events which occur at a constant rate within a given interval of time.


Probability Mass Function

The probability mass function (pmf) is a function that gives the probability that a discrete random variable is exactly equal to some value. The probability mass function is often the primary means of defining a discrete probability distribution, and such functions exist for either scalar or multivariate random variables whose domain is discrete.

$$ P(x) = \frac{\lambda^xe^{-\lambda}}{x!} $$

where:   
 - $P(x)$ is the probability of getting exactly x successes
 - $x$ is the number of successes
 - $\lambda$ is the average number of successes that occur in a specified region
 - $e$ is the base of the natural logarithm (approximately equal to 2.71828)

## EXAMPLE 
> Sara is a salesperson for Camera’s Etc., which is a retailer for high-end digital cameras.
> Historically, Sara has averaged selling 2.1 extended warranties per day for cameras that she sells.
> Assume the number of camera warranties that Sara sells per day follows the Poisson distribution.

|number|probability|less then|less then or equal|more then|more then or equal|
|------|-----------|---------|------------------|---------|------------------|
|     0|12.245643|0.000000|12.245643|87.754357|100.000000|
|     1|25.715850|12.245643|37.961493|62.038507|87.754357|
|     2|27.001642|37.961493|64.963135|35.036865|62.038507|
|     3|18.901150|64.963135|83.864285|16.135715|35.036865|
|     4|9.923104|83.864285|93.787388|6.212612|16.135715|
|     5|4.167704|93.787388|97.955092|2.044908|6.212612|
|     6|1.458696|97.955092|99.413788|0.586212|2.044908|
|     7|0.437609|99.413788|99.851397|0.148603|0.586212|
|     8|0.114872|99.851397|99.966269|0.033731|0.148603|
|     9|0.026804|99.966269|99.993073|0.006927|0.033731|
|    10|0.005629|99.993073|99.998702|0.001298|0.006927|
|    11|0.001075|99.998702|99.999776|0.000224|0.001298|
|    12|0.000188|99.999776|99.999964|0.000036|0.000224|
|    13|0.000030|99.999964|99.999995|0.000005|0.000036|
|    14|0.000005|99.999995|99.999999|0.000001|0.000005|
|    15|0.000001|99.999999|100.000000|0.000000|0.000001|
|    16|0.000000|100.000000|100.000000|0.000000|0.000000|
|    17|0.000000|100.000000|100.000000|0.000000|0.000000|
|    18|0.000000|100.000000|100.000000|0.000000|0.000000|
|    19|0.000000|100.000000|100.000000|0.000000|0.000000|
