# xl_grapher

**xl_grapher** is a command line tool for quickly analyzing and graphing data from Excel files, using the **numpy**, **pandas**, and **matplotlib** libraries.

## Installation

Before running the script, make sure you have Python 3.x installed on your system. To set up the required environment, follow these steps:

### 1. Clone the Repository

Clone or download this repository to your local machine:

```bash
git clone https://github.com/yourusername/xl_grapher.git
```

### 2. Create a Virtual Environment

Navigate to the cloned repository, create a virtual environment, and activate it:

```bash
cd xl_grapher
python -m venv venv
# activate venv in Linux
source venv/bin/activate
# activate venv in Windows
venv\Scripts\activate
```

### 2. Install Dependencies

Install the required libraries using pip from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 3. Run the Script

You can now run the script:

```bash
python xl_grapher.py
```

## Usage

The script provides various commands for analysis and graphing, to be entered after the script is run:

help: List available functions and commands.  
end: Exit the program.  
data: Display the current data from the Excel file.  
graph: Create a scatter plot of two columns from the Excel file.  
histo: Create a histogram of a column from the Excel file (functionality not yet implemented).  
mean: Calculate and display the mean of a specified column.  
std: Calculate and display the population standard deviation of a specified column.  
sem: Calculate and display the standard error of the mean (SEM) of a specified column.  
median: Calculate and display the median of a specified column.  
mode: Display the mode of a specified column (functionality not yet implemented).  

For example, to create a scatter plot using columns 'a' and 'b', enter `graph 'a', 'a'`.  

## Contributions

Contributions and feeback are welcome! If you have ideas for additional commands or other improvements, feel free to create issues or pull requests. Otherwise, I will be adding functionality to the script as I find useful.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
