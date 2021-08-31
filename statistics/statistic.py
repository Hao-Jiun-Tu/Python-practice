# STATISTICS
import random
data = random.choice([1, 5, 6, 10, 20])
print(data)
data = random.sample([1, 5, 6, 10, 20], 3)
print(data)
data = [1, 5, 8, 20]
random.shuffle(data)           # change order randomly
print(data)
data = random.uniform(60, 100) # random number betwenn 60 to 100
print(data)
# normal distribution
# mean = 100, stdev = 10
data = random.normalvariate(100, 10)
print(data)

import statistics as stat
data = stat.mean([1, 4, 5, 8])
print(data)
data = stat.median([1, 2, 3, 4, 5, 8, 100])
print(data)
data = stat.stdev([1, 2, 3, 4, 5, 8, 100])
print(data)

