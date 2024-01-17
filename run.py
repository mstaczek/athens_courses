from GenerateCsv.links_to_htmls import links_to_htmls
from GenerateCsv.htmls_to_csv import htmls_to_csv
from GenerateWebpage.csv_to_html import csv_to_html_web, csv_to_html_table


def create_html_webpage_from_links(links, htmls, csv, result, result_table):
    links_to_htmls(input_urls_txt=links, output_htmls_folder=htmls)
    htmls_to_csv(input_htmls_folder=htmls, output_csv_path=csv)
    csv_to_html_web(input_csv_path=csv, output_html_path=result)
    csv_to_html_table(input_csv_path=csv, output_html_path=result_table)


if __name__ == '__main__':
    year = 2024
    session_no_this_year = 1
    links = f"GenerateCsv/links_{year}_{session_no_this_year}.txt"
    htmls = f"GenerateCsv/html_downloads_{year}_{session_no_this_year}"
    csv = f"results_{year}_{session_no_this_year}.csv"
    result = f"results_{year}_{session_no_this_year}_web.html"
    result_table = f"results_{year}_{session_no_this_year}_table.html"
    create_html_webpage_from_links(links, htmls, csv, result, result_table)
