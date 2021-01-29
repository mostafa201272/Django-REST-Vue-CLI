# Django-REST-Vue-CLI
This Repo Contain a Django web application with Vue CLI


# Steps to Create Django application with Vue CLI
In this section we will create django project with django environment and create vue cli application with vue environment.

> ## [1] Django Project Setup
>> ### 1. Create Django Environment

>>> **1. Create an Isolation Area For Project (For Production)**
>>>> - command: `mkdir "Environment Folder name"`

>>> **2. Change Your current directory to the Environment directory**
>>>> - command: `cd YOUR_DIRECTORY_PATH/Environment_DIRECTORY`

>>> **3. Install The Virtual Environment**
>>>> - command: `python -m venv "Environment_DIRECTORY_PATH" `

>>> **4. Activate Environment**
>>>> - command: `YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/activate`
>>>> - ***OR***
>>>> - Change your current directory to environment Scripts Folder and activate
>>>>> 1. command: `cd YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/`
>>>>> 2. command: `activate`

>>> **5. Upgrade pip**
>>>> - command: `python -m pip install --upgrade pip`

>>> **6. Install Django**
>>>> - command: `pip install django`

>>> **7. Check the Django Version**
>>>> - command: `django-admin --version`

>>> **8. Install Django REST Framework**
>>>> - command: `pip install djangorestframework`

>>> **9. Deactivate the Virtual Environment**
>>>> - command: `deactivate`

>> ### 2. Create Django Project and add REST Framework

>>> **1. Activate Environment**
>>>> - command: `YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/activate`
>>>> - ***OR***
>>>> - Change your current directory to environment Scripts Folder and activate
>>>>> 1. command: `cd YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/`
>>>>> 2. command: `activate`

>>> **2. Change Directory to Isolated Directory to create the project**
>>>> - command: `cd "Isolated Directory"`

>>> **3. create django project**
>>>> - command: `django-admin startproject project_Name`

>>> **4. run django project**
>>>> - command: python manage.py runserver

>>> **5. Add Django REST Framework to django project**
>>>> 5.1. open `settings.py` in root project folder
>>>> 5.2. in `INSTALLED_APPS` array add the `rest_framework` and `rest_framework.authtoken`

<hr>
> ## [2] Vue CLI Project Setup
>>
