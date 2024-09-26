import psutil
import multiprocessing as mp

def func(x):
    return x**2

def par_func(x):
    num_cores = psutil.cpu_count(logical=False)  # Determine number of cores
    num_workers = num_cores-4 # Leave some cores free
    with mp.Pool(num_workers) as p:
        results = p.map(func,x)
    return results