import pandas as pd
import jinja2

def csv_to_html(input_csv_path, output_html_path):
    print("Creating pretty html table from csv ;)")
    loader = jinja2.FileSystemLoader('jinja2template.html')
    env = jinja2.Environment(loader=loader)
    template = env.get_template('')
    input_df = pd.read_csv(input_csv_path, na_filter=False)
    output = template.render(df=input_df)
    with open(output_html_path, "w", encoding='utf-8') as fh:
        fh.write(output)
    print("New html table is in " + output_html_path)

def csv_to_html2(input_csv_path, output_html_path):
    print("Creating pretty html webpage from csv ;)")
    loader = jinja2.FileSystemLoader('jinja2template2.html')
    env = jinja2.Environment(loader=loader)
    template = env.get_template('')
    input_df = pd.read_csv(input_csv_path, na_filter=False)
    card_titles = input_df['What']
    card_descriptions = input_df[['Prerequisites','Objectives','Programme','Exam']]
    course_links = input_df['Link']
    card_descriptions_details = input_df[['Professor','Other professors','Address','Tags','Might be online?','When','Code']]
    params = {'df':input_df, 'year':2022, 'card_titles':card_titles, 'card_descriptions':card_descriptions, 'card_descriptions_details':card_descriptions_details, 'course_links':course_links} 
    output = template.render(params)
    with open(output_html_path, "w", encoding='utf-8') as fh:
        fh.write(output)
    print("New html webpage is in " + output_html_path)

if __name__ == '__main__':
    # csv_to_html(input_csv_path='results_2022_1.csv', output_html_path='results_2022_1.html')
    csv_to_html2(input_csv_path='results_2022_1.csv', output_html_path='results_2022_1_new.html')
    