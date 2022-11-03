from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def click_element_by_css_selector(self, css_selector):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).click()


def send_keys_by_css_selector(self, css_selector, text):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(text)


def element_displayed(self, css_selector):
    return self.driver.find_element(By.CSS_SELECTOR, css_selector).is_displayed()


def get_element_text(self, css_selector):
    return self.driver.find_element(By.CSS_SELECTOR, css_selector).text


def click_on_a_product(self, css_selector):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).click()


def wait_until_element_displayed(self, css_selector):
    WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
