该仓库仅为测试demo

# 1. 开发环境

* Windows 10专业版 版本21H2（操作系统内部版本 19044.1645）
* Python 3.10.4
* Pycharm Professional 2021.3.3
* Django 4.0.4
* SQLite3

# 2. 创建项目

1. 安装Django：
    ```bash
    pip install django
    ```
2. 创建Django项目：
    ```bash
    django-admin.exe startproject bms
    ```
3. 创建Django项目里的App：
    ```bash
    python .\manage.py startapp app
    ```
4. 初始化数据库：
    ```py
    py.exe .\manage.py makemigrations
    py.exe .\manage.py migrate
    ```

# 3. 启动项目

1. 安装Django：
    ```bash
    pip install django
    ```
2. 启动Django服务，先进入`bms`目录，然后执行：
    ```bash
    python .\manage.py runserver
    ```
    或者直接双击运行`bms`目录里的`runserver.bat`

# 4. 使用项目

1. 插入50万条数据：
http://127.0.0.1:8000/init_database

2. 获取第几页的数据（page是页数，size是每页展示多少条数据）：
http://127.0.0.1:8000/get_books_info?page=1&size=20
