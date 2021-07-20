from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Page(object):    
    __TIMEOUT = 10

    def __init__(self, driver):
        super(Page, self).__init__()
        self.driver_wait= WebDriverWait(driver, Page.__TIMEOUT)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def current_url(self):
        self.driver.current_url()

    def maximize(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.quit

    def get_title(self):
        self.driver.title

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_by_xpath(self, xpath):
        return self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self.driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self.driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_selector(self, selector):
        return self.driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

