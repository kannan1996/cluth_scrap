import requests
import csv, json
import time
from bs4 import BeautifulSoup

# page = requests.get("https://clutch.co/agencies")

# soup = BeautifulSoup(page.content, 'html.parser')

# print soup.prettify()

# row_provider = soup.find_all(class_="provider-row")

## row_provider = provider.find_all(class_="row provider-row-header")
## field_content = row_provider.find(class_="field-content")

## print row_provider[3].prettify()

company_csv = open('cluth_app_developers_first.csv', 'w')
csvwriter = csv.writer(company_csv)

# csvwriter.writerow('')
csvwriter.writerow(['Organization_name','Min. Project','Rating','Hourly_rate','Total_Employees','Locality','Region','Profile','Website','Mail','Phone'])

new_page = 'https://clutch.co/app-development'

for i in range(1,2):
	page_url = 'https://clutch.co/app-development?page='+str(i)
	print page_url
	page = requests.get(new_page)
	time.sleep(0.5)
	soup = BeautifulSoup(page.content, 'html.parser')
	row_provider = soup.find_all(class_="provider-row")

	for i in range(len(row_provider)):
		company_list = []
		profile = row_provider[i].find(class_="row-header").find(class_="company-name").a['href']
		company = row_provider[i].find(class_="row-header").find(class_="company-name").get_text()
		full_profile = 'https://clutch.co'+profile
		print company, full_profile

		# min_project = row_provider[i].select(".module-list .list-item")[0]
		# if min_project:
		# 	min_project = min_project.get_text()			
		# else:
		# 	min_project = 'None'
		# rating = row_provider[i].find(class_="rating")
		# if rating:
		# 	rating = rating.get_text()
		# else:
		# 	rating = 'None'
		# rate = row_provider[i].find(class_="hourly-rate")
		# if rate:
		# 	rate = rate.get_text()
		# else: 
		# 	rate = 'None'
		# employee = row_provider[i].find(class_="employees")
		# if employee:
		# 	employee = employee.get_text()
		# 	employee = '"{}"'.format(employee)
		# else:
		# 	employee = 'None'
		# locality = row_provider[i].find(class_="locality")
		# if locality:
		# 	locality = locality.get_text()
		# else:
		# 	locality = 'None'
		# region = row_provider[i].find(class_="region")
		# if region:
		# 	region = region.get_text()
		# else:
		# 	region = 'None'
		# website = row_provider[i].find(class_="website-link website-link-a")
		# if website:
		# 	website = website.a['href']
		# else:
		# 	website = 'None'
		# phone = row_provider[i].find('div', attrs={'class' : 'contact-dropdown hide'}).find('div', attrs={'class' : 'item __color6a'})
		# if phone:
		# 	phone = phone.get_text()
		# else:
		# 	phone = 'None'
		# profile = row_provider[i].find('div',attrs={'class':'col-xs-12 col-md-2 provider-link-details'}).find('ul',attrs={'class':'nav nav-pills nav-stacked nav-right-profile'}).find_all('li')
		# if profile:
		# 	profile =profile[1].a['href']
		# else:
		# 	profile = 'None'


		# full_profile = 'https://clutch.co'+profile
		# final_mailId = ''

		# # mail = row_provider[5].find('div', attrs={'class' : 'contact-dropdown hide'}).find('div', attrs={'class' : 'item'}).find('a')
		# mail_script = row_provider[i].find('div', attrs={'class' : 'contact-dropdown hide'}).find('script') #row_provider[4].select(".contact-dropdown  .item").a['href']

		# if mail_script:
		# 	mail_script  = mail_script.get_text()

		# if mail_script != '':
		# 	try:
		# 		mail_script = str(mail_script)
		# 		mail_list = mail_script.split(' = ')
		# 		shuffle_name = mail_list[1].split(';')[0].replace("'","")
		# 		shuffle_pattern = mail_list[3].split(';')[0].split(']')
		# 		spera_name = shuffle_name.split('#')

		# 		for pat in shuffle_pattern:
		# 			if pat != '':
		# 				final_mailId = final_mailId+spera_name[int(pat[-1:])]
		# 		# print "\n",full_profile,final_mailId,"\n"
		# 	except:
		# 		print "error in mail id"


		company_list.append(company.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(min_project.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(rating.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(rate.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(employee.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(locality.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(region.encode('ascii', 'ignore').decode('ascii'))
		company_list.append(full_profile.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(website.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(final_mailId.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(phone.encode('ascii', 'ignore').decode('ascii'))
		# company_list.append(row_provider[i].find(class_="field-content").get_text())
		# company_list.append(row_provider[i].find(class_="rating").get_text() if row_provider[i].find(class_="rating") else None)
		# company_list.append(row_provider[i].find(class_="hourly-rate").get_text() if row_provider[i].find(class_="hourly-rate") else None)
		# company_list.append(row_provider[i].find(class_="employees").get_text() if row_provider[i].find(class_="employees") else None)
		# company_list.append(row_provider[i].find(class_="locality").get_text() if row_provider[i].find(class_="locality") else None)
		# company_list.append(row_provider[i].find(class_="region").get_text() if row_provider[i].find(class_="region") else None)
		csvwriter.writerow(company_list)


company_csv.close()

# wrfile = open('provider.txt','w')
# wrfile.write(text.encode('ascii', 'ignore').decode('ascii'))