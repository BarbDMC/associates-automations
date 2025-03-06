import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Establece el path del ejecutable de Chrome y el de ChromeDriver
        chrome_driver_path = '/home/barbdmc/.local/share/undetected_chromedriver/undetected_chromedriver'
        chrome_exe_path = '/usr/bin/google-chrome'

        # Configura las opciones de Chrome
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_exe_path
        # options.add_argument('--headless')  # Ejecutar en modo headless

        # Inicializa el driver
        self.driver = uc.Chrome(options=options, driver_executable_path=chrome_driver_path)

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

    def test_login_success(self):
        # Navegar a la página de login
        self.driver.get('https://platzi.com/login/')

        # Espera a que el campo de correo esté disponible y lo llena
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_field.send_keys('barbaradmorantesc@gmail.com')

        # Haz clic en el botón de continuar
        continue_button = self.driver.find_element(By.CSS_SELECTOR, '[data-qa="continueBtn"]')
        continue_button.click()

        # Espera a que el campo de contraseña esté disponible y lo llena
        time.sleep(30)
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_field.send_keys('unapashbfisocpwi')

        # Haz clic en el botón de login
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'a[data-qa="loginBtn"]')
        login_button.click()

        # Espera a que la URL sea la de la página de inicio
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be('https://platzi.com/home/')
        )

        # Obtiene la URL actual y verifica que sea la correcta
        current_url = self.driver.current_url
        self.assertEqual(current_url, 'https://platzi.com/home/')

if __name__ == '__main__':
    unittest.main()
