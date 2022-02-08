import shutil
import os

def main():
    shutil.copyfile("results_2022_1.html", os.path.join("docs", "index.html"))


if __name__ == '__main__':
    main()
