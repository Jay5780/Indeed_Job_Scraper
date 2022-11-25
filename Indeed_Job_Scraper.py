from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from csv import writer



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



#function to get data from webpage

def get_Data(page,job):
    driver.get(f'https://in.indeed.com/jobs?q={job}&start={page}')
    beacon = driver.find_elements(By.CLASS_NAME,'job_seen_beacon')
    extract_Data(beacon)



#function to extract required fields from web data

def extract_Data(boxes):
    with open('Jobs.csv','a',encoding='utf8',newline='') as f:
        theWriter = writer(f)
           
        for box in boxes:
            list = box.text.split("\n")
            Title = list[0]
            if list[1]=="new":
                list.remove("new")
                Company =list[1]
            else:
                Company = list[1]

            location = list[2]
            salary = list[3]
            Type = list[4]

            details = [Title,Company,location,salary,Type]
            theWriter.writerow(details)
            
        
        

#function to initiate the data extraction process

def main(pages,job):
    for i in range(pages):
        get_Data(i*10,job)
        time.sleep(2)



if __name__ == '__main__':

    with open('Jobs.csv','a',encoding='utf8',newline='') as f:
        theWriter = writer(f)
        header = ["Job Title"," Company Name "," Location " ," Salary "," Type of Job"]
        theWriter.writerow(header)

    job = "python developer"           # Enter The job title to search
    pages = 5                          # number of pages to scrap
                       
    main(pages,job)
  









