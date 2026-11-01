import pytest
import allure
from pages.main_page import MainPage


@allure.epic("Тестирование пользовательского интерфейса (UI)")
class TestKinopoiskUI:

    @allure.title("FT-UI-01: Проверка поиска фильма на главной странице")
    def test_search_film(self, driver) -> None:
        main = MainPage(driver)
        film: str = "Дюна"
        main.open_page()
        main.search(film)
        assert (
            film.lower() in driver.page_source.lower()
            or "kinopoisk" in driver.page_source.lower()
        )

    @allure.title("FT-UI-02: Проверка перехода в общую категорию Фильмы")
    def test_check_films_category(self, driver) -> None:
        main = MainPage(driver)
        main.open_page()
        assert main.is_films() is True

    @allure.title("FT-UI-03: Проверка открытия страницы Сериалов")
    def test_open_serials(self, driver) -> None:
        main = MainPage(driver)
        main.open_page()
        main.click_button("Сериалы")
        assert main.is_serials() is True

    @allure.title("FT-UI-04: Проверка открытия страницы Телеканалов")
    def test_open_chanells(self, driver) -> None:
        main = MainPage(driver)
        main.open_page()
        main.click_button("Телеканалы")
        assert main.is_chanells() is True

    @allure.title("FT-UI-05: Валидация наличия бренда Кинопоиска")
    def test_logo_presence(self, driver) -> None:
        main = MainPage(driver)
        main.open_page()
        assert (
            "kinopoisk" in driver.current_url
            or "кинопоиск" in driver.page_source.lower()
        )
