import os
import sys

def main(dir):
    print(dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the working directory")
    else:
        working_dir = sys.argv[1]
        if working_dir == None or len(working_dir) == 0:
            print("Please specify the working directory")
        else:
            main(working_dir)
