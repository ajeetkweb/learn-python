import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(f"Letter: {letter}")

if __name__ == "__main__":

    start_time = time.time()
    # Create process objects
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    print("Done in", time.time() - start_time)
    print("Both processes finished execution!")





