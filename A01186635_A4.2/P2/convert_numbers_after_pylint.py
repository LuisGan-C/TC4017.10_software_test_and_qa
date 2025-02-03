"""
Module: convertNumbers.py
This script reads a file containing numerical data and converts each number
into its binary and hexadecimal representations using basic algorithms.
Results are printed to the console and saved to 'ConvertionResults.txt'.

File before pylint
"""

import sys
import time

def read_numbers_from_file(filename):
    """Reads numbers from a file, handling invalid data."""
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                numbers.append(int(line.strip()))
            except ValueError:
                print(f"Warning: Invalid data skipped -> {line.strip()}")
    return numbers

def to_binary(n):
    """Converts an integer to binary using basic algorithm."""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def to_hexadecimal(n):
    """Converts an integer to hexadecimal using basic algorithm."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_value = ""
    while n > 0:
        hex_value = hex_chars[n % 16] + hex_value
        n //= 16
    return hex_value

def write_results_to_file(results, elapsed_time):
    """Writes conversion results to an output file."""
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as file:
        file.write(results + f"\nExecution Time: {elapsed_time:.4f} seconds\n")

def main():
    """Main function to handle file reading, conversion, and output."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <fileWithData.txt>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        start_time = time.time()
        data = read_numbers_from_file(filename)
        if not data:
            print("Error: No valid numbers found in the file.")
            sys.exit(1)

        results = ""
        for num in data:
            binary = to_binary(num)
            hexa = to_hexadecimal(num)
            result_line = f"Number: {num} -> Binary: {binary}, Hexadecimal: {hexa}"
            print(result_line)
            results += result_line + "\n"

        elapsed_time = time.time() - start_time
        print(f"Execution Time: {elapsed_time:.4f} seconds")
        write_results_to_file(results, elapsed_time)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except (OSError, IOError, ValueError) as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
