from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

#open browser
def my_func(driver):
    #navigate to python.org
    driver.get("https://www.python.org/")
    time.sleep (2)
    driver.maximize_window()

    #Search ‘bla bla’ text
    driver.find_element(By.ID,"id-search-field").send_keys("bla bla")
    time.sleep(2)

    # Click on Go button
    driver.find_element(By.CLASS_NAME,"search-button").click()
    time.sleep(2)

#Check that ‘No results found.’ text display in page
    eleSelected= driver.find_element(By.XPATH,'//*[@id="content"]/div/section/form/ul/p').text
    if (eleSelected =="No results found."):
        print("True",'\n')
    #TODO, would be better keep also else and print that you have result

    #Print Page title
    print(driver.title,'\n')
    #Print URL
    print(driver.current_url,'\n')
    #close driver
    driver.close()

my_func(driver = webdriver.Chrome(executable_path=ChromeDriverManager().install()))
my_func(driver= webdriver.Firefox(executable_path=GeckoDriverManager().install()))

#Nel, good job