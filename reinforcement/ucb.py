# Upper Confidence Bound

# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
import math  # for sqrt, log methods
# get row (N 'rounds') and col (d 'ads') values
(N, d) = (dataset.shape[0], dataset.shape[1])
nums_of_selections = [0] * d  # create vector of size 'd' initialize to 0
sums_of_rewards = [0] * d  # vector of sums of rewards for ads at each round
ads_selected = []  # vector containing ad selected at each round
total_reward = 0  # track 'click through rate'
# Compute avg reward of ad 'i' up to round 'n'
# loop over each row (round)
for n in range(N):
    max_upper_bound = 0  # initialize
    ad = 0  # initialize
    for i in range(d):  # loop over every column (ad) in each row
        # use strategy after 1st 10 rounds (to select all ads once)
        if (nums_of_selections[i] > 0):
            avg_reward = sums_of_rewards[i]/nums_of_selections[i]
            # UCB = avg reward + delta(i)
            delta_i = math.sqrt(1.5 * math.log(n+1)/nums_of_selections[i])
            upper_bound = avg_reward + delta_i
        else:
            upper_bound = 1e400  # set high UB to ensure initial ad selection
        if max_upper_bound < upper_bound:  # compare max ucb to each new ad
            max_upper_bound = upper_bound  # set new max UCB
            ad = i  # potential selected ad = current interval
    ads_selected.append(ad)  # add the selected ad
    nums_of_selections[ad] += 1  # update number of selection for selected ad
    # Update accumulated rewards (click through) for current round at current ad
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] += reward
    total_reward += reward


# Visualising the results
plt.hist(ads_selected)  # plot ad selection using histogram
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
