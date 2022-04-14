import os
import sys


def main(dir):
    print("Working directory: " + dir)
    counter = 10  # For debuging
    for root, subdirs, files in os.walk(dir):
        print('--\nroot = ' + root)
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)
        for filename in files:
            file_path = os.path.join(root, filename)
            print('\t- file %s (full path: %s)' % (filename, file_path))
        counter -= 1
        if counter == 0:
            return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the working directory")
    else:
        working_dir = sys.argv[1]
        if working_dir == None or len(working_dir) == 0:
            print("Please specify the working directory")
        else:
            main(working_dir)
