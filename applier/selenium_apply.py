from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumApplier:
    def __init__(self, headless=True):
        opts = webdriver.ChromeOptions()
        if headless:
            opts.add_argument("--headless")
        self.driver = webdriver.Chrome(options=opts)

    def apply(self, job, resume_path, cover_text):
        self.driver.get(job['url'])
        time.sleep(2)
        self.driver.find_element(By.NAME, "resume").send_keys(resume_path)
        self.driver.find_element(By.NAME, "cover_letter").send_keys(cover_text)
        self.driver.find_element(By.XPATH, "//button[contains(., 'Submit')]").click()
        time.sleep(2)
