import requests
import pytest
import allure
import json
from typing import Dict, Any

API_BASE_URL = "https://kinopoiskapiunofficial.tech/api/"
API_KEY = "6c0e63a4-6e05-4acb-acd8-d3e785bfe2c3"
my_headers = {"X-API-KEY": API_KEY}


@pytest.mark.api
@allure.feature("Поиск через Кинопоиск API")
@allure.story("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Поиск фильма по существующему ID")
def test_search_by_id():
    film_id = 4540126
    headers = my_headers

    with allure.step(
        f"Отправка GET-запроса для получения фильма с ID {film_id}"
    ):
        response = requests.get(
            f"{API_BASE_URL}v2.2/films/{film_id}", headers=headers
            )

    with allure.step("Проверка статус-кода ответа (должен быть 200)"):
        assert response.status_code == 200

    with allure.step(
        f"Проверка, что в ответе вернулся фильм с kinopoiskId = {film_id}"
    ):
        data = response.json()
        assert data["kinopoiskId"] == film_id


@pytest.mark.api
@allure.feature("Поиск через Кинопоиск API")
@allure.story("Поиск фильмов")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Поиск фильма по ключевому слову (названию)")
def test_search_by_name():
    film_name = "Дюна"
    query_params: Dict[str, Any] = {
        "order": "RATING",
        "type": "ALL",
        "ratingFrom": 0,
        "ratingTo": 10,
        "yearFrom": 1000,
        "yearTo": 3000,
        "keyword": film_name,
        "page": 1
    }
    headers = my_headers

    with allure.step(
        f"Отправка GET-запроса поиска фильмов"
        f"по ключевому слову '{film_name}'"
    ):
        response = requests.get(
            f"{API_BASE_URL}v2.2/films",
            headers=headers,
            params=query_params
        )

    with allure.step("Проверка статус-кода ответа (должен быть 200)"):
        assert response.status_code == 200

    with allure.step(
        f"Проверка, что слово '{film_name}' "
        "присутствует в названии хотя бы одного фильма"
    ):
        data = response.json()
        name_found: bool = False
        for item in data["items"]:
            if film_name.lower() in item["nameRu"].lower():
                name_found = True
                break
        assert name_found, (
            f"Ни один фильм в результатах"
            f"не содержит в названии '{film_name}'"
        )


@pytest.mark.api
@allure.feature("Поиск через Кинопоиск API")
@allure.story("Поиск персон")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Поиск режиссера по имени и фамилии")
def test_search_by_surname():
    surname = "Дени Вильнёв"
    query_params: Dict[str, Any] = {
        "name": surname,
        "page": 1
    }
    headers = my_headers

    with allure.step(f"Отправка GET-запроса поиска персоны '{surname}'"):
        response = requests.get(
            f"{API_BASE_URL}v1/persons", headers=headers, params=query_params
            )

    with allure.step("Проверка статус-кода ответа (должен быть 200)"):
        assert response.status_code == 200

    with allure.step(
        f"Проверка, что имя первой найденной"
        f"персоны совпадает с '{surname}'"
    ):
        data = response.json()
        first_person: Dict[str, Any] = data["items"][0]
        assert first_person["nameRu"] == surname, (
             f"Ожидалось имя {surname}, но получили"
             f"{first_person['nameRu']}"
        )


@pytest.mark.api
@allure.feature("Поиск через Кинопоиск API")
@allure.story("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Поиск фильма с пустым/невалидным токеном авторизации")
def test_search_without_auth():
    film_id = 4540126
    headers = {"X-API-KEY": ""}

    with allure.step(
        f"Отправка GET-запроса без валидного токена"
        f"для фильма ID {film_id}"
    ):
        response = requests.get(
            f"{API_BASE_URL}v2.2/films/{film_id}", headers=headers
        )

    with allure.step("Проверка возврата ошибки авторизации (статус-код 401)"):
        assert response.status_code == 401

    with allure.step("Проверка текста сообщения об ошибке доступа"):
        data = response.json()
        assert "You don't have permissions" in data["message"]


@pytest.mark.api
@allure.feature("Поиск через Кинопоиск API")
@allure.story("Поиск фильмов")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Поиск фильма по несуществующему ID")
def test_search_by_non_existent_id():
    film_id = 9999999
    headers = my_headers

    with allure.step(
        f"Отправка GET-запроса для несуществующего фильма с ID {film_id}"
    ):
        response = requests.get(
            f"{API_BASE_URL}v2.2/films/{film_id}", headers=headers
            )

    with allure.step("Проверка возврата ошибки 404 (Not Found)"):
        assert response.status_code == 404
