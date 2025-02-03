import sys
import time

'''
File version before pylint
'''

def read_numbers_from_file(filename):
    """Reads numbers from a file, handling invalid data."""
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Warning: Invalid data skipped -> {line.strip()}")
    return numbers

def compute_mean(data):
    """Computes mean using basic sum and division."""
    return sum(data) / len(data) if data else 0

def compute_median(data):
    """Computes median by sorting and finding the middle value."""
    n = len(data)
    if n == 0:
        return 0
    data.sort()
    mid = n // 2
    return (data[mid] + data[mid - 1]) / 2 if n % 2 == 0 else data[mid]

def compute_mode(data):
    """Computes mode using a frequency count."""
    if not data:
        return None
    freq = {}
    for num in data:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_freq]
    return modes[0] if len(modes) == 1 else modes  # Return single mode or list

def compute_variance(data, mean):
    """Computes variance using the basic formula."""
    n = len(data)
    return sum((x - mean) ** 2 for x in data) / (n - 1) if n > 1 else 0

def compute_std_dev(variance):
    """Computes standard deviation as sqrt of variance."""
    return variance ** 0.5

def write_results_to_file(results, elapsed_time):
    """Writes statistics results to an output file."""
    with open('StatisticsResults.txt', 'w') as file:
        file.write(results + f"\nExecution Time: {elapsed_time:.4f} seconds\n")

def main():
    """Main function to handle file reading, computation, and output."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <fileWithData.txt>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        start_time = time.time()
        data = read_numbers_from_file(filename)
        
        if not data:
            print("Error: No valid numbers found in the file.")
            sys.exit(1)
        
        mean = compute_mean(data)
        median = compute_median(data)
        mode = compute_mode(data)
        variance = compute_variance(data, mean)
        std_dev = compute_std_dev(variance)
        
        elapsed_time = time.time() - start_time
        results = (f"Mean: {mean}\nMedian: {median}\nMode: {mode}\n"
                   f"Variance: {variance}\nStandard Deviation: {std_dev}")
        print(results + f"\nExecution Time: {elapsed_time:.4f} seconds")
        write_results_to_file(results, elapsed_time)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
