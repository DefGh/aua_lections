# Sampling And Sampling Distributions

## standard error of the mean for normal distribution

$$ \sigma_{\bar{x}} = {\sigma \over  \sqrt{n}}  $$

where
- $\sigma_{\bar{x}}$ is the standard error of the mean
- $\sigma$ is the standard deviation of the population
- $n$ is the sample size

## standard error for proportion

$$ \sigma_{\bar{p}} = \sqrt{ {p(1-p) \over n} } $$

where 
- $\sigma_{\bar{p}}$ is the standard error of the proportion
- $p$ is the proportion of the population
- $1-p$ is the complement of the proportion of the population
- $n$ is the sample size

## for the z-Score for the Sample Mean

$$ z = { \bar{x} - \mu \over \sigma_{\bar{x}} } $$

where
- $z$ is the z-score
- $\bar{x}$ is the sample mean
- $\mu$ is the population mean
- $\sigma_{\bar{x}}$ is the standard error of the mean

## for the z-Score for the Sample Proportion

$$ z = { \bar{p} - p \over \sigma_{\bar{p}} } $$

where
- $z$ is the z-score
- $\bar{p}$ is the sample proportion
- $p$ is the population proportion
- $\sigma_{\bar{p}}$ is the standard error of the proportion

## standard error for the finite population

$$ \sigma_{\bar{x}} = {\sigma \over  \sqrt{n}} \sqrt{N-n \over N-1} $$

where
- $\sigma_{\bar{x}}$ is the standard error of the mean
- $\sigma$ is the standard deviation of the population
- $n$ is the sample size
- $N$ is the population size

## standard error for the finite population proportion

$$ \sigma_{\bar{p}} = \sqrt{ {p(1-p) \over n} } \sqrt{N-n \over N-1} $$

where
- $\sigma_{\bar{p}}$ is the standard error of the proportion
- $p$ is the proportion of the population
- $1-p$ is the complement of the proportion of the population
- $n$ is the sample size
- $N$ is the population size

# Confidence Intervals

## Standard error of the mean

$$ \sigma_{\bar{x}} = {\sigma \over  \sqrt{n}}  $$

## Confidence interval for the mean ($\sigma$ known)

$$ CL = \bar{x} \pm z_{\alpha/2} \sigma_{\bar{x}} $$

where

- $CL$ is the confidence interval
- $\bar{x}$ is the sample mean
- $z_{\alpha/2}$ is the z-score for the desired confidence level
- $\sigma_{\bar{x}}$ is the standard error of the mean

## Margin of error

$$ ME = z_{\alpha/2} \sigma_{\bar{x}} $$

where

- $ME$ is the margin of error
- $z_{\alpha/2}$ is the z-score for the desired confidence level
- $\sigma_{\bar{x}}$ is the standard error of the mean

## Confidence interval for the mean ($\sigma$ unknown)

## Sample standard deviation

$$ s = \sqrt{ { \sum (x - \bar{x})^2 \over n-1 } } $$

where

- $s$ is the sample standard deviation
- $x$ is the data point
- $\bar{x}$ is the sample mean
- $n$ is the sample size

## Approximate Standard Error of the Mean

$$ s_{\bar{x}} = {s \over \sqrt{n}} $$

where

- $s_{\bar{x}}$ is the approximate standard error of the mean
- $s$ is the sample standard deviation
- $n$ is the sample size

## Degrees of freedom

$$ df = n - 1 $$

where

- $df$ is the degrees of freedom
- $n$ is the sample size

## Confidence interval for the mean ($\sigma$ unknown)

$$ CL = \bar{x} \pm t_{\alpha/2, df} s_{\bar{x}} $$

where

- $CL$ is the confidence interval
- $\bar{x}$ is the sample mean
- $t_{\alpha/2, df}$ is the t-score for the desired confidence level and degrees of freedom
- $s_{\bar{x}}$ is the approximate standard error of the mean

## standard error of the proportion

$$ \sigma_{\bar{p}} = \sqrt{ {p(1-p) \over n} } $$

## Confidence interval for the proportion

$$ CL = \bar{p} \pm z_{\alpha/2} \sigma_{\bar{p}} $$

where

- $CL$ is the confidence interval
- $\bar{p}$ is the sample proportion
- $z_{\alpha/2}$ is the z-score for the desired confidence level
- $\sigma_{\bar{p}}$ is the standard error of the proportion

### how to find the z-score for a given confidence level
> for a 95% confidence level, the z-score is 1.96  
> for a 99% confidence level, the z-score is 2.58  
> for a 90% confidence level, the z-score is 1.64  
> get the  $ P =\alpha/2$ and look up the closest value in the z-table

# Calculating Sample Size

## Sample size for the mean

$$ n = \left( {z_{\alpha/2} \sigma \over E} \right)^2 $$

where

- $n$ is the sample size
- $z_{\alpha/2}$ is the z-score for the desired confidence level
- $\sigma$ is the standard deviation of the population
- $E$ is the margin of error

## Sample size for the proportion

$$ n = \left( {z_{\alpha/2} \sqrt{p(1-p)} \over E} \right)^2 $$

where

- $n$ is the sample size
- $z_{\alpha/2}$ is the z-score for the desired confidence level
- $p$ is the proportion of the population
- $E$ is the margin of error

## Margin of error

$$ E = z_{\alpha/2} \times \sigma_{\bar{x}}  $$

where

- $E$ is the margin of error
- $z_{\alpha/2}$ is the z-score for the desired confidence level
- $\sigma_{\bar{x}}$ is the standard error of the mean


# Hypothesis Testing

## Steps for hypothesis testing

1. State the null hypothesis ($H_0$) and the alternative hypothesis ($H_1$)
2. Choose the significance level ($\alpha$)
3. Calculate the test statistic
4. Determine the critical value
5. Compare the test statistic to the critical value
6. Make a decision

## Test statistic for the mean

$$ z = { \bar{x} - \mu \over \sigma_{\bar{x}} } = {\bar{x} - \mu \over \frac{\sigma}{n}} $$

where

- $z$ is the z-score
- $\bar{x}$ is the sample mean
- $\mu$ is the population mean
- $\sigma_{\bar{x}}$ is the standard error of the mean

## Test statistic for the proportion

$$ z = { \bar{p} - p \over \sigma_{\bar{p}} } = {\bar{p} - p \over \sqrt{ {p(1-p) \over n} }} $$

where

- $z$ is the z-score
- $\bar{p}$ is the sample proportion
- $p$ is the population proportion
- $\sigma_{\bar{p}}$ is the standard error of the proportion

# Comparing Two Population Means

## Standard error of the difference between two means

$$ \sigma_{\bar{x}_1 - \bar{x}_2} = \sqrt{ {\sigma_1^2 \over n_1} + {\sigma_2^2 \over n_2} } $$

where

- $\sigma_{\bar{x}_1 - \bar{x}_2}$ is the standard error of the difference between two means
- $\sigma_1$ is the standard deviation of the first population
- $\sigma_2$ is the standard deviation of the second population
- $n_1$ is the sample size of the first population
- $n_2$ is the sample size of the second population

## Standard error of the difference between two means (pooled)

$$ t_{\bar{x}}= {(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2) \over \sqrt{ s_p^2 \left( {1 \over n_1} + {1 \over n_2} \right) } } $$

where

- $t_{\bar{x}}$ is the t-score
- $\bar{x}_1$ is the sample mean of the first population
- $\bar{x}_2$ is the sample mean of the second population
- $\mu_1$ is the population mean of the first population
- $\mu_2$ is the population mean of the second population
- $s_p^2$ is the pooled variance

## Pooled variance

$$ s_p^2 = { (n_1 - 1)s_1^2 + (n_2 - 1)s_2^2 \over n_1 + n_2 - 2 } $$

where

- $s_p^2$ is the pooled variance
- $n_1$ is the sample size of the first population
- $s_1^2$ is the sample variance of the first population
- $n_2$ is the sample size of the second population
- $s_2^2$ is the sample variance of the second population

