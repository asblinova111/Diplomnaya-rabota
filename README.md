# Diplomnaya-rabota
Проект автоматизации тестирования веб-сервиса Кинопоиск

Дипломный проект по курсу «Инженер по тестированию» от Skypro. В рамках проекта реализовано ручное и автоматизированное тестирование ключевого функционала REST API и пользовательского интерфейса (UI) сайта `kinopoisk.ru`.

## Стек технологий
* **Язык:** Python 3.x
* **Тестовый фреймворк:** Pytest
* **UI-автоматизация:** Selenium WebDriver + Page Object Model (POM)
* **API-автоматизация:** Requests
* **Отчетность:** Allure Framework
* **Конфигурация:** Python-dotenv

## Структура проекта
* `pages/` — локаторы и методы для работы с веб-страницами (Page Object).
* `tests/` — UI и API автотесты.
* `conftest.py` — фикстуры для инициализации WebDriver.
* `.env` — файл конфигурации с API-ключами (не логируется в Git).
* `.gitignore` — список исключений для Git.
* `requirements.txt` — используемые зависимости.

## Инструкция по установке и запуску

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com
   cd Diplomnaya-rabota
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте окружение:**
   Создайте файл `.env` в корневой папке и добавьте ваш токен доступа:
   ```text
   API_KEY=ваш_секретный_ключ_api
   ```

4. **Запуск тестов:**
   * Запуск всех тестов сбором данных для Allure:
     ```bash
     pytest --alluredir=allure-results
     ```
   * Просмотр отчета Allure:
     ```bash
     allure serve allure-results
     ```