# Simple Wiper

Simple Wiper is a Python script designed to securely erase files by overwriting them with zeros. This tool can be useful for ensuring that sensitive files are irrecoverably deleted.

## Features

- Overwrites files with zeros to securely erase them.
- Supports wiping of individual files or entire directories.
- Utilizes multiple processes for concurrent wiping to improve performance.

## Getting Started

To use Simple Wiper, follow these steps:

1. Clone the repository to your local machine:
   
	git clone https://github.com/IC3-512/wiper.git

2. Navigate to the project directory:

	cd simple-wiper

3. Run the script and specify the file or directory you want to wipe:

	python simple_wiper.py /path/to/file_or_directory



## Requirements

Python 3.x
tqdm library (install via pip: pip install tqdm)

## Usage

python simple_wiper.py /path/to/file_or_directory

Replace /path/to/file_or_directory with the path to the file or directory you want to wipe.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
