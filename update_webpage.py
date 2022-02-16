import shutil
import os

def main():
    shutil.copyfile("results_2022_1_web.html", os.path.join("docs", "index.html"))
    shutil.copyfile("results_2022_1_table.html", os.path.join("docs", "table.html"))


if __name__ == '__main__':
    main()
