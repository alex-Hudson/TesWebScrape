import requests
import json
import pandas

schools_list = ['The Perse Upper School', 'Abingdon', 'The Leys', 'Kings Ely']

school = {}
for searchString in schools_list:
    print('hello')

    url = "https://www.tes.com/api/jobs/browser/search-v3"
    querystring = {"siteCountry": "gb^", "^": "", "sort": "^", "workplaces": [
        "Independent^%25^20senior^", "Independent^%25^20pre-prep^"], "keywords": searchString}

    headers = {
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        'accept': "application/json, text/plain, */*",
        'referer': "https://www.tes.com/jobs/search?siteCountry=gb^&sort=^&workplaces=Independent^%^20senior^&workplaces=Independent^%^20pre-prep^&keywords=perse^&locations=United^%^20Kingdom^%^3AEngland",
        'authority': "www.tes.com",
        'cookie': "csrf=a52882f3f672baf15bde8544647a21b3; __tese=0981cdbb-441c-4bb8-98d2-e86bfe63904c; geoCountry=GB; siteCountry=GB; _ga=GA1.2.1399363400.1561393833; __tesu=ae826394-ec5f-430d-af52-a61570fd9f41; _gid=GA1.2.1267084163.1561393833; _fbp=fb.1.1561393832928.768766063; _vwo_uuid_v2=D4E23F6CC3F9392B73D38E483CA2A47AC^|1117eb7df4dd3898b9f37ab3d5356a53; _vis_opt_s=1^%^7C; _vis_opt_test_cookie=1; has_js=1; __tesv=b053cfb3-be1c-44d6-b01a-c8a3318a7ff4; __tess=home^%^7C^%^7C11",
        'cache-control': "no-cache",
        'Postman-Token': "3cb94421-ab85-45c2-8bbe-4c671dc8f9e0"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.text)

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    search_data = json.loads(response.text)
    for job in search_data['searchResult']['jobs']['items']:
        print(job['title'])
        if 'employerName' not in job.keys():
            continue
        schoolName = job['employerName']
        if schoolName not in school.keys():
            school[schoolName] = {}

        jobTitle = job['title']
        school[schoolName][jobTitle] = {}
        school[schoolName][jobTitle]['jobStartDate'] = job['displayJobStartDate']
        school[schoolName][jobTitle]['applicationCloseDate'] = job['application']['displayCloseDate']
        school[schoolName][jobTitle]['contactTerms'] = job['displayContractTerms']
        print(school)


school_json = json.dumps(school)
pandas.read_json(school_json).to_excel("output.xlsx")
