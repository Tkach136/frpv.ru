# frpv

Региональный фонд развития промышленности Воронежской области

1. Слить репу к себе
$ git clone https://gitlab.com/egor_zenkin/frpv.git
2. Создать виртуальное окружение в корневой папке frpv и активировать его
$ py -m venv .venv
$ .venv\Scripts\activate 
3. Установить зависимости (библиотеки)
pip install -r freeze.txt
4. Инициализировать базу данных:
$ py manage.py migrate
(перед этим соответственно перейти в каталог с файлом manage.py с помощью $ cd project)
5. Создать суперпользователя, чтобы можно было зайти в админку
(!ВНИМАНИЕ! Процесс ввода пароля не отображается)
$ py manage.py createsuperuser
6. Основная ветка разработки - devel, в неё ничего не пушить без согласования
!!!!ДОСЛОВНО: НИКОГДА НЕ ДЕЛАЙ $ git push origin devel
7. Чекай Issue в GitLab, там найдёшь список заданий.
8. Работа с git, основные команды
$ git branch - список веток
$ git checkout <name> - перейти на ветку <name>
$ git checkout -b <name> - создать новую локальную ветку <name> и перейти на неё
$ git status - статус проекта (красным - файлы не будут внесены в коммит, зеленым - будут)
$ git add <file> - подготовить измененный файл <file> к коммиту
$ git add . - добавить все измененные файлы к будущему коммиту
$ git commit -m 'comment' - закоммитить изменения с комментарием 'comment'
$ git push origin <branch> - опубликовать локальные изменения в удалённую ветку <branch>
$ git pull origin <branch> - получить все изменения, сделанные на далённом репозитории, на свою локальную ветку
