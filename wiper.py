# Author IC3-512

import os
import sys
import time
import concurrent.futures
from tqdm import tqdm


def overwrite_with_zeros(file_path: str) -> None:
    try:
        with open(file_path, "r+b") as f:
            size = os.path.getsize(file_path)
            f.write(b'\x00' * size)

    except Exception as e:
        print(f"Error overwriting file '{file_path}': {e}")


def list_files(directory: str) -> (list, int):
    file_list = []
    size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size += os.path.getsize(file_path)
            file_list.append(file_path)
    return file_list, size


def convert_size(size: int) -> str:
    if size > 1024 ** 4:
        return str(round(size / (1024 ** 4))) + "TB"
    elif size > 1024 ** 3:
        return str(round(size / (1024 ** 3))) + "GB"
    elif size > 1024 ** 2:
        return str(round(size / (1024 ** 2))) + "MB"
    elif size > 1024 ** 1:
        return str(round(size / (1024 ** 1))) + "KB"
    else:
        return str(size) + "B"


def print_banner() -> None:
    print("   ██╗    ██╗██╗██████╗ ███████╗██████╗\n "
          "  ██║    ██║██║██╔══██╗██╔════╝██╔══██╗ \n "
          "  ██║ █╗ ██║██║██████╔╝█████╗  ██████╔╝ \n "
          "  ██║███╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗ \n "
          "  ╚███╔███╔╝██║██║     ███████╗██║  ██║ \n "
          "   ╚══╝╚══╝ ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝\nSimple wiper - IC3-512  ")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_banner()
        start = time.time()
        files, total_size = list_files(directory=sys.argv[1])
        print(f"Space to wipe: {convert_size(total_size)}")
        with concurrent.futures.ProcessPoolExecutor(os.cpu_count()) as executor:
            with tqdm(total=len(files)) as pbar:

                futures = []
                for file in files:
                    future = executor.submit(overwrite_with_zeros, file)
                    futures.append(future)

                for future in concurrent.futures.as_completed(futures):
                    pbar.update(1)

        print(f"{round(time.time() - start, 2)} 's")
        print(f"{convert_size(int(total_size / (time.time() - start)))}/s")
    else:
        print("Usage: Drag and drop a file or folder onto this script to overwrite it with zeros.")
    input("Press Enter to exit.....")
