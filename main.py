from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def open_website():
    driver = webdriver.Chrome(executable_path="C:\\Users\\ajain\\Downloads\\chromedriver.exe")
    driver.get("http://localhost:3000")
    return driver

def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//label[text()='Email']/../div//input")
    username_field.send_keys(username)
    time.sleep(1)
    password_field = driver.find_element(By.XPATH, "//label[text()='Password']/..//div//input")
    password_field.send_keys(password)
    time.sleep(1)
    login_button = driver.find_element(By.XPATH, '//div/button[text()="Login"]')
    login_button.click()
    time.sleep(1)

def search(driver):
    print('')
    search_field = driver.find_element(By.XPATH, "//div//input[@id=':r5:']")
    search_item = 'rick'
    search_field.send_keys(search_item)
    time.sleep(5)
    getName(driver)

def getName(driver):
    search_list = []
    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]/../../../div[@class="MuiDataGrid-row MuiDataGrid-row--lastVisible"]')
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        search_list.extend([i.text for i in res])
        driver.execute_script("arguments[0].scrollIntoView();", res[-1])
        if for_parent_of_last and "lastVisible" in for_parent_of_last[-1].get_attribute('class'):
            break
        time.sleep(2)
    print(f"searchlist={search_list},\n total results: {len(search_list)}")
    return search_list

def sort(driver):
    sort_button = driver.find_element(By.XPATH, '//div[text()="Name"]')
    sort_button.click()
    time.sleep(1)
    scroll_to_top(driver)
    search_list1 = getName(driver)
    search_list_ascending = search_list1
    search_list1.sort()
    if(search_list_ascending == search_list1):
        print('sorted in ascending')
    else:
        print('not sorted in ascending') 
    sort_button.click()
    scroll_to_top(driver)
    search_list2 = getName(driver)
    search_list_descending = search_list2
    search_list2.sort(reverse=True)
    if(search_list_descending == search_list2):
        print('sorted in descending')
    else:
        print('not sorted in descending') 

def scroll_to_top(driver):
    action = ActionChains(driver)
    print("Scrolling to top")
    while True:
        for_parent_of_first = driver.find_elements(By.XPATH, "//div[@data-rowindex = '1']")
        res = driver.find_elements(By.XPATH, '//div[@data-field="name"]/div[text()]')
        action.scroll_to_element(res[0]).perform()
        if for_parent_of_first:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "1"]/div[@data-field="name"]/div[text()]')
            break
        time.sleep(1)

if __name__ == "__main__":
    driver = open_website()
    time.sleep(1)
    print("website open")
    login(driver, 'aditi@gmail.com', '123')
    print("user is logged in application")
    search(driver)
    sort(driver)