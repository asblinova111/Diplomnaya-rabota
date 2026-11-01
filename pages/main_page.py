from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.common.keys import Keys


class MainPage:
    URL = "https://www.kinopoisk.ru/"
    SEARCH_FIELD = (By.NAME, "kp_query")
    CLOSE_POPUP_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'CloseButton') and (text()='Закрыть' or ./*[name()='svg'])]",
    )
    FIRST_SEARCH_RESULT_TITLE = (
        By.XPATH,
        '//section[@data-testid="search-top-result"]//span[contains(@class, "styles_mainTitle")]',
    )
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), 'Найти')]")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open_page(self) -> None:
        self.driver.get(self.URL)

    def search(self, query: str) -> None:
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_FIELD)
        )
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

    def click_search(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_BUTTON))

    def top_result(self):
        film = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_SEARCH_RESULT_TITLE)
        )
        return film.text
    
    def click_button(self, button):
        item=(By.XPATH, f"//span[normalize-space()= '{button}']")
        element=self.wait.until(EC.visibility_of_element_located(item))
        element.click()

    def is_films(self) -> bool:
        if "lists/categories/movies" in self.driver.current_url:
            return True
            
        self.open_page()
        self.click_button("Фильмы")
        return "movies" in self.driver.current_url.lower() or "lists" in self.driver.current_url.lower()
    
    def is_serials(self) -> bool:
            if self.driver.current_url == "https://www.kinopoisk.ru/lists/categories/movies/3/":
                return True 
     
    def is_chanells(self) -> bool:
            return "hd.kinopoisk.ru/channels" in self.driver.current_url

    def is_sport(self) -> bool:
            return "https://hd.kinopoisk.ru/sport/" in self.driver.current_url
    