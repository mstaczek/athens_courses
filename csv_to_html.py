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


def csv_to_html3(input_csv_path, output_html_path):
    print("Creating pretty html webpage from csv ;)")
    loader = jinja2.FileSystemLoader('jinja2templates/')
    env = jinja2.Environment(loader=loader)
    template = env.get_template('jinja2template3.html')
    input_df = pd.read_csv(input_csv_path, na_filter=False)
    params = {}
    params['courses_data'] = input_df
    params['colname_for_title'] = 'What'
    params['colname_for_subtitle'] = ['How','Code']
    params['colnames_for_card_body'] = ['Where','Prerequisites','Objectives','Programme','Exam']
    params['colname_for_link'] = 'Link'
    params['colnames_for_card_desc'] = ['Min. year','Language','How','Might be online?','Tags','Professor','Other professors','Address','When','Code']
    params['js_dict'] = input_df.to_dict(orient='records')
    params['colnames_dropdown_filters'] = ['When']
    params['colnames_checkbox_filters'] = ['Language','How','Might be online?','Min. year','Where']
    params['columns_sort_by'] = ['What','Code','Min. year']
    output = template.render(params)
    with open(output_html_path, "w", encoding='utf-8') as fh:
        fh.write(output)
    print("New html webpage is in " + output_html_path)

if __name__ == '__main__':
    # csv_to_html(input_csv_path='results_2022_1.csv', output_html_path='results_2022_1.html')
    csv_to_html3(input_csv_path='results_2022_1.csv', output_html_path='results_2022_1_new.html')
    