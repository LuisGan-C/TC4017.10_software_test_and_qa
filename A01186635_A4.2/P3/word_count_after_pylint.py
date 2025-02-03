"""
Module: wordCount.py
This script reads a file containing words, identifies distinct words,
and calculates their frequencies. 
Results are printed to the console and saved to 'WordCountResults.txt'.

File after pylint
"""

import sys
import time

def read_words_from_file(filename):
    """Reads words from a file, handling invalid data."""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except (OSError, IOError) as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    return words

def count_word_frequencies(words):
    """Counts the frequency of each distinct word using a basic algorithm."""
    word_counts = {}
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def write_results_to_file(results, elapsed_time):
    """Writes word frequency results to an output file."""
    with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
        file.write(results + f"\nExecution Time: {elapsed_time:.4f} seconds\n")

def main():
    """Main function to handle file reading, word counting, and output."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()
    words = read_words_from_file(filename)

    if not words:
        print("Error: No valid words found in the file.")
        sys.exit(1)

    word_frequencies = count_word_frequencies(words)

    results = "Word Frequencies:\n"
    for word, count in sorted(word_frequencies.items()):
        results += f"{word}: {count}\n"
        print(f"{word}: {count}")

    elapsed_time = time.time() - start_time
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    write_results_to_file(results, elapsed_time)

if __name__ == "__main__":
    main()
