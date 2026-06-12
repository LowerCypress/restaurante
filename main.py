from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

USER = "admin"
PASSWORD = "1234"

def main():
    service = Service(ChromeDriverManager().install())

    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")

    driver = Chrome(service=service, options=option)

    # 1. Abre el enlace local del servidor de Flask
    driver.get("http://127.0.0.1:5000")

    time.sleep(3)

    # 2. Localiza los campos usando el atributo 'name' en lugar de 'id'
    driver.find_element(By.NAME, "username").send_keys(USER)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    
    # 3. Localiza el botón por su clase o etiqueta dentro del formulario
    # Usamos XPATH para asegurarnos de que seleccione el botón correcto de inicio de sesión
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()

    # Espera para ver el resultado antes de cerrar el navegador
    time.sleep(15)

    driver.quit()

if __name__ == "__main__":
    main()