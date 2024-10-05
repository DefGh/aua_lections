
import math

def PMF(x: int, lamd: float, comulative: bool = False) -> float:
    if comulative:
        return sum([PMF(i, lamd) for i in range(0, x+1)])
    
    
    lsqr = math.pow(lamd, x)
    eminx = math.pow(math.e, - lamd)
    factor = math.factorial(x)

    return (lsqr * eminx)/(factor)



# _lambda = 2.6


# zero = PMF(0, _lambda)

# print(f'Probability of zero births is {zero}')

# less_then_four = (PMF(0, _lambda) + PMF(1, _lambda) + PMF(2, _lambda) + PMF(3, _lambda))

# print(f'Probability of less then 4 births i {less_then_four}')

# more_then_one = 1 -(PMF(0, _lambda) + PMF(1, _lambda) )

# print(f'Probability of more then 1 births i {more_then_one}')

# _lambda = 12 / 2

# four = PMF(4, _lambda)

# print(f'Probability of 4 customers is {four*100:.2f}%')


# Applications of Poisson Distribution
# EXAMPLE 3
# Sara is a salesperson for Camera’s Etc., which is a retailer for high-end digital cameras.
# Historically, Sara has averaged selling 2.1 extended warranties per day for cameras that she sells.
# Assume the number of camera warranties that Sara sells per day follows the Poisson distribution.
# a. What is the probability that Sara will sell five extended warranties tomorrow?
# b. What is the probability that Sara will not sell an extended warranty tomorrow?
# c. What is the probability that Sara will sell more than two extended warranties tomorrow?
# d. What is the standard deviation for this distribution?

_lambda = 2.1

five = PMF(5, _lambda)
print(f'Probability of 5 extended warranties is {five*100:.2f}%')

zero = PMF(0, _lambda)
print(f'Probability of zero extended warranties is {zero*100:.2f}%')

more_then_two = 1 -PMF(2, _lambda, True)
print(f'Probability of more then 2 extended warranties is {more_then_two*100:.2f}%')

std_dev = math.sqrt(_lambda)
print(f'Standard deviation for this distribution is {std_dev:.4f}')


print("|number|probability|less then|less then or equal|more then|more then or equal|")
print("|------|-----------|---------|------------------|---------|------------------|")

for i in range(0, 20):
    print(f'|{i:6}|{PMF(i, _lambda)*100:.6f}|{PMF(i-1, _lambda, True)*100:.6f}|{PMF(i, _lambda, True)*100:.6f}|{(1-PMF(i, _lambda, True))*100:.6f}|{(1-PMF(i-1, _lambda, True))*100:.6f}|')

