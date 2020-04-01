import requests
from bs4 import BeautifulSoup
import pandas
from geog_import import get_essex_output_area
import csv
import pandas as pd
from config import Essex_Shape_Config, Web_Scrape_Config


def clean_salary(salary_text:str):
    """converts the salary string to an interger, deals with hourly, daily and annually"""
    salary_text.replace('\n', '')
    word_list = salary_text.split()  #split text into words
    if word_list[-1]=="hour":
        return(word_list[-3].replace('£', '').replace(',', '.'), "hour")
    elif word_list[-1]=="year":
        #careful of this as it needs to prepresnet thousands, not decimal pennies
        return(word_list[-3].replace('£', '').replace(',', ''), "year")
    elif word_list[-1]=="day":
        return(word_list[-3].replace('£', '').replace(',', ''), "day")


def scrape_pages(url:str, region:str):
    """Scrapes the indeed website with the region as a search term"""
    page_collect = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # file = open("web_data/webhtml.txt","r") # static webpage for testing 
    # soup = BeautifulSoup(file, 'html.parser')

    jobobj = soup.find_all("div", {"class": "jobsearch-SerpJobCard unifiedRow row result"}) #get all job positng on the page
    for job in jobobj:
        job_collect = []
        job_collect.append(region)


        job_title_obj = job.find("a", {"class": "jobtitle turnstileLink"}).get_text() #Job title by a id
        job_collect.append(job_title_obj.replace('\n', '').replace('  ', ''))


        try: 
            salary_obj = job.find("span", {"class": "salaryText"}).get_text() #search by a id
            salary_info = clean_salary(salary_obj)
            job_collect.append(salary_info[0]) # salary amount
            job_collect.append(salary_info[1]) # salary frequency

        except:
            job_collect.append("")
            job_collect.append("")

        try:
            company_obj = job.find("span", {"class": "company"}).get_text() #search by a id
            job_collect.append(company_obj.replace('\n', '').replace('  ', ''))
        except:
            job_collect.append("")

        try:
            loc_obj = job.find("div", {"class": "location accessible-contrast-color-location"}).get_text() #search by a id
            job_collect.append(loc_obj.replace('\n', '').replace('  ', ''))
        except:
            job_collect.append("")

        try:
            desc_obj = job.find("div", {"class":"summary"}) #find job descriptions
            desc = desc_obj.find_all('li') 
            s = "" #create empty string object
            for text in desc: 
                s+=(text.get_text()) #concatanate all string job descriptions
            job_collect.append(s)
        except:
            job_collect.append("")
        page_collect.append(job_collect)

    return page_collect







def crawl_pages():
    """Uses the regions dict to crawl through the regions ins essex
    Appends the datafram to a csv file"""
    regions_df = get_essex_output_area() #call geog import function
    regions_arr = regions_df.LAD15NM_x.values #get list of LAU

    regions_arr = ['Rochford' ,'Tendring','Uttlesford']

    print(f"searching these regions {regions_arr}")
    for region in regions_arr:
        print("Now working on Region: " + region)
        search_region= region.partition(' ')[0]
        for page in range(0,Web_Scrape_Config.NUM_PAGES,10): # itterate through all pages of job advertisements
            print(f"Working on page: {page}")
            base_address = f"https://www.indeed.co.uk/jobs?q=&l={search_region}+Essex&start={page}"

            jobs_on_page = scrape_pages(base_address, search_region)
            df = pd.DataFrame(jobs_on_page, columns=Web_Scrape_Config.OUTPUT_COLS)
            df.to_csv(Web_Scrape_Config.SCRAPE_OUTPUT_PATH, index = False, mode='a', header=False)



if __name__ == "__main__":
    #use this for new dataset
    crawl_pages()

