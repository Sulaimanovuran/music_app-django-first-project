"""
python3 -m venv venv - создание виртуального окружения

source venv/bin/activate - активируем ВП

pip freeze - список установленных библиотек

deactivate - выйти из ВП

"""
############################################################################

'''
requirements.txt
    django
    djangorestframework
'''

############################

''' pip install -r requirements.txt'''

##################################

'''django-admin startproject name_project . -  создаем главное приложение нашего проекта'''

#####################################3

'''
a) django-admin startapp new_name_app - создаем определенное приложение
b) ./manage.py startapp new_name_app - создаем определенное приложение (v2)
'''
#########################
'''
./manage.py makemigrations - создаеь миграцию
./manage.py migrate - применяет её
./manage.py createsuperuser - создает админа
'''

#########################

'''./manage.py runserver'''