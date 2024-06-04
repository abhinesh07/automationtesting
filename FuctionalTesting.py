from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expectedVegetables = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 kg"]
actualVegetables = []
edge_driver_path = r"C:\Users\vijay\Downloads\edgedriver_win64\msedgedriver.exe"
service_obj = Service(edge_driver_path)
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise#/")

search_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[2]/form/input')
search_input.send_keys("ber")
sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0
for result in results:
    actualVegetables.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH, "div/button").click()
print(actualVegetables)
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


prices = driver.find_elements(By.XPATH, "//td[5]//p[@class='amount']")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print("Sum:", sum)  # Print the calculated sum

totalAmount = int(driver.find_element(By.XPATH,
"//span[@class='totAmt']").text)
print("Total Amount:", totalAmount)  # Print the total amount

assert sum == totalAmount

driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)

totalAfterDis = float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)
print("total amount after discount:",totalAfterDis)
assert totalAfterDis < totalAmount

driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/button').click()
dropdown1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/select/option[89]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/button').click()


driver.quit()

