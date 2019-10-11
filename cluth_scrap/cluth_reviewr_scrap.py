import requests
import csv, json
import time
from bs4 import BeautifulSoup
import pandas as pd 

df = pd.read_csv('cluth_app_developers.csv')

profile = df['Profile']

reviewer_csv = open('reviewer_app_developer.csv', 'w')
csvwriter = csv.writer(reviewer_csv)

csvwriter.writerow(['Project_Name','Project_Category','Project_Cost','Project_Length','Project_Summary','Reviewer_Name','Reviewer_Role','Industry_Type','Reviewer_Company_Size','Reviewer_Location'])

for i in profile:
	page_url = i #'https://clutch.co/profile/apriorit#reviews'
	print "reveiwer detail--->", page_url
	page = requests.get(page_url)
	time.sleep(0.5)
	soup = BeautifulSoup(page.content, 'html.parser')
	row_provider = soup.find(class_="view-content main-row")

	try:
		review_count = soup.find(class_ ="reviews-count").find('a').get_text()
	except:
		continue
	str_review_count = review_count.split(' ')[0]
	rev_count = int(str_review_count)
	print "review count--->", review_count
	rev_list = range(0,rev_count)

	total_classes = ['views-row views-row-1 views-row-odd views-row-first','views-row views-row-2 views-row-even','views-row views-row-3 views-row-odd','views-row views-row-4 views-row-even','views-row views-row-5 views-row-odd','views-row views-row-6 views-row-even','views-row views-row-7 views-row-odd','views-row views-row-8 views-row-even','views-row views-row-9 views-row-odd','views-row views-row-10 views-row-even views-row-last']

	for index,iCal in enumerate(total_classes):
		reviewer_list = []
		try:
			if index == rev_count-1 and index != 9:
				iCal = iCal+' views-row-last'
			# menu_review = row_provider.find('div',attrs={'class':iCal}).find('div', attrs={'class':'node node-feedback node-teaser client-interview clearfix'})
			menu_review = row_provider.find('div',attrs={'class':iCal}).find('div', attrs={'property':'review'})

			project_tree = menu_review.find('div',attrs={'class':'col-30 project-col'})
			reviewer_tree = menu_review.find('div', attrs={'class': 'review-mobile-cp hideon_active'}).find('div',attrs={'class':'col-24 reviewer-col'})

			try:
				project = project_tree.find('h2').find('a').get_text()
			except:
				project = 'None'

			try:
				project_category = project_tree.find('div', attrs={'class':'hidden-xs abs-aligned'}).find('div', attrs={'class':'field field-name-field-fdb-project-type field-type-taxonomy-term-reference field-label-hidden field-label-inline clearfix'}).find('div',attrs={'class':'field-item even'}).get_text()
			except:
				project_category = 'None'

			try:
				project_cost = project_tree.find('div', attrs={'class':'hidden-xs abs-aligned'}).find('div', attrs={'class':'field field-name-field-fdb-cost field-type-taxonomy-term-reference field-label-hidden field-label-inline clearfix'}).find('div',attrs={'class':'field-item even'}).get_text()
			except:
				project_cost = 'None'

			try:
				project_length = project_tree.find('div', attrs={'class':'hidden-xs abs-aligned'}).find('div', attrs={'class':'field field-name-field-fdb-project-length field-type-text field-label-hidden field-label-inline clearfix'}).find('div',attrs={'class':'field-item even'}).get_text()
				# if project_length:
				# 	project_length =project_length.get_text()
				# else:
				# 	project_length = 'None'	
			except:
				project_length = 'None'

			try:
				prject_summary = project_tree.find('div', attrs={'class':'review-mobile-cp hideon_active'}).find('div', attrs={'class':'field field-name-field-fdb-proj-description field-type-text-long field-label-inline clearfix'}).find('div',attrs={'class':'field-item even'}).find('p').get_text()
			except:
				prject_summary = 'None'

			try:
				reviewer_role = reviewer_tree.find('div', attrs={'class':'group-fdb-interview hidden-xs'}).find('div', attrs={'class':'field field-name-field-fdb-title field-type-text field-label-hidden'}).find('div',attrs={'class':'field-item even'}).get_text()
			except:
				reviewer_role = 'None'

			try:
				reviewer_name = reviewer_tree.find('div', attrs={'class':'group-fdb-interview hidden-xs'}).find('div', attrs={'class':'field field-name-field-fdb-full-name-display field-type-text field-label-hidden'}).find('div',attrs={'class':'field-item even'}).get_text()
			except:
				reviewer_name = 'None'

			try:
				industry_type = reviewer_tree.find('div', attrs={'class':'group-fdb-interview hidden-xs'}).find('div', attrs={'class':'field field-name-field-fdb-user-industry field-type-text field-label-hidden field-label-inline clearfix'}).find('div',attrs={'class':'field-item even'}).get_text()
			except:
				industry_type = 'None'

			try:
				rev_company_size = reviewer_tree.find('div', attrs={'class':'group-fdb-interview hidden-xs'}).find('div', attrs={'class':'field field-name-field-fdb-company-size field-type-text field-label-hidden field-label-inline clearfix'}).find('div',attrs={'class':'field-item even'}).get_text()
			except:
				rev_company_size = 'None'

			try:
				reviewer_location = reviewer_tree.find('div', attrs={'class':'group-fdb-interview hidden-xs'}).find('div', attrs={'class':'field field-name-field-fdb-location field-type-text field-label-hidden field-label-inline clearfix'}).find('div',attrs={'class':'field-item even'}).get_text()
			except:
				reviewer_location = 'None'

			# print "project Details-->", project, project_category, project_cost, project_length, prject_summary
			# print "reviewer Detail--->",reviewer_name, reviewer_role,  industry_type,rev_company_size,reviewer_location,"\n"
			if index == rev_count-1:
				break

		except:
			print "error in reading field"

		reviewer_list.append(project.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(project_category.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(project_cost.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(project_length.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(prject_summary.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(reviewer_name.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(reviewer_role.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(industry_type.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(rev_company_size.encode('ascii', 'ignore').decode('ascii'))
		reviewer_list.append(reviewer_location.encode('ascii', 'ignore').decode('ascii'))
		csvwriter.writerow(reviewer_list)


reviewer_csv.close()

