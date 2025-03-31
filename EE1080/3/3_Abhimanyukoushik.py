import sys  # Provides access to command-line arguments and system-related functions.
import random  # Enables the generation of pseudo-random numbers.
import matplotlib.pyplot as plt  # Used for creating visualizations like bar plots.
import math  # Provides access to mathematical functions, though it's not explicitly used here.
random.seed(42)  # Set the seed for the random number generator to ensure reproducible results.

def plot_frequency(data):
    """Plots a relative frequency plot of the given data, including zero-frequency elements."""
    
    # Manually count occurrences of each unique value in 'data'.
    value_counts = {}
    total = len(data)  # Total number of data points.

    # Iterate through each value in the data and update the count in 'value_counts'.
    for val in data:
        if val in value_counts:
            value_counts[val] += 1
        else:
            value_counts[val] = 1

    # Identify the smallest and largest values observed in the data.
    min_val = min(value_counts.keys())
    max_val = max(value_counts.keys())

    # Generate a list of all integer values from min_val to max_val.
    values = list(range(min_val, max_val + 1))

    # Build a corresponding list of frequencies, ensuring missing values are given a frequency of 0.
    frequencies = [(value_counts[val]) if val in value_counts else 0 for val in values]

    # Create a new figure with specified size (width: 10 inches, height: 6 inches).
    plt.figure(figsize=(10, 6))
    # Plot a bar chart: 
    #   - x-coordinates from 'values', 
    #   - heights from 'frequencies'.
    #   - 'width' controls the bar width, 
    #   - 'color' sets bar color, 
    #   - 'edgecolor' defines bar borders, 
    #   - 'alpha' sets bar transparency.
    plt.bar(values, frequencies, width=0.8, color='skyblue', edgecolor='black', alpha=0.7)

    # Label the axes and title.
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Frequency Plot")

    # Display a grid on the y-axis with dashed lines and partial transparency.
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    # Render the plot.
    plt.show()

def run_script():
    """Handles command-line input and processing.
    
    This script expects three command-line arguments:
      1. n: An integer representing the size of the set from which subsets are chosen.
      2. k: The number of elements to choose in each subset.
      3. N: The number of samples (subsets) to generate.
    
    Usage:
        python 2_name_of_file.py n k N
    """
    # Check that the script received exactly three arguments besides the script name.
    if len(sys.argv) != 4:
        print("Usage: python 2_name_of_file.py n k N")
        sys.exit(1)

    # Convert the command-line arguments to integers.
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    N = int(sys.argv[3])

    # Generate a 2D list U of size n x N, where each element is a random float in [0, 1).
    U = [[random.random() for _ in range(N)] for _ in range(n)]
    # Create a corresponding 2D list I of the same dimensions, initialized to 0.
    I = [[0 for _ in range(N)] for _ in range(n)]

    # For each of the N samples (columns):
    for j in range(N):
        # Decide whether the first element I[0][j] is 1 or 0 based on comparing U[0][j] to k/n.
        I[0][j] = 1 if U[0][j] <= k/n else 0
        
        # Initialize a running sum of previously assigned indicators to track how many have been chosen so far.
        sumofIij = 0
        for i in range(0, n - 1):
            # Accumulate the indicator value of the current row i.
            sumofIij += I[i][j]
            # For the next row (i+1), decide if it should be 1 or 0 by comparing U[i+1][j] 
            # to the ratio (k - sumofIij)/(n - (i+1)).
            I[i+1][j] = 1 if U[i+1][j] <= (k - sumofIij)/(n - (i+1)) else 0
    
    # Convert each subset (represented by a column of I) into a decimal number.
    # Specifically, interpret the binary digits in each column as bits of a binary number.
    decimalSubset = [0 for _ in range(N)]
    for i in range(n):
        for j in range(N):
            # If I[i][j] == 1, add 2^i to decimalSubset[j].
            decimalSubset[j] += I[i][j] * (2 ** i)

    # Plot the frequency of each resulting decimal representation.
    plot_frequency(decimalSubset)

# Directly call run_script() to execute the script when the file is run.
run_script()
