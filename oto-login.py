from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CODER BY KRON1K
driver = webdriver.Chrome()
# CODER BY KRON1K
url = "https://m.kentkart.com/cities"

# CODER BY KRON1K
driver.get(url)


# CODER BY KRON1K
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.searchTapTextArea')))
search_input.send_keys("Kocaeli") # BULUNDUĞUNUZ ŞEHİRİ GİRİNİZ.

# Kocaeli seçeneğini bul ve tıkla
kocaeli_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//li[@class="city ng-star-inserted"]//p[text()="Kocaeli"]')))
kocaeli_option.click()

# Kentkart giriş sayfasına git
driver.get("https://m.kentkart.com/account/login")

# Eğer mesaj varsa kabul et
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
except:
    pass  # CODER BY KRON1K

# Oturum bilgileri
phone_number = "5437331923"  # CODER BY KRON1K
password = "515783"  # CODER BY KRON1K

# Telefon numarası kutucuğunun yüklenmesini bekleyin
phone_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="(XXX) XXX XX XX"]')))
phone_input.clear()  # CODER BY KRON1K
for digit in phone_number:
    phone_input.send_keys(digit)
    time.sleep(0.5)  # CODER BY KRON1K

# CODER BY KRON1K
password_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Şifreniz"]')
password_input.send_keys(password)

# CODER BY KRON1K
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.formButton.ng-star-inserted')))
login_button.click()

# CODER BY KRON1K
bakiye_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//h2[text()="Bakiye Sorgulama"]')))
bakiye_button.click()

# CODER BY KRON1K
numara = input("Lütfen numaranızı giriniz: ")
numara_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'aliasNumber')))
numara_input.clear()  # Kutucuğu temizle
for digit in numara:
    numara_input.send_keys(digit)
    time.sleep(0.5)  # CODER BY KRON1K

# CODER BY KRON1K
sorgula_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn-primary.center-block.btn-lg')))
sorgula_button.click()

# CODER BY KRON1K
bakiye_verisi = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[style="font-size: 30px; font-weight: bold; color: #81b71a;"]'))).text

# TL miktarını yazdır
print(f"Bakiyeniz: {bakiye_verisi} TL")

# Tarayıcıyı kapat
driver.quit()
