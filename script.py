from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chromeのオプション設定
chrome_options = Options()
chrome_options.add_argument("--headless")  # ヘッドレスモードで実行（UIを表示しない）

# ChromeDriverのパスを設定
service = Service('/usr/local/bin/chromedriver')

# WebDriverの初期化
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.add_cookie({"name": "token", "value": 1})
    # ターゲットURLにアクセス
    driver.get('https://reliable-salamander-9e07cf.netlify.app/')

    element = driver.find_element(By.XPATH, "//div[@slot='content' and contains(text(), '顧客管理')]")
    element.click()
    time.sleep(2)  # 少し待機

finally:
    # ブラウザを閉じる
    driver.quit()
