import os
import bs4
import pandas as pd


def clean_values(value):
    return value.replace('\xa0','').replace('\n',' ').replace(' ','').strip()

def extract_data_from_html(html_file, course_no):
    soup = bs4.BeautifulSoup(html_file, features="html.parser")
    results_pairs = []

    results = soup.findAll("div", {"_ngcontent-c2": "", "class": "row p-1"})
    for result in results:
        results_pairs += [([child.get_text(strip=True) for child in result.findChildren("div", recursive=False)])]
    results_pairs = [pair for pair in results_pairs if len(pair) == 2]
    colnames = [pair[0] for pair in results_pairs] + ["Link"]
    values = [[clean_values(pair[1]) for pair in results_pairs]+\
              [f"https://register.athensnetwork.eu/courses/course-show/{course_no}"]]
    return pd.DataFrame(values,columns=colnames)

def clean_df_befor_saving(df):
    new_colnames = {'Unnamed: 0': 'No.',
                    'Session:': 'When',
                    'Institution:': 'Where',
                    'Course takes place:': 'How',
                    'Course title:': 'What',
                    'Course code:': 'Code',
                    'Minimum year of study:': 'Min. year',
                    'Language of tutition:': 'Language',
                    'Prerequisites:': 'Prerequisites',
                    'Objectives:': 'Objectives',
                    'Course exam:': 'Exam',
                    'Programme to be followed:': 'Programme',
                    "Professor responsible:": 'Professor',
                    "Participating professors:": 'Other professors',
                    "Course address:": 'Address',
                    "Categories:": 'Tags',
                    "Will switch to 'online' if necessary:": 'Might be online?'}
    output_order = [
        'No.',
        'Where',
        'What',
        'Prerequisites',
        'Objectives',
        'Programme',
        'Exam',
        'How',
        'Language',
        'Min. year',
        'Professor',
        'Other professors',
        'Address',
        'Tags',
        'Might be online?',
        'When',
        'Code',
        'Link']

    new_df = df.fillna(" ", inplace=False)
    new_df = new_df.reset_index()
    new_df.rename(new_colnames, axis=1, inplace=True)
    new_df["No."] = new_df.index + 1
    new_df = new_df.drop(['index', 'Course location:'], axis=1)
    new_df.loc[new_df.loc[:, "How"] != 'on-site', ["Might be online?"]] = "Yes"
    new_df = new_df[output_order].fillna('')
    return new_df

def htmls_to_csv(input_htmls_folder,output_csv_path):
    print("Starting data extraction from htmls...")
    htmls_paths = [f for f in os.listdir(input_htmls_folder)]
    dfs_list = []
    for file in htmls_paths:
        with open(os.path.join(input_htmls_folder, file), encoding="utf-8") as html_file:
            dfs_list += [extract_data_from_html(html_file, course_no=os.path.splitext(file)[0])]
    df = pd.concat(dfs_list)
    df = clean_df_befor_saving(df)
    df.to_csv(output_csv_path, index=False)
    print("Finished htmls to csv conversion.")

if __name__ == '__main__':
    htmls_to_csv(input_htmls_folder="html_downloads_2022_1", output_csv_path="results_2022_1.csv")

