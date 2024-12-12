import time
# --ilgili kütüphaneler eklendi
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# --chrome options kullanıldı çünkü web sitesinin açıldığında kaybolmaması için
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("D:\software programs\python\Lib\site-packages\selenium\chromedriver.exe")  # Service object belirtildi.

# --Chrome Broswer
driver = webdriver.Chrome(options=chrome_options)  # Chrome doğrudan çağrılamaz, bu nedenle tarayıcıyı çağırmak için kullanılır.
driver.get("https://testcase.myideasoft.com/")  # istenilen web sitesi cağrılır.

    #HomePage

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Aramak istediğiniz ürünü yazınız']").click() #arama butonu seçilir
myElement=driver.find_element(By.NAME, "q").send_keys("ürün") # araba butonuna "ürün" yazılır
time.sleep(3) #3 sn bekleme süresi eklenir

#arama çubuğunda "ürün" girildikten sonra açılan dinamik drop down penceresi seçilir
actions=ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
time.sleep(5) #5 sn bekleme süresi eklenir

    #CheckOutPage

dropdown=Select(driver.find_element(By.ID, "qty-input")) #statik drop down menü seçildi
dropdown.select_by_visible_text("5") # üründen 5 adet seçildi

driver.find_element(By.CSS_SELECTOR, "a[class='add-to-cart-button'] span").click() #5 adet ürün sepete eklendi
time.sleep(2)
driver.get_screenshot_as_file("screen.png") #sepete eklenmiş olan 5 adet ürüne ait ekran alıntısı

    #ConfirmPage

driver.find_element(By.CSS_SELECTOR, "a[title='Sepet'] span").click() #sepet sayfasına gidilir
assert driver.find_element(By.XPATH, "//input[@value='5']").is_displayed() #sepete 5 adet ürün eklendi mi? T or F döner
message=driver.find_element(By.XPATH, "//input[@value='5']").is_displayed()
print(message) #T, sepete 5 adet ürün eklendi.
driver.get_screenshot_as_file("addingToCardFiveItems.png") #sepete eklenmiş olan 5 adet ürüne ait ekran alıntısı















