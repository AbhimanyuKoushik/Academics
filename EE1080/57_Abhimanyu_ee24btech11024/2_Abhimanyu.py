import csv  # Import the CSV module to enable reading from and writing to CSV files.
import math  # Import the math module to perform mathematical operations like logarithms and square roots.
import sys  # Import the sys module to interact with the interpreter and handle command-line arguments.
import matplotlib.pyplot as plt  # Import matplotlib's pyplot module to create visualizations like histograms.

# -------------------------------------------------------------------------------------------------
# Function: plot_histogram
# Purpose: To display a histogram visualization of a list of numerical data.
# Additional Details:
#   - The function leverages matplotlib to create a figure and display the histogram.
#   - The bin_size parameter controls the granularity of the histogram.
#   - This function is useful for getting a visual understanding of data distribution.
# -------------------------------------------------------------------------------------------------
def plot_histogram(data, bin_size):
    """Plots a histogram of the given data.
    
    Parameters:
        data (list): The list of numerical values to be visualized.
        bin_size (int): The number of bins to be used in the histogram.
    """
    # Create a new figure with a specified size (width: 8 inches, height: 5 inches).
    plt.figure(figsize=(8, 5))
    # Plot a histogram of the data with the given number of bins.
    # 'edgecolor' defines the color of the bin borders.
    # 'alpha' sets the transparency level for the histogram bars.
    plt.hist(data, bins=bin_size, edgecolor='black', alpha=0.7)
    # Set the label for the x-axis.
    plt.xlabel("Value")
    # Set the label for the y-axis.
    plt.ylabel("Frequency")
    # Set the title of the histogram.
    plt.title("Histogram")
    # Enable grid lines for the y-axis with dashed style and a specified transparency.
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    # Display the histogram on the screen.
    plt.show()

# -------------------------------------------------------------------------------------------------
# Function: is_number
# Purpose: To determine whether a given string can be converted to a float.
# Additional Details:
#   - This helper function is critical for filtering out non-numeric data when reading CSV files.
#   - The try-except block is used to handle potential conversion errors gracefully.
# -------------------------------------------------------------------------------------------------
def is_number(value):
    """Check if a string can be converted to a float.
    
    Parameters:
        value (str): The string to be checked.
    
    Returns:
        bool: True if the string can be converted to a float, otherwise False.
    """
    try:
        # Attempt to convert the value to a float.
        float(value)
        return True  # Return True if the conversion is successful.
    except ValueError:
        # If a ValueError occurs, the value cannot be converted to a float.
        return False

# -------------------------------------------------------------------------------------------------
# Function: read_csv
# Purpose: To extract and convert numerical data from a CSV file.
# Additional Details:
#   - The function reads each row from the file, processes each cell, and filters for numeric values.
#   - This function is robust to CSV files containing mixed data types, as it checks each element.
# -------------------------------------------------------------------------------------------------
def read_csv(filename):
    """Reads numeric data from a CSV file.
    
    Parameters:
        filename (str): The path to the CSV file.
    
    Returns:
        list: A list of floating-point numbers read from the file.
    """
    data = []  # Initialize an empty list to store numeric data.
    # Open the CSV file in read mode with newline handling.
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)  # Create a CSV reader object.
        # Iterate over each row in the CSV file.
        for row in reader:
            # Iterate over each item in the current row.
            for x in row:
                # Check if the current item can be converted to a float.
                if is_number(x):
                    # Convert the item to float and append it to the data list.
                    data.append(float(x))
    return data  # Return the list of numeric data.

