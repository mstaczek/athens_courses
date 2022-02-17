import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_urls(path_to_txt):
    with open(path_to_txt) as urls_file:
        lines = urls_file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def download_htmls(urls, download_folder):
    driver_path = "GenerateCsv/chromedriver.exe"
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    for i, url in enumerate(urls):
        print(f"Link {i+1}: {url}")
        driver.get(url)
        try:
            WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.TAG_NAME,'app-course-show'), "20"))
        except Exception as e:
            print(f"Error downloading link {i+1}: {url}")
            print(f"Error: {e}")
            with open("bugged2.txt", 'a', encoding="utf-8") as f:
                f.write(url)
                f.write('\n')
        else:
            html_source = driver.page_source
            html_filename = url[54:-1]+".html"
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
    links_to_htmls(input_urls_txt="links_all.txt", output_htmls_folder="html_downloads_all")

