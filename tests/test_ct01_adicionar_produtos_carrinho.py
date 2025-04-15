from time import sleep
import pytest
from selenium.webdriver.common.by import By
from conftest import driver

@pytest.mark.usefixtures("setup_teardown" )
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.ID, "login-button").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']").click()
        sleep(1)
        driver.find_element(By.ID, "add-to-cart").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*[@data-test='shopping-cart-link']").click()
        sleep(1)
        driver.find_element(By.ID, "checkout").click()
        sleep(1)
        driver.find_element(By.ID, "first-name").send_keys("Matheus")
        sleep(1)
        driver.find_element(By.ID, "last-name").send_keys("Souza")
        sleep(1)
        driver.find_element(By.ID, "postal-code").send_keys("87083-020")
        sleep(1)
        driver.find_element(By.ID, "continue").click()
        sleep(1)
        driver.find_element(By.ID, "finish").click()
        sleep(1)
        assert driver.find_element(By.XPATH, "//*[@data-test='complete-header']").is_displayed()
        sleep(1)
        driver.find_element(By.ID, "back-to-products").click()
        sleep(1)