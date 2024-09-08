import threading

# Shared variable
current_number = 1
max_number = 10

# Locks for synchronization
even_lock = threading.Lock()
odd_lock = threading.Lock()

# Start with the even lock acquired to let odd numbers print first
even_lock.acquire()

def print_odd_numbers():
    global current_number
    while current_number <= max_number:
        # Acquire the odd lock to print the next odd number
        odd_lock.acquire()
        if current_number % 2 != 0:
            print(f"Odd: {current_number}")
            current_number += 1
        # Release the even lock to allow even number to print
        even_lock.release()

def print_even_numbers():
    global current_number
    while current_number <= max_number:
        # Acquire the even lock to print the next even number
        even_lock.acquire()
        if current_number % 2 == 0:
            print(f"Even: {current_number}")
            current_number += 1
        # Release the odd lock to allow odd number to print
        odd_lock.release()

# Create threads
odd_thread = threading.Thread(target=print_odd_numbers)
even_thread = threading.Thread(target=print_even_numbers)

# Start threads
odd_thread.start()
even_thread.start()

# Wait for threads to complete
odd_thread.join()
even_thread.join()

print("Done!")
