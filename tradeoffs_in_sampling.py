import numpy as np

def simulate_sampling(population_size, proportion_plus_one, sample_size, num_simulations):
    count_majority_plus_one = 0

    for _ in range(num_simulations):

        population = np.random.choice([1, -1], size=population_size, p=[proportion_plus_one, 1 - proportion_plus_one])


        sample = np.random.choice(population, size=sample_size, replace=False)

        count_plus_one = np.sum(sample == 1)


        if count_plus_one > sample_size / 2:
            count_majority_plus_one += 1


    probability_majority_plus_one = count_majority_plus_one / num_simulations

    return probability_majority_plus_one


sample_sizes = [20, 100, 400]
num_simulations = 100

for sample_size in sample_sizes:
    probability = simulate_sampling(1000000, 0.52, sample_size, num_simulations)
    print("For sample size {}, average probability: {}".format(sample_size, probability))


current_sample_size = 400
while probability < 0.9:
    current_sample_size += 10  
    probability = simulate_sampling(1000000, 0.52, current_sample_size, num_simulations)

print("To achieve a probability of 0.9, you need a sample size of {}".format(current_sample_size))

