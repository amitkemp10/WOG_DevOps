from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import ChromiumOptions


def test_scores_service():
    chrome_options = ChromiumOptions()
    service = Service(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(service=service)
    driver.get("http://127.0.0.1:5000")
    score_value = driver.find_element(By.XPATH, '//*[@id="score"]/h1[2]').text
    score_value = int(score_value)
    if 0 < score_value < 1001:
        return True
    return False


def main():
    check = test_scores_service()
    print(check)
    if check is True:
        return 0
    return -1
