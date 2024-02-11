
File Wiper
File Wiper is a Python script that securely overwrites files with either zeros or random bytes, ensuring that the original data cannot be recovered. This can be useful for securely deleting sensitive files before discarding or transferring storage media.

Features
Securely overwrite files with zeros or random bytes.
Progress reporting with a customizable progress bar.
Supports wiping individual files or entire directories recursively.
Getting Started
Prerequisites
Python 3.x
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/file-wiper.git
Navigate to the project directory:

bash
Copy code
cd file-wiper
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
To securely overwrite files with zeros, run the following command:

bash
Copy code
python file_wiper.py /path/to/directory
To overwrite files with random bytes, use the --random flag:

bash
Copy code
python file_wiper.py /path/to/directory --random
For more options and help, run:

bash
Copy code
python file_wiper.py --help
Example
Securely wipe all files in the current directory:

bash
Copy code
python file_wiper.py .
Notes
Use with caution as the wiped data will be irrecoverable.
Make sure to specify the correct directory path to avoid accidental data loss.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Inspired by the need for secure file deletion.
