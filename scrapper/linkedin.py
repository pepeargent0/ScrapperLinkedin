import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ScraperLinkedIn:
    """
    Clase para iniciar sesión en LinkedIn y realizar acciones como seguir URLs.

    Atributos:
    email (str): El correo electrónico del usuario.
    password (str): La contraseña del usuario.
    driver (webdriver): El controlador del navegador Selenium.
    cookies_file (str): El archivo donde se almacenan las cookies de sesión.
    """

    def __init__(self, email, password):
        """
        Inicializa la clase ScraperLinkedIn con el correo y la contraseña del usuario.

        Args:
        email (str): El correo electrónico del usuario.
        password (str): La contraseña del usuario.
        """
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.cookies_file = 'linkedin_cookies.pkl'
        logger.info('ScraperLinkedIn inicializado.')

    def login(self):
        """
        Inicia sesión en LinkedIn y guarda las cookies de sesión en un archivo.
        """
        try:
            self.driver.get('https://www.linkedin.com/login')
            time.sleep(2)

            username = self.driver.find_element(By.ID, 'username')
            password = self.driver.find_element(By.ID, 'password')

            username.send_keys(self.email)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)

            time.sleep(5)
            self.save_cookies()
            logger.info('Inicio de sesión exitoso.')
        except Exception as e:
            logger.error(f'Error durante el inicio de sesión: {e}')

    def save_cookies(self):
        """
        Guarda las cookies de sesión en un archivo.
        """
        try:
            with open(self.cookies_file, 'wb') as file:
                pickle.dump(self.driver.get_cookies(), file)
            logger.info('Cookies guardadas correctamente.')
        except Exception as e:
            logger.error(f'Error al guardar las cookies: {e}')

    def load_cookies(self):
        """
        Carga las cookies de sesión desde un archivo.
        """
        try:
            self.driver.get('https://www.linkedin.com')
            with open(self.cookies_file, 'rb') as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()
            logger.info('Cookies cargadas y sesión restaurada.')
        except Exception as e:
            logger.error(f'Error al cargar las cookies: {e}')

    def follow_urls(self, urls):
        """
        Sigue una lista de URLs proporcionada y realiza acciones en cada página.

        Args:
        urls (list): Lista de URLs a seguir.
        """
        self.load_cookies()
        for url in urls:
            try:
                self.driver.get(url)
                time.sleep(2)
                logger.info(f'Visitada URL: {url}')
                try:
                    follow_button = self.driver.find_element(By.XPATH, '//button[contains(@aria-label, "Follow") or contains(@aria-label, "Seguir")]')
                    follow_button.click()
                    logger.info(f'Seguido el perfil: {url}')
                except Exception as e:
                    logger.error(f'Error al hacer clic en seguir en {url}: {e}')
            except Exception as e:
                logger.error(f'Error al seguir la URL {url}: {e}')

    def close(self):
        """
        Cierra el navegador.
        """
        self.driver.quit()
        logger.info('Navegador cerrado.')