# -------------------------------------------------------------------------------------------------
# Function: write_csv
# Purpose: To output a list of numerical values into a CSV file.
# Additional Details:
#   - Each number is written as a row in the output CSV.
#   - The function ensures that the file is written with proper newline handling to avoid extra blank lines.
# -------------------------------------------------------------------------------------------------
def write_csv(filename, data):
    """Writes numeric data to a CSV file.
    
    Parameters:
        filename (str): The name of the CSV file to write to.
        data (list): The list of numeric values to be written.
    """
    # Open the CSV file in write mode with newline handling.
    with open(filename, mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer object.
        # Iterate over each value in the data list.
        for value in data:
            # Write the value as a single-element row in the CSV file.
            writer.writerow([value])
    # Print a confirmation message after successfully writing the file.
    print(f"Data successfully written to {filename}")

# -------------------------------------------------------------------------------------------------
# Function: process_bernoulli
# Purpose: To transform raw numerical data into Bernoulli distributed data.
# Additional Details:
#   - A Bernoulli trial results in 1 (success) or 0 (failure) based on a probability threshold.
#   - The parameter provided is the threshold; if the data value is less than or equal to it,
#     the result is considered a success.
#   - The function calculates and prints the mean of the generated Bernoulli samples.
# -------------------------------------------------------------------------------------------------
def process_bernoulli(data, parameter):
    """Processes data for Bernoulli distribution.
    
    This function transforms the input data into Bernoulli samples.
    For each element in the data, if the element is less than or equal to the parameter,
    it is considered a success (represented by 1); otherwise, it's a failure (represented by 0).
    
    Parameters:
        data (list): The list of numerical values.
        parameter (float): The probability threshold to determine success.
    
    Returns:
        list: A list of Bernoulli samples (1s and 0s).
    """
    # Create a new list using list comprehension:
    # For each value in data, assign 1 if the value is less than or equal to 'parameter', else assign 0.
    bernoulli_samples = [1 if x <= parameter else 0 for x in data]
    # Calculate the mean of the Bernoulli samples.
    mean = sum(bernoulli_samples) / len(bernoulli_samples)
    # Print the mean value formatted to four decimal places.
    print(f"Mean: {mean:.4f}")
    return bernoulli_samples  # Return the list of Bernoulli samples.

# -------------------------------------------------------------------------------------------------
# Function: process_exponential
# Purpose: To generate samples following an exponential distribution from uniformly distributed data.
# Additional Details:
#   - The function uses the inverse transform sampling method.
#   - For a given uniform random variable x, the transformation is -ln(1 - x) / parameter.
#   - A special condition is used to handle the rare case when x is equal to 1.
#   - The mean of the resulting exponential samples is computed and printed.
# -------------------------------------------------------------------------------------------------
def process_exponential(data, parameter):
    """Processes data for Exponential distribution.
    
    This function applies an exponential transformation to the input data.
    It uses the inverse transform sampling method to generate samples from an exponential distribution.
    The transformation is given by: -ln(1 - x) / parameter, with a correction if x is equal to 1.
    
    Parameters:
        data (list): The list of numerical values.
        parameter (float): The rate parameter (lambda) for the exponential distribution.
    
    Returns:
        list: A list of transformed values following an exponential distribution.
    """
    # Use list comprehension to transform each value in the data list:
    # If x is less than 1, use the standard formula.
    # Is sample is 1 then it means x is going to infinity, it anyway has a very less chance, we will ignore it
    exp_samples = [-(math.log(1 - x) / parameter) if x < 1 else 0 for x in data]
    # If x is 1 (or very close to 1), subtract a very small number to avoid math domain error.
    #exp_samples = [-(math.log(1 - x) / parameter) if x < 1 else -(math.log(1 - (x - 5.6e-17)) / parameter) for x in data]
    # Calculate the mean of the Exponential samples.
    mean = sum(exp_samples) / len(exp_samples)
    # Print the mean value formatted to four decimal places.
    print(f"Mean: {mean:.4f}")
    return exp_samples  # Return the list of exponentially transformed samples.

# -------------------------------------------------------------------------------------------------
# Function: process_cdfx
# Purpose: To perform a piecewise transformation of data based on cumulative distribution function (CDF) logic.
# Additional Details:
#   - The function applies different transformations based on thresholds (1/3 and 2/3) of the input value.
#   - It is designed to simulate a specific distribution shape as defined by the piecewise function.
#   - Additionally, it counts and prints the number of times the transformed value equals 2.
# -------------------------------------------------------------------------------------------------
def process_cdfx(data):
    """Processes data for CDF transformation.
    
    This function transforms the input data according to a piecewise function.
    The transformation is defined as follows:
        - If x <= 1/3, then the transformed value is sqrt(3*x).
        - If 1/3 < x <= 2/3, then the transformed value is 2.
        - If x > 2/3, then the transformed value is 6*x - 2.
    
    Additionally, it counts the number of times the transformed value equals 2.
    
    Parameters:
        data (list): The list of numerical values.
    
    Returns:
        list: A list of values after the CDF transformation.
    """
    # Apply the piecewise transformation using list comprehension.
    cdfx_samples = [math.sqrt(3*x) if x <= 1/3 else 2 if x <= 2/3 else 6*x - 2 for x in data]
    # Count how many times the value 2 appears in the transformed data.
    counts2 = sum(1 for x in cdfx_samples if x == 2)  # Count occurrences of '2'
    # Print the count of occurrences of the value 2.
    print(f"Number of 2s in samples of X is {counts2}")
    return cdfx_samples  # Return the list of transformed values.

# -------------------------------------------------------------------------------------------------
# Function: run_script
# Purpose: To manage the overall workflow of the script including parsing arguments, processing data,
#          plotting results, and writing outputs.
# Additional Details:
#   - The function validates command-line arguments and selects the processing mode.
#   - It reads input data from a CSV file, applies the chosen processing method, and optionally plots a histogram.
#   - The processed data is then saved to an output CSV file.
#   - The mode determines which statistical transformation is applied:
#       Mode 0: Bernoulli processing (requires a parameter).
#       Mode 1: Exponential processing (requires a parameter) and histogram plotting.
#       Mode 2: CDF transformation processing and histogram plotting.
# -------------------------------------------------------------------------------------------------
def run_script():
    """Handles command-line input and processing.
    
    This function parses command-line arguments, reads input data from a CSV file,
    processes the data based on the specified mode, optionally plots a histogram,
    and writes the processed data to an output CSV file.
    
    Modes:
        0 - Process data using the Bernoulli distribution (parameter required).
        1 - Process data using the Exponential distribution (parameter required) and plot a histogram.
        2 - Process data using a CDF transformation and plot a histogram.
    
    Usage:
        python 2_name_of_file.py Mode input_filename [parameter]
    """
    # Check if the correct number of command-line arguments has been provided.
    if len(sys.argv) not in [3, 4]:
        # Print usage instructions if the arguments are incorrect.
        print("Usage: python 2_name_of_file.py Mode input_filename [parameter]")
        # Exit the program with an error code.
        sys.exit(1)

    # Parse the mode from the first command-line argument and convert it to an integer.
    mode = int(sys.argv[1])
    # Parse the input filename from the second command-line argument.
    input_filename = sys.argv[2]
    # If a parameter is provided (i.e., 4 arguments), convert it to a float; otherwise, set it to None.
    parameter = float(sys.argv[3]) if len(sys.argv) == 4 else None

    # Read numeric data from the specified CSV file.
    data = read_csv(input_filename)

    # Process the data based on the specified mode.
    if mode == 0:
        # Mode 0: Bernoulli processing.
        if parameter is None:
            # If the parameter is missing, print an error message and exit.
            print("Error: Parameter required for Mode 0.")
            sys.exit(1)
        # Create a parameter string for the output filename.
        fracstring = int((parameter - math.floor(parameter)) * 100)
        intstring = math.floor(parameter)
        # The string represents the integer and fractional parts of the parameter.
        param_str = (f"{intstring}p" if (intstring != 0 and fracstring <= 1e-12)
                    else f"{intstring}p{fracstring}" if (intstring != 0 and int(10 * int(fracstring/10) - fracstring) != 0)
                    else f"{intstring}p{int(fracstring/10)}" if (intstring != 0 and int(10 * int(fracstring/10) - fracstring) == 0)
                    else f"p{fracstring}" if (intstring == 0 and fracstring != 0) 
                    else f"p")
        # Construct the output filename using the parameter value multiplied by 100.
        output_filename = f"Bernoulli_{param_str}.csv"
        # Process the data using the Bernoulli distribution.
        result = process_bernoulli(data, parameter)

    elif mode == 1:
        # Mode 1: Exponential processing.
        if parameter is None:
            # If the parameter is missing, print an error message and exit.
            print("Error: Parameter required for Mode 1.")
            sys.exit(1)
        # Create a parameter string for the output filename.
        fracstring = int((parameter - math.floor(parameter)) * 100)
        intstring = math.floor(parameter)
        # The string represents the integer and fractional parts of the parameter.
        param_str = (f"{intstring}p" if (intstring != 0 and fracstring <= 1e-12)
                    else f"{intstring}p{fracstring}" if (intstring != 0 and int(10 * int(fracstring/10) - fracstring) != 0)
                    else f"{intstring}p{int(fracstring/10)}" if (intstring != 0 and int(10 * int(fracstring/10) - fracstring) == 0)
                    else f"p{fracstring}" if (intstring == 0 and fracstring != 0) 
                    else f"p")
        # Construct the output filename using the parameter string.
        output_filename = f"Exponential_{param_str}.csv"
        # Process the data using the Exponential transformation.
        result = process_exponential(data, parameter)
        # Plot a histogram of the processed data.
        # The number of bins is determined by the integer square root of the number of data points.
        plot_histogram(result, int(math.sqrt(len(result))))

    elif mode == 2:
        # Mode 2: CDF transformation processing.
        output_filename = "CDFX.csv"  # Set a fixed output filename for CDF transformation.
        # Process the data using the CDF transformation.
        result = process_cdfx(data)
        # Plot a histogram of the processed data.
        plot_histogram(result, int(math.sqrt(len(result))))

    else:
        # If an invalid mode is provided, print an error message and exit.
        print("Invalid Mode! Program terminated.")
        sys.exit(1)

    # Write the processed result data to the output CSV file.
    write_csv(output_filename, result)

# -------------------------------------------------------------------------------------------------
# Script Execution:
# The following line ensures that when the script is run directly from the command line,
# the run_script function is invoked to carry out the data processing workflow.
# -------------------------------------------------------------------------------------------------
run_script()
