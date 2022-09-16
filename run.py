from GenerateCsv.links_to_htmls import links_to_htmls
from GenerateCsv.htmls_to_csv import htmls_to_csv
from GenerateWebpage.csv_to_html import csv_to_html_web, csv_to_html_table


def create_html_webpage_from_links(links, htmls, csv, result, result_table):
    links_to_htmls(input_urls_txt=links, output_htmls_folder=htmls)
    htmls_to_csv(input_htmls_folder=htmls, output_csv_path=csv)
    csv_to_html_web(input_csv_path=csv, output_html_path=result)
    csv_to_html_table(input_csv_path=csv, output_html_path=result_table)


if __name__ == '__main__':
    links = "GenerateCsv/links_2022_2.txt"
    htmls = "GenerateCsv/html_downloads_2022_2"
    csv = "results_2022_2.csv"
    result = "results_2022_2_web.html"
    result_table = "results_2022_2_table.html"
    create_html_webpage_from_links(links, htmls, csv, result, result_table)
