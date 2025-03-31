import sys  # Provides access to command-line arguments and system-specific parameters.
import random  # Enables generation of pseudo-random numbers.
import matplotlib.pyplot as plt  # Used for plotting graphs and histograms.
import math  # Provides access to mathematical functions.
random.seed(42)  # Set the seed for the random number generator to ensure reproducible results.

def plot_histogram(data, bin_size):
    """Plots a histogram of the given data.
    
    Parameters:
        data (list): The list of chord length samples to be plotted.
        bin_size (int): The number of bins to use in the histogram.
        
    The function creates a histogram showing the distribution of chord lengths,
    sets axis labels, adds a title, and displays gridlines for improved readability.
    """
    # Create a new figure with dimensions 8x5 inches.
    plt.figure(figsize=(8, 5))
    # Plot a histogram of 'data' with a specified number of bins, black edges for bars, 
    # and a slight transparency (alpha=0.7).
    plt.hist(data, bins=bin_size, edgecolor='black', alpha=0.7)
    # Label the x-axis as "Chord Length".
    plt.xlabel("Chord Length")
    # Label the y-axis as "Frequency".
    plt.ylabel("Frequency")
    # Set the title of the plot.
    plt.title("Chord Length Distribution")
    # Add a dashed grid on the y-axis for better visualization.
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    # Display the plot.
    plt.show()

def run_script():
    """Handles command-line input and processing.
    
    Usage:
        python script_name.py Mode N
        
    Parameters:
        Mode (int): Determines the method to generate chord lengths.
            Mode 0: Angle-based method.
            Mode 1: Radial distance method.
            Mode 2: Random points inside circle method (via transformation of uniform variable).
        N (int): The number of chord length samples to generate.
    
    For each method, the script calculates chord lengths in a unit circle and counts
    the fraction of chords whose length is at least sqrt(3). Additionally, the histogram 
    of the chord lengths is plotted.
    
    The methods correspond to different interpretations of the Bertrand Paradox, yielding 
    distinct probability density functions (PDFs) for the chord lengths:
    
    Mode 0: Angle-based method
      - Procedure:
          1. A random angle theta is drawn uniformly from [0, π].
          2. The chord length is computed as L = 2 * sin(theta).
    
    Mode 1: Radial distance method
      - Procedure:
          1. A distance r from the center is drawn uniformly from [0, 1].
          2. The chord is constructed such that its midpoint lies at distance r from the center.
          3. The chord length is computed as L = 2 * sqrt(1 - r^2).
    
    Mode 2: Random points inside circle method (via transformation)
      - Procedure:
          1. A uniform random number R is drawn from [0, 1].
          2. Set r = sqrt(R) so that the distribution of r has the PDF f_r(r) = 2r,
             which corresponds to choosing a random point uniformly inside the circle.
          3. The chord length is computed as L = 2 * sqrt(1 - r^2).
      - Derivation of PDF:
          Given (x,y) is uniform in the Area (x^2 + y^2 <= 1), f(x,y) = 1/π
          f(r,theta) = f(x,y)J(r,theta)
          f(r,theta) = (1/π)r
          f(r) = integration of f(r,theta) with respect to theta from 0 to 2π
          f(r) = 2r
          F(r) = R^2 --> F^(-1)(U) = sqrt(U)
    
    In all methods, the code also counts the number of chords with length at least sqrt(3)
    (a common threshold in Bertrand’s chord problem) and prints the fraction.
    """
    # Check for correct number of command-line arguments.
    if len(sys.argv) != 3:
        print("Usage: python script_name.py Mode N")
        sys.exit(1)

    # Parse the method (Mode) and number of samples (N) from the command line.
    Mode = int(sys.argv[1])
    N = int(sys.argv[2])

    # Validate that the Mode is one of the accepted values (0, 1, or 2).
    if Mode not in (0, 1, 2):
        print("Invalid Mode. Use 0, 1, or 2.")
        sys.exit(1)

    # Initialize a counter for chords with length >= sqrt(3).
    count = 0
    # List to store the generated chord lengths.
    chord_length_samples = []

    if Mode == 0:
        # Mode 0: Angle-based method.
        # For each sample, generate a random angle and compute chord length.
        for _ in range(N):
            # Generate a random angle theta uniformly distributed in [0, π].
            theta = math.pi * random.random()
            # Compute the chord length using L = 2 * sin(theta).
            length = 2 * math.sin(theta)
            chord_length_samples.append(length)
            # Increment the count if the chord length is at least sqrt(3).
            if length >= math.sqrt(3):
                count += 1

    elif Mode == 1:
        # Mode 1: Radial distance method.
        # In this method, the chord is determined by a random midpoint distance from the center.
        for _ in range(N):
            # Generate a random distance from the center (r) uniformly distributed in [0, 1].
            dist_from_center = random.random()
            # Compute the chord length using the geometry of a circle:
            # For a chord with midpoint at distance r from the center in a unit circle,
            # the half-length is sqrt(1 - r^2), so full chord length is 2 * sqrt(1 - r^2).
            length = 2 * math.sqrt(1 - (dist_from_center ** 2))
            chord_length_samples.append(length)
            if length >= math.sqrt(3):
                count += 1

    elif Mode == 2:
        # Mode 2: Random points inside circle method (using transformation of a uniform variable).
        # This method uses a transformation to ensure uniform distribution over the circle's area.
        for _ in range(N):
            # Draw a uniform random number R from [0, 1].
            R = random.uniform(0, 1)
            # Transform R to get a radius with PDF proportional to 2r:
            # Set the distance from the center r = sqrt(R).
            dist_from_center = math.sqrt(R)
            # Compute the chord length using L = 2 * sqrt(1 - r^2), derived from circle geometry.
            length = 2 * math.sqrt(1 - (dist_from_center ** 2))
            chord_length_samples.append(length)
            if length >= math.sqrt(3):
                count += 1

    # Compute and print the fraction of chords with length at least sqrt(3).
    print(f"Fraction of chords >= sqrt(3): {count / N:.4f}")

    # Determine an appropriate bin size for the histogram (here chosen as the integer square root of N).
    bin_size = int(math.sqrt(N))
    # Plot the histogram of chord lengths.
    plot_histogram(chord_length_samples, bin_size)

# Directly call run_script() when the script is run.
run_script()
