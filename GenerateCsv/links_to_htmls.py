import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH_PREFIX = "GenerateCsv/"

def get_urls(path_to_txt):
    with open(path_to_txt) as urls_file:
        lines = urls_file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def download_htmls(urls, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    driver_path = PATH_PREFIX + "chromedriver.exe"
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    for i, url in enumerate(urls):
        print(f"Link {i+1}: {url}")
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME,'app-course-show'), "20"))
        except Exception as e:
            print(f"Error downloading link {i+1}: {url}")
            print(f"Error: {e}")
            with open(PATH_PREFIX + "failed_to_download.txt", 'a', encoding="utf-8") as f:
                f.write(url)
                f.write('\n')
        else:
            html_source = driver.page_source
            html_filename = url[54:]+".html"
            path_to_html = os.path.join(download_folder,html_filename)
            with open(path_to_html, 'w', encoding="utf-8") as f:
                f.write(html_source)
    driver.quit()
    return

def links_to_htmls(input_urls_txt, output_htmls_folder):
    print("Reading links")
    urls = get_urls(path_to_txt=input_urls_txt)
    print(f"Found {len(urls)} links...")
    print("Starting downloading every link...")
    download_htmls(urls, download_folder=output_htmls_folder)
    print("Downloading finished!")

if __name__ == '__main__':
    input_path = PATH_PREFIX + "links_2022_1.txt"
    output_path = PATH_PREFIX + "html_downloads_2022_1"
    links_to_htmls(input_urls_txt=input_path, output_htmls_folder=output_path)

