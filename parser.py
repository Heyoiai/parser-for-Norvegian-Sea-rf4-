import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from itertools import islice
import json


def all_parsing() -> dict[str, dict[str, list]]:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    with webdriver.Chrome(options=options) as browser:
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
                location = i.find_element(By.CSS_SELECTOR, f'div.row:nth-child({start_value}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)').text
                fish = i.find_element(By.CLASS_NAME, 'text').text
                temp_bait = []
                for j in i.find_elements(By.CLASS_NAME, 'bait_icon'):
                    temp_bait.append(j.get_attribute('title'))
                result_dict.setdefault(location, {}).setdefault(fish, temp_bait)
            except:
                continue
        return result_dict
#сохранить результаты всего парсинга в json файл
def save_all_parsing_in_json(result_dict: dict[str, dict[str, list]], file_name='all_parsing_result.json') -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=2)
#вывод из json формата в питон формат
def load_parsing_results(filename='all_parsing_result.json') -> dict:
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def result():
    result_dict = all_parsing()
    save_all_parsing_in_json(result_dict)
    return None

random_fish = ['Акула гигантская', 'Акула гренландская полярная',
               'Акула плащеносная', 'Акула сельдевая атлантическая',
               'Берикс красный', 'Гимантолоф атлантический', 'Горбыль серебристый',
               'Зубатка синяя', 'Кальмар обыкновенный', 'Конгер', 'Краб камчатский',
               'Меч-рыба', 'Мольва голубая', 'Мольва обыкновенная', 'Морской чёрт',
               'Окунь каменный', 'Окунь морской золотистый', 'Окунь морской норвежский',
               'Окунь-клювач', 'Опах краснопёрый', 'Палтус атлантический', 'Палтус синекорый',
               'Тунец голубой', 'Центролоф чёрный']
small_fish = ['Бельдюга европейская', 'Макрель атлантическая', 'Путассу северная',
              'Сайра атлантическая', 'Сардина европейская', 'Сельдь атлантическая']
other_fish = ['Бельдюга европейская', 'Гребешок исландский', 'Камбала морская',
              'Камбала палтусовидная', 'Камбала хоботная', 'Катран', 'Керчак европейский',
              'Краб съедобный', 'Менёк', 'Мерланг', 'Мерлуза', 'Мидия', 'Пикша', 'Пинагор',
              'Поллак', 'Сайда', 'Треска атлантическая', 'Тюрбо', 'Устрица съедобная']

def baits_for_random_fish(result_dict):
    temp_dict = {}
    for k, v in result_dict['Норвежское море'].items():
        if k in random_fish:
            for i in v:
                temp_dict[i] = temp_dict.get(i, 0) + 1
    return list(islice(dict(sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)).items(), 5))

def baits_for_small_fish(result_dict):
    temp_dict = {}
    for k, v in result_dict['Норвежское море'].items():
        if k in small_fish:
            for i in v:
                temp_dict[i] = temp_dict.get(i, 0) + 1
    return list(islice(dict(sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)).items(), 5))

def baits_for_other(result_dict):
    temp_dict = {}
    for k, v in result_dict['Норвежское море'].items():
        if k in other_fish:
            for i in v:
                temp_dict[i] = temp_dict.get(i, 0) + 1
    return list(islice(dict(sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)).items(), 8))




