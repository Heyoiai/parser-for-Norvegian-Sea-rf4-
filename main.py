import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def all_parsing() -> {str: {str:list}}:
    with webdriver.Chrome() as browser:
        url = 'https://rf4game.ru/records/weekly'
        browser.get(url)

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located
                                                ((By.CSS_SELECTOR, '.records > div:nth-child(2) > div:nth-child(4)'))) # пока элемент не станет доступен на странице
        start_value = 0
        result_dict = {}
        for i in browser.find_elements(By.CLASS_NAME, 'row'):
            if i.get_attribute('class') == 'row header':
                start_value += 1
            try:
                #print(i.find_element(By.CSS_SELECTOR, f'div.row:nth-child({start_value}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)').text)
                location = i.find_element(By.CSS_SELECTOR, f'div.row:nth-child({start_value}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)').text
                #print(i.find_element(By.CLASS_NAME, 'text').text)
                fish = i.find_element(By.CLASS_NAME, 'text').text
                temp_bait = []
                for j in i.find_elements(By.CLASS_NAME, 'bait_icon'):
                    temp_bait.append(j.get_attribute('title'))
                result_dict.setdefault(location, {}).setdefault(fish, temp_bait)

                    #print(j.get_attribute('title'))
                #start_value += 1
            except:
                continue
                #print(i.find_element(By.CLASS_NAME, 'bait_icon').get_attribute('title'))
        return result_dict

if __name__ == "__main__":
    # Вызов функции
    print(all_parsing())



