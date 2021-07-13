from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class DriverHelper(object):    
    __TIMEOUT = 10

    def __init__(self, driver):
        super(DriverHelper, self).__init__()
        self._driver_wait= WebDriverWait(driver, DriverHelper.__TIMEOUT)
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def current_url(self):
        self.driver.current_url

    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit

    def get_title(self):
        self._driver.title

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_selector(self, selector):
        return self._driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

