# Write a program to find the simple interest when the value of principle ,rate of interest and time period is given.

principle = 5000
rate_of_interest = 6
time_period = 3

def simple_interest(P, T, R):
    return f"Simple Interest for Principle ${P}, Rate of interest {R}% and Time period {T} years is {(P * T * R) / 100}"



print(simple_interest(principle, rate_of_interest, time_period))
