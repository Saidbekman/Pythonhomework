# Homework:

# Exercise 1: Threaded Prime Number Checker
# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.
import threading
prime_numbers = []
lock = threading.Lock()

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    with lock:
        prime_numbers.extend(local_primes)

def threaded_prime_checker(range_start, range_end, thread_count):
    threads = []
    step = (range_end - range_start) // thread_count

    for i in range(thread_count):
        start = range_start + i * step
        end = range_start + (i + 1) * step if i < thread_count - 1 else range_end
        t = threading.Thread(target=check_primes, args=(start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ Topilgan tub sonlar:")
    print(sorted(prime_numbers))
if __name__ == "__main__":
    range_start = int(input("Boshlanish sonini kiriting: "))
    range_end = int(input("Tugash sonini kiriting: "))
    thread_count = int(input("Nechta thread ishlatilsin: "))
    
    threaded_prime_checker(range_start, range_end, thread_count)

# Exercise 2: Threaded File Processing
# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.
import threading
from collections import Counter
import os
word_counts = Counter()
lock = threading.Lock()

def process_lines(lines):
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)
    
    with lock:
        word_counts.update(local_counter)

def threaded_file_processor(filename, thread_count=4):
    with open(filename, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    total_lines = len(all_lines)
    step = total_lines // thread_count

    threads = []

    for i in range(thread_count):
        start = i * step
        end = (i + 1) * step if i != thread_count - 1 else total_lines
        part = all_lines[start:end]
        t = threading.Thread(target=process_lines, args=(part,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n📊 So‘zlar soni (top 10):")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")
if __name__ == "__main__":
    filename = input("Matnli fayl nomini kiriting (masalan: sample.txt): ")
    if not os.path.exists(filename):
        print("❌ Fayl topilmadi.")
    else:
        thread_count = int(input("Nechta thread ishlatilsin: "))
        threaded_file_processor(filename, thread_count)
