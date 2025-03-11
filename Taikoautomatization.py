from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Путь к chromedriver (укажи свой)
CHROMEDRIVER_PATH = "/path/to/chromedriver"

# Настройки Chrome
options = Options()
options.add_argument("--start-maximized")  # Развернуть браузер
options.add_experimental_option("detach", True)  # Оставить браузер открытым после выполнения

# Запуск Chrome через Selenium
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    # 1️⃣ Открываем сайт
    driver.get("https://ritsu.xyz/")
    time.sleep(5)

    # 2️⃣ Подключаем Rabby Wallet
    connect_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Подключить кошелек')]")
    connect_button.click()
    time.sleep(3)

    # 3️⃣ Ждем открытия Rabby Wallet
    time.sleep(5)
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[1])

    # 4️⃣ Подключаем кошелек
    connect_wallet_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Подключить')]")
    connect_wallet_button.click()
    time.sleep(3)

    # 5️⃣ Переключаемся обратно на сайт
    driver.switch_to.window(all_windows[0])
    time.sleep(2)

    # 6️⃣ Делаем 20 обменов ETH → WETH
    for i in range(20):
        print(f"🔄 Обмен {i + 1}/20: ETH → WETH")

        # Нажимаем кнопку "Отправить"
        send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Отправить')]")
        send_button.click()
        time.sleep(3)

        # Вводим сумму 0.0001 ETH
        amount_input = driver.find_element(By.XPATH, "//input[@type='number']")
        amount_input.clear()
        amount_input.send_keys("0.0001")
        time.sleep(2)

        # Подтверждаем отправку
        confirm_send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Подтвердить')]")
        confirm_send_button.click()
        time.sleep(3)

        # Переключаемся в Rabby Wallet
        driver.switch_to.window(all_windows[1])
        time.sleep(2)

        # Подтверждаем транзакцию
        confirm_transaction_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Подтвердить')]")
        confirm_transaction_button.click()
        time.sleep(3)

        # Переключаемся обратно на сайт
        driver.switch_to.window(all_windows[0])
        time.sleep(5)

        print(f"✅ Обмен {i + 1}/20 завершен!")

    print("🎉 Все 20 обменов ETH → WETH выполнены!")

    # 7️⃣ Делаем 20 обменов WETH → ETH
    for i in range(20):
        print(f"🔄 Обмен {i + 1}/20: WETH → ETH")

        # 🔄 Переключаем направление обмена (ищи XPATH кнопки смены)
        switch_button = driver.find_element(By.XPATH, "//button[contains(text(), '⇄')]")
        switch_button.click()
        time.sleep(3)

        # Нажимаем "Отправить"
        send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Отправить')]")
        send_button.click()
        time.sleep(3)

        # Вводим сумму 0.0001 WETH
        amount_input = driver.find_element(By.XPATH, "//input[@type='number']")
        amount_input.clear()
        amount_input.send_keys("0.0001")
        time.sleep(2)

        # Подтверждаем отправку
        confirm_send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Подтвердить')]")
        confirm_send_button.click()
        time.sleep(3)

        # Переключаемся в Rabby Wallet
        driver.switch_to.window(all_windows[1])
        time.sleep(2)

        # Подтверждаем транзакцию
        confirm_transaction_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Подтвердить')]")
        confirm_transaction_button.click()
        time.sleep(3)

        # Переключаемся обратно на сайт
        driver.switch_to.window(all_windows[0])
        time.sleep(5)

        print(f"✅ Обмен {i + 1}/20 завершен!")

    print("🎉 Все 20 обменов WETH → ETH выполнены!")

finally:
    time.sleep(5)
    driver.quit()
