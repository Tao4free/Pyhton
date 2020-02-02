import numpy as np

a = np.array([[1, 2], [3, 4]])
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))
print(np.mean(a, axis=(0, 1)))

x = np.concatenate([np.random.exponential(size=200), np.random.normal(size=100)])
# print("\n", x)
n = len(x)
reps = 10000
xb = np.random.choice(x, (n, reps))
mb = xb.mean(axis=0)
percentile = np.percentile(mb, [2.5, 97.5])
mb.sort()
percentile_sort = np.percentile(mb, [2.5, 97.5])
print("\n{} \n{}".format(percentile, percentile_sort))
