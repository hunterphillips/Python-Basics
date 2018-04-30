# Thompson Sampling

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Thompson Sampling
import random
# get row (N 'rounds') and col (d 'ads') values
(N, d) = (dataset.shape[0], dataset.shape[1])
# vectors of sums of rewards for ads at each round
num_rewards_1 = [0] * d
num_rewards_0 = [0] * d
ads_selected = []  # vector containing ad selected at each round
total_reward = 0  # track 'click through rate'
# Compute avg reward of ad 'i' up to round 'n'
# loop over each row (round)
for n in range(N):
    ad = 0  # initialize
    max_random = 0
    for i in range(d):
        # generate random draw for each ad
        random_beta = random.betavariate(
            num_rewards_1[i]+1, num_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i  # potential selected ad = current interval
    ads_selected.append(ad)  # add the selected ad
    # Update accumulated rewards (click through) for current round at current ad
    reward = dataset.values[n, ad]
    if reward == 1:  # Update appropriate rewards vector
        num_rewards_1[ad] += 1
    else:
        num_rewards_0[ad] += 1
    total_reward += reward


# Visualising the results - Histogram
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
