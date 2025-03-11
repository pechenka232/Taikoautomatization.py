from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Подключаемся к открытому Chrome
# Можно сделать через chromedriver, но в моем случае легче через открытый Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = ""
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

try:
    # 1️⃣ Открываем сайт
    driver.get("https://ritsu.xyz/")
    
    # 2️⃣ Нажимаем кнопку "Connect"
    connect_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Connect')]")))
    connect_button.click()
    print("✅ Кнопка 'Connect' нажата")
    time.sleep(2)

    # 3️⃣ Выбираем Rabby Wallet
    wallet_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Rabby Wallet')]")))
    wallet_button.click()
    print("✅ 'Rabby Wallet' выбран")
    time.sleep(2)

    # 4️⃣ Нажимаем "Sign"
    sign_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign')]")))
    sign_button.click()
    print("✅ Кнопка 'Sign' нажата")
    time.sleep(3)

    # 5️⃣ Совершаем 20 обменов ETH → WETH
    for i in range(20):
        print(f"🔄 Обмен {i+1}/20: ETH → WETH")

        # Ввод ETH
        eth_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter amount']")))
        eth_input.clear()
        eth_input.send_keys("0.0001")

        # Нажимаем кнопку "Swap"
        swap_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Swap')]")))
        swap_button.click()
        time.sleep(2)

        # Подтверждаем обмен
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm Swap')]")))
        confirm_button.click()
        print("✅ Обмен ETH → WETH выполнен")
        time.sleep(5)

    # 6️⃣ Совершаем 20 обменов WETH → ETH
    for i in range(20):
        print(f"🔄 Обмен {i+1}/20: WETH → ETH")

        # Выбираем WETH
        weth_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'WETH')]")))
        weth_button.click()
        time.sleep(1)

        # Ввод WETH
        weth_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter amount']")))
        weth_input.clear()
        weth_input.send_keys("0.0001")

        # Нажимаем кнопку "Swap"
        swap_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Swap')]")))
        swap_button.click()
        time.sleep(2)

        # Подтверждаем обмен
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm Swap')]")))
        confirm_button.click()
        print("✅ Обмен WETH → ETH выполнен")
        time.sleep(5)

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()
