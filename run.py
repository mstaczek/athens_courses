from links_to_htmls import links_to_htmls
from htmls_to_csv import htmls_to_csv
from csv_to_html import csv_to_html_web


def create_html_webpage_from_links(links, htmls, csv, result):
    links_to_htmls(input_urls_txt=links, output_htmls_folder=htmls)
    htmls_to_csv(input_htmls_folder=htmls, output_csv_path=csv)
    csv_to_html_web(input_csv_path=csv, output_html_path=result)


if __name__ == '__main__':
    links = "links_2022_1.txt"
    htmls = "html_downloads_2022_1"
    csv = "results_2022_1.csv"
    result = "results_2022_1_web.html"
    create_html_webpage_from_links(links, htmls, csv, result)
