import numpy as np
import matplotlib.pyplot as plt

last_iteration_start = 0

batch_num = 100000
batch = np.arange(0, 100000, 1)
# cycle_size = np.linspace(0, 5000, len(batch))
cycle_size = 5000
batches_cycle_mult = 1.5
learning_rate_min = 0.00001
learning_rate = 0.001

while ((last_iteration_start + cycle_size) < batch_num):
    print('last iteration start:\t', last_iteration_start)
    print('cycle size:\t\t', cycle_size)
    last_iteration_start += cycle_size

    cycle_size *= batches_cycle_mult


print('last iteration start:\t', last_iteration_start)
print('cycle size:\t\t', cycle_size)
# batch =
# rate = learning_rate_min+0.5*(learning_rate - learning_rate_min)*(1. + np.cos((batch_num - last_iteration_start)*np.pi / cycle_size))
