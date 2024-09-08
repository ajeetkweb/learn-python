import multiprocessing

def cube(x):
    return x ** 3

if __name__ == "__main__":
    # Create a pool of 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        results = pool.map(cube, numbers)
        print("Cubed numbers:", results)
