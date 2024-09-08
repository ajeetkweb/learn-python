import multiprocessing

def square_numbers(numbers, result, index):
    for i, n in enumerate(numbers):
        result[index + i] = n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    result = multiprocessing.Array('i', len(numbers))
    
    # Divide the list of numbers into two halves for two processes
    mid = len(numbers) // 2
    process1 = multiprocessing.Process(target=square_numbers, args=(numbers[:mid], result, 0))
    process2 = multiprocessing.Process(target=square_numbers, args=(numbers[mid:], result, mid))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Squared numbers:", list(result))
