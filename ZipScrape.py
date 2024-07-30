import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

options = uc.ChromeOptions()
driver = uc.Chrome(options=options, use_subprocess=True)

loaction = 'chicago'
title = 'software developer'

page_number = [
    '//*[@id="react-job-results-root"]/div/div[1]/div[22]/div[1]/div[2]/a',
    '//*[@id="react-job-results-root"]/div/div[1]/div[22]/div[1]/div[3]/a',
    '//*[@id="react-job-results-root"]/div/div[1]/div[22]/div[1]/div[4]/a',
    '//*[@id="react-job-results-root"]/div/div[1]/div[22]/div[1]/div[5]/a'
]

all_jobs = []

# .clear() doesnt work on mac
def clear_searchbox(element, blank=''):
    while element.get_attribute("value") != blank:
        input_text = element.get_attribute("value")
        if input_text is not None:
            for _ in range(len(input_text)):
                element.send_keys(Keys.BACKSPACE)

def scrape_job():
    
    title_xpath = '//*[@id="react-job-results-root"]/div/div[2]/div[2]/div[1]/div[1]/h1'
    while(True):
        try:
            title_element = driver.find_element(By.XPATH, title_xpath)
            break
        except:
            None

    title_element = driver.find_element(By.XPATH, title_xpath)
    title_text = title_element.text

    company_xpath = '//*[@id="react-job-results-root"]/div/div[2]/div[2]/div[1]/div[2]/a'
    company_element = driver.find_element(By.XPATH, company_xpath)
    company_text = company_element.text
    
    identifier = title_text + ' ' + company_text
    return identifier
    

def click_job():
    action = ActionBuilder(driver)
    action.pointer_action.move_to_location(100, 200)
    action.pointer_action.click()
    action.perform()

def scroll(scrollable_element):
    driver.execute_script("arguments[0].scrollBy(0, 100);", scrollable_element)

def scrape_page():
    

    job_list = []
    while(len(job_list)<20):
        scrollable_element = driver.find_element(By.XPATH, '//*[@id="react-job-results-root"]/div/div[1]')
        click_job()

        try:
            job_identifier = scrape_job()
            if job_identifier not in job_list:
                job_list.append(job_identifier)
        except:
            None

        scroll(scrollable_element)
    all_jobs.append(job_list)
        


def load_job_site():
    driver.get('https://www.ziprecruiter.com/')

    keyword_searchbox = driver.find_element(By.XPATH, '//*[@id=":R4pmja:-input"]')
    location_searchbox = driver.find_element(By.XPATH, '//*[@id=":R6pmja:-input"]')
    search_button = driver.find_element(By.XPATH, '//*[@id=":R8pmja:"]')

    clear_searchbox(location_searchbox)

    keyword_searchbox.send_keys(title)
    location_searchbox.send_keys(loaction)

    search_button.click()

load_job_site()

for index in range(5):
    scrape_page()
    
    if index < 4:
        next_page = driver.find_element(By.XPATH,page_number[index])
        next_page.click()
    

print(len(all_jobs))
print(all_jobs)



driver.quit()

