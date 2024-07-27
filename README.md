<a></a>
<img src="https://img.shields.io/badge/python-3.12-gree" alt="Python version"/>
<img src="https://img.shields.io/badge/Django-5.0.7-gree" alt="Django Version"/>
<img src="https://img.shields.io/badge/Django%20REST%20framework-3.15-gree" alt="Django REST Framework Version"/>
<img src="https://img.shields.io/badge/scrapy-2.11.2-gree" alt="Scrapy Version"/>
<a href="https://documenter.getpostman.com/view/25907870/2sA3kaAxvU"><img src="https://img.shields.io/badge/API docs-latest-blue.svg" alt="API Docs"/></a>

<h1>API-сервис для получения данных об объявлениях Farpost</h1>

<hr>
<h2>Описание</h2>

<p>Проект представляет собой API-сервис для автоматизированного сбора и анализа данных об объявлениях с платформы Farpost. Основной целью является создание инструмента, позволяющего пользователям получать актуальную информацию о рынке недвижимости, товаров и услуг, представленных на Farpost, через удобный API-интерфейс. Сервис позволяет пользователям просматривать детальную информацию об объявлениях, включая статистику просмотров и позиции в выдаче.</p>

<p>Ключевыми задачами проекта являются: обеспечение сбора данных с Farpost, предоставление удобного доступа к собранной информации через API, реализация системы аутентификации для защиты данных.</p>

<h3>Функциональность сервиса:</h3>

<h4>Для пользователей API:</h4>
<ul>
  <li>Регистрация и аутентификация через API с использованием JWT токенов.</li>
  <li>Получение списка всех собранных объявлений.</li>
  <li>Получение детальной информации о конкретном объявлении по его ID.</li>
</ul>

<h4>Для администраторов системы:</h4>
<ul>
  <li>Управление процессом сбора данных: запуск и остановка Scrapy парсера.</li>
  <li>Мониторинг состояния системы и процесса сбора данных.</li>
  <li>Управление объявлениями (создание, редактирование, удаление).</li>
</ul>

<h3>Технические особенности:</h3>
<ul>
  <li>Использование Django и Django REST Framework для создания API.</li>
  <li>Применение Scrapy для эффективного сбора данных с Farpost.</li>
  <li>Реализация JWT-аутентификации для безопасного доступа к API.</li>
  <li>Управление количеством объявлений осуществляется через settings.MAX_COUNT_ADS.</li>
</ul>


<h3><a href="https://documenter.getpostman.com/view/25907870/2sA3kaAxvU">API Документация (Postman)</a></h3>

<hr>

<h2>Запуск проекта</h2>

<ol>
  <li>Клонируйте репозиторий:
    <pre><code>git clone https://github.com/Edmaroff/farpost-ads-api</code></pre>
  </li>
  <li>Перейдите в директорию проекта:
    <pre><code>cd farpost-ads-api/app/</code></pre>
  </li>
  <li>Установите и активируйте виртуальное окружение для проекта <code>venv</code>:
    <details open>
      <summary>Windows</summary>
      <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
    </details>
    <details open>
      <summary>Linux/macOS</summary>
      <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
    </details>
  </li>
  <li>Установите зависимости из <code>requirements.txt</code>:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Выполните миграции:
    <pre><code>python manage.py migrate</code></pre>
  </li>
  <li>*Опционально: cоздайте и заполните файл <code>.env</code> по шаблону <code>.env.template</code>.</li>
  <li>Запустите парсинг данных:
    <pre><code>python manage.py crawl_farpost</code></pre>
  </li>
  <li>Запустите сервер:
    <pre><code>python manage.py runserver</code></pre>
     Список эндпоинтов - <a href="https://documenter.getpostman.com/view/25907870/2sA3kaAxvU">API Документация (Postman)</a>
  </li>
</ol>
<hr>
