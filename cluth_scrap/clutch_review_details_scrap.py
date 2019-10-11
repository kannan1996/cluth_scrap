import requests
import csv
import time
import re
from bs4 import BeautifulSoup

company_csv = open('clutch_review_details_scrap.csv', 'w')
csvwriter = csv.writer(company_csv)

base_url = "https://clutch.co"

csvwriter.writerow(['Name', 'Positions', 'Company Name',
                    'Project Name', 'Project Type',
                    'Cost', 'Start Date'])


all_companies = base_url + "/directory/mobile-application-developers"

page = requests.get(all_companies)
soup = BeautifulSoup(page.content, 'html.parser')

'''Get the Total number of pages in the main directory
   (i.e,) from `all_companies` url '''
main_page_pagination = soup.find(
    class_="pager").find(class_="pager-current").get_text()
main_page_pagination_pattern = '(\d+) of (\d+)'
page_match = re.match(main_page_pagination_pattern, main_page_pagination)
app_page_count = int(page_match.group(2))

for dir_pge in range(app_page_count):
    directory_page_url = all_companies + "?page={}".format(dir_pge)
    directory_page = requests.get(directory_page_url)
    directory_page_content = BeautifulSoup(directory_page.content,
                                           'html.parser')

    if directory_page_content.find(class_="view-rows"):
        company_list = directory_page_content.find(
            class_="view-rows").find_all(class_="provider-row")
        for i in range(len(company_list)):
            profile_det = company_list[i].find(
                class_="provider-row-header").find(class_="company-name")
            review_base_url = base_url + profile_det.a['href']
            profile = profile_det.get_text().strip()
            print(review_base_url)

            review_base_page = requests.get(review_base_url)
            review_base_page_content = BeautifulSoup(
                review_base_page.content, 'html.parser'
            )
            review_base_page_pagination = review_base_page_content.find_all(
                "a", {"title": re.compile(r"Go to page \d")}
            )
            review_base_pagination_count = len(review_base_page_pagination) + 1
            review_count_text = company_list[i].find(
                class_="provider-row-header").find(
                class_="rating-reviews").find(
                class_="provider-profile-rating-widget"
            ).get_text()

            if len(review_count_text) > 0:
                for i in range(0, review_base_pagination_count):
                    review_page_url = review_base_url + '?page=0%2C{}'.format(i)
                    review_page = requests.get(review_page_url)
                    time.sleep(0.5)
                    review_page_content = BeautifulSoup(
                        review_page.content, 'html.parser'
                    )

                    row_provider = review_page_content.find_all(class_="views-row")

                    for i in range(len(row_provider)):
                        company_details_row = []

                        company_name_div = row_provider[i].find(
                            class_="reviewer-col").find(
                            class_="field-name-field-fdb-title")
                        company_data = company_name_div.find(
                            class_="field-item"
                        ).get_text() if company_name_div else ""

                        company_data_list = company_data.split(",")

                        if len(company_data_list) > 1:
                            position = company_data_list[0]
                            company_name = company_data_list[1]
                        elif len(company_data_list) == 1:
                            position = company_name = company_data_list[0]
                        elif len(company_data_list) == 0:
                            position = "None"
                            company_name = "None"

                        proj_name_div = row_provider[i].find(
                            class_="project-col").find(
                            class_="inner_url"
                        )
                        proj_name = proj_name_div.get_text() \
                            if proj_name_div else "None"

                        proj_type_div = row_provider[i].find(
                            class_="project-col").find(
                            class_="abs-aligned").find(
                            class_="field-name-field-fdb-project-type"
                        )
                        proj_type = proj_type_div.find(
                            class_="field-item even"
                        ).get_text() if proj_type_div else "None"

                        date_div = row_provider[i].find(
                            class_="project-col").find(
                            class_="abs-aligned").find(
                            class_="field-name-field-fdb-project-length"
                        )
                        date = date_div.find(
                            class_="field-item even").get_text() \
                            if date_div else "None"

                        cost_div = row_provider[i].find(
                            class_="project-col").find(
                            class_="abs-aligned").find(
                            class_="field-name-field-fdb-cost")
                        cost = cost_div.find(
                            class_="field-item even").get_text() \
                            if cost_div else "None"

                        company_details_row.append(profile.encode(
                            'ascii', 'ignore').decode('ascii')
                        )
                        company_details_row.append(position.encode(
                            'ascii', 'ignore').decode('ascii')
                        )
                        company_details_row.append(company_name.encode(
                            'ascii', 'ignore').decode('ascii')
                        )
                        company_details_row.append(proj_name.encode(
                            'ascii', 'ignore').decode('ascii')
                        )
                        company_details_row.append(proj_type.encode(
                            'ascii', 'ignore').decode('ascii')
                        )
                        company_details_row.append(cost.encode(
                            'ascii', 'ignore').decode('ascii')
                        )
                        company_details_row.append(date.encode(
                            'ascii', 'ignore').decode('ascii')
                        )

                        csvwriter.writerow(company_details_row)
    else:
        break

company_csv.close()
