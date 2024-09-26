import multiprocessing as mp
import psutil
import functools

# Define a Function you want to run in parallel
def func(num):
    return num**2

def func_2_inputs(num,offset):
    return num**2 + offset

# To run the function in paralle in a script, it needs to be protected by an
# if __name__=='__main__' statement. This is because Python has something
# called a Global Interpreter Lock (GIL) that prevents you from spawning
# multiple process. There is only ONE interpreter at a time to rpevent race
# conditions and the like.
if __name__ == '__main__':

    x = list(range(1,10))
    results = []

    # This would be the serial way of running it
    for num in x:
        results.append(func(num))
    print(results)
    
    # Launch a parallel process pool and use map to pass the inputs to fun
    with mp.Pool(5) as p:
        print(p.map(func, x))

    # When a function has multiple inputs but you only want to parallelize over 1
    # you can use functools.partial to freeze some of the variables
    y = 1
    with mp.Pool(5) as p:
        results = p.map(functools.partial(func_2_inputs, offset=y),x)
    print(results)