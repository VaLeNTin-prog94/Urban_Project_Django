# Доска объявлений на Django
## Содержание
Фреймворк Django предоставляет много возможностей для создания веб-приложений. У него есть встроенные модули с различным функционалом.
В данном проектк используется рендеринг шаблонов, авторизация и регистрация пользователей.
Можно создавать новых пользователей, добавлять новые объявления и просматривать существующие.
### Для запуска проекта после установки зависимостей с помощью
```
pip install -r requirements.txt
```
### Нужно перейти в директорию 
```
cd urban_project
```
### Запустить проект:
```
python manage.py runserver
```
### Вид доски объявлений до авторизации:
![image](https://github.com/user-attachments/assets/b2b77a02-755f-4763-a7cb-32a65eaaf4b8)
![image](https://github.com/user-attachments/assets/50b6bf76-4099-4b92-ab99-be09bc7fbc7c)
### Вид доски объявлений после авторизации:
![image](https://github.com/user-attachments/assets/2c3e8323-cf83-40d0-be20-7249488d04d2)
![image](https://github.com/user-attachments/assets/050fa0fd-7c8b-4bd3-b554-15c9f0497584)
### Отдельное объявление
![image](https://github.com/user-attachments/assets/214a6fa8-c25e-4333-ba67-68f31098eee9)
### Структура проекта
![image](https://github.com/user-attachments/assets/4b7318bd-3b2b-46ff-86db-0fddc9157b77)
## Описание файлов и их функционала
db.sqlite3: Файл базы данных SQLite, где хранятся все данные приложения, включая пользователей и объявления.
manage.py: Утилита командной строки Django для управления проектом (например, запуск сервера, создание миграций).
### Команда для запуска сервера:
```
python manage.py runserver
```
### Приложение board:
- admin.py: Файл для настройки административной панели Django для моделей приложения.
- apps.py: Конфигурация приложения board.
- forms.py: Определения форм Django, используемых для ввода данных пользователем (например, добавление и редактирование объявлений).
- models.py: Определения моделей Django, представляющих структуру данных приложения (например, модель объявления).
- tests.py: Файл для написания тестов для приложения.
- urls.py: Определения URL-адресов для приложения board, связывающие URL-адреса с представлениями.
- views.py: Определения представлений Django, содержащие логику обработки запросов пользователя.
- migrations/: Директория с файлами миграций, автоматически генерируемыми Django для применения изменений в базе данных.
- templates/board: Шаблоны HTML для отображения страниц приложения board.
### Корневая директория templates:
- base.html: Базовый шаблон, от которого наследуются другие шаблоны. Обычно содержит общую разметку страницы (например, навигационную панель).
- home.html: Шаблон домашней страницы проекта.
- registration/login.html: Шаблон страницы входа для пользователей.
### Приложение urban_project:
- asgi.py и wsgi.py: Точки входа для ASGI- и WSGI-совместимых веб-серверов соответственно.
- settings.py: Настройки проекта Django, включая конфигурацию базы данных, приложений, middleware и т.д.
- urls.py: Корневой маршрутизатор проекта, включающий маршруты из приложений.
## Работа компоненотов
### Templates
Шаблоны (templates) в Django используются для генерации HTML кода. В обычном HTML коде ставятся специальные теги шаблонизатора Django {% %} для выполнения логики на стороне сервера (например, циклы и условия) и переменные {{ }}, 
которые заменяются на значения, переданные из представлений.
### Namespace
Пространства имен (namespace) URL-адресов позволяют группировать URL-адреса по приложениям и избегать конфликтов имен.
app_name = 'board' в board/urls.py позволяет ссылаться на URL-адреса с использованием этого пространства имен.
Например, определенную в board/urls.py ссылку advertisement_list можно указывать в шаблонах как 'board:advertisement_list'.
### URLs
В Django URL-конфигурации определяются в файлах urls.py каждого приложения и корневого проекта. Эти конфигурации связывают URL-адреса с представлениями (views), которые должны обрабатывать запросы к этим адресам.
### Views
Представления (views) в Django принимают веб-запросы и возвращают веб-ответы. Они взаимодействуют с моделями для выполнения операций с базой данных (например, получение, добавление или изменение данных) и передают результаты шаблонам для отображения.
### Settings
Файл settings.py содержит конфигурацию проекта Django, включая настройки базы данных, настройки безопасности, зарегистрированные приложения, настройки статических файлов и многое другое.
Использование шаблонов и настройка URL-адресов
Шаблоны используют контекстные переменные и теги шаблонизатора для динамического генерирования HTML. Создаваемый контекст в представлениях передается в шаблоны, где он используется для отображения данных.
Пример использования переменной контекста: {{ advertisement.title }} для отображения заголовка объявления.
URL-адреса настраиваются с помощью регулярных выражений или путей (paths), которые определяют, какой шаблон URL соответствует определенному представлению. Использование аргументов в URL-адресах, таких как <pk>, позволяет передавать значения в представления для обработки запросов к конкретным объектам (например, к определенному объявлению).
