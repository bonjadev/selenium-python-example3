import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoSend_Keys():
    def demo_keys(self):
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            driver.get("https://apollon.rs/log-in")
            driver.maximize_window()
            driver.refresh()
            driver.find_element(By.XPATH, "//button[normalize-space()='STANDARDNI LOG IN']").click()
            driver.find_element(By.XPATH, "//input[@placeholder='Korisničko ime']").send_keys("Votre nom")
            driver.find_element(By.XPATH, "//input[@placeholder='Lozinka']").send_keys("Votre mot de passe")
            time.sleep(5)
            driver.find_element(By.XPATH, "//button[@ id='submit']").click()
            time.sleep(10)
            driver.close()

demo_keys = DemoSend_Keys()
demo_keys.demo_keys()


