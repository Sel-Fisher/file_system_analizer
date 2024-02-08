# File System Analysis Tool

This tool analyzes the file system structure and usage on a Linux system. It can be used to classify files into categories, calculate the total size for each file type category, identify large files, and generate a report of world-writable files.

## Usage

To use the tool, follow these steps:

1. **Install Python 3:** Ensure Python 3 is installed on your system. You can download it from the official Python website if it's not already installed.

2. **Place the Script:** Place the `file_system_analyzer.py` script in a directory that is included in your system's `PATH` or in a directory from where you intend to run the script.

3. **Make the Script Executable:** Open a terminal and navigate to the directory containing the script. Run the following command to make the script executable:
   ```bash
   chmod +x /path/to/script/directory/file_system_analyzer.py
   
4. **Add the Script to Your PATH: (Optional)** If you want to run the script from any directory, you need to add it to your `PATH`. Run the following command in the terminal:
    ```bash
    # If you use '.bashrc'
    echo 'export PATH="$PATH:/path/to/script/directory"' >> ~/.bashrc
    source ~/.bashrc 
   
    # If you use '.bash_profile'
    echo 'export PATH="$PATH:/path/to/script/directory"' >> ~/.bash_profile
    source ~/.bash_profile 
    ```
   Replace `/path/to/script/directory` with the actual path to the directory containing the `file_system_analyzer.py` script. This command will append the new `PATH` entry to the end of the `.bashrc` or `.bash_profile`  file and apply the changes to your current session.

5. **Run the Script:** Now you can run the script from any directory by simply typing its name followed by the required arguments:
   ```bash
   file_system_analyzer.py <directory> [--size_threshold <size>] [--show_world_writable]
   ```
   Replace <directory> with the path to the directory you want to analyze. Optionally, you can specify a size threshold for large files (in bytes) using the --size_threshold flag (short flag -s). If you want to see the list of world-writable files, use the --show_world_writable flag (short flag -w).

**Dependencies**

This tool has no external dependencies beyond Python 3. It should work out of the box with most Linux distributions.

**Functionality**

The tool performs the following tasks:

* Traverses through a specified directory recursively.

* Classifies files into categories based on their extensions or file signatures.

* Calculates and displays the total size for each file type category.

* Identifies and lists files above a certain size threshold.

* Generates a report of files with unusual permission settings (e.g., world-writable files).

**Error Handling**

The tool handles errors related to inaccessible directories and file access issues. It will print an error message and continue with the next file if it encounters a problem with a specific file.

**Contributing**

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the project's GitHub repository.

**License**

This tool is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you include the original copyright and license notice.

**Acknowledgments**

This tool was developed by Denis Komandyr as part of a coding exercise or project. If you have any questions or need further assistance, please contact deniskomandyr@gmail.com.
