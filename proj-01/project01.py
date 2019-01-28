#!/usr/bin/env

# EE 381 Spring 2019 Project 01
# David Taitingfong
# 016695521
# Start  Date: 01-23-2019
# End Date:    01-??-2019
# ------------------------------------
# This project does summary statistics
# and a Pareto chart
# ------------------------------------

def main():
    L = []  # Empty list for data
    v = 1   # Initial value for boolean variable

    print('You will be asked to input non-negative integers.')
    print('When you are done, enter a letter to stop.')

    while v == 1:
        try:
            l = int(input('Enter a non-negative integer: '))
            if (l < 0):
                print('\nERROR: That number is negative. Please enter a non-negative integer\n')
            else:
                L.append(l)
        except ValueError:
            print('Input halted.')
            print('\n')
            v = 0

    print('You inputted the following list of numbers: ', L)
    print('\n')

    N = len(L)  # Number of integers in the list
    get_mean(L, N)
    get_median(L, N)
    get_mode(L)

    # Range - Hi vs lo
    range = L[len(L)-1] - L[0]

    # Variance
    # sum((x - mu)^2) / N

    # Standard Deviation
    # sqrt(variance)

    # Pareto chart created w/ household spending data given

def get_mean(L, N):
    # Calculation of the mean
    s = sum(L)  # The sum of the inputted numbes
    N = len(L)
    mean = s / N
    print('The mean of the numbers entered is {}'.format(mean))
    # ---------------------------------------------------------

def get_median(L, N):
    L.sort()  # Sort the list
    # It is necessary to determine whether or not the length of the list is even
    # or odd
    if N % 2 == 0:
        # Even
        median = (L[N//2] + L[(N//2) - 1]) / 2
    else:
        # Odd
        median = L[N//2]
    print('The median of the numbers entered is {}'.format(median))

def get_mode(L):
    pass

def get_range():
    pass

def get_variance():
    pass

def get_std_dev():
    pass

if __name__ == "__main__":
    main()