from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from utils.utilities import ExceptionHandler

class LoginScrape:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        
    def login(self, username, password):
        self.driver.get('https://www.linkedin.com/login')
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.get('https://www.linkedin.com/jobs/collections/still-hiring')

            
    def scrape_title_corp_desc(self):
        job_title_path    = (By.CLASS_NAME, 'job-details-jobs-unified-top-card__job-title-link')
        company_name_path = (By.XPATH,      '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div')
        job_desc_path     = (By.XPATH,      '//*[@id="job-details"]')

        try:
            job_title    = self.driver.find_element(*job_title_path)    
            company_name = self.driver.find_element(*company_name_path) 
            job_desc     = self.driver.find_element(*job_desc_path)     

            return job_title.text, company_name.text, job_desc.text
        
        except Exception as e:
            ExceptionHandler.handle_exception(e)
            return None, None


    def close_browser(self):
        self.driver.quit()
