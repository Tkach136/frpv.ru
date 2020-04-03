1. Слить репозиторий к себе
$ git clone https://gitlab.com/egor_zenkin/frpv.git

2. Создать виртуальное окружение в корневой папке frpv и активировать его
$ py -m venv .venv

$ .venv\Scripts\activate 
3. Установить зависимости (библиотеки)
pip install -r freeze.txt

4. Инициализировать базу данных:
$ py manage.py migrate
$ py manage.py createsuperuser // создаём суперпользователя
( В корне лежит архив всех данных и сама бд на всякий случай, если удобнее так. superuser: admin, Pushkin1)

5. Основная ветка разработки - devel, в неё ничего не пушить без согласования (Merge Request).

6. Чекай Issue в GitLab, там найдёшь список заданий. Название ветки - согласно номеру Issue (Issue #7 => git branch fix#7)