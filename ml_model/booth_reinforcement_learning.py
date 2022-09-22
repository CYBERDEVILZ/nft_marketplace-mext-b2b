'''
    The model is powered by a reinforcement learning algorithm
    known as UCB Bandit (UCB-1). From a dynamic dataset, 
'''

# basic imports
import pandas as pd
import math

# read csv
# NOTE: the dataset is collected on a user-to-user basis.
# Each entry represents the NFT bought by the user in that 
# particular session.
dataset = pd.read_csv('../dataset/realtime_company_buy_data.csv')


# Implementing Reinforcement algorithm: UCB-1 Bandit
DATASET_SIZE = len(dataset)

no_of_companies = len(dataset.columns)
companies_selected = []
numbers_of_selections = [0] * no_of_companies
sums_of_reward = [0] * no_of_companies
total_reward = 0

for n in range(0, DATASET_SIZE):
    company = 0
    max_upper_bound = 0

    for i in range(0, no_of_companies):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_reward[i] / numbers_of_selections[i]
            delta_i = math.sqrt(2 * math.log(n+1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400

        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            company = i

    companies_selected.append(company)
    numbers_of_selections[company] += 1
    reward = dataset.values[n, company]
    sums_of_reward[company] += reward
    total_reward += reward


print(total_reward)
print(pd.Series(companies_selected).head(1500).value_counts(normalize=True))

