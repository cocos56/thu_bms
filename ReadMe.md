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

# 3. 启动项目

1. 安装Django：
    ```bash
    pip install django
    ```
2. 初始化数据库：
    ```py
    py .\manage.py makemigrations
    py .\manage.py migrate
    ```
2. 启动Django服务，先进入`bms`目录，然后执行：
    ```bash
    python .\manage.py runserver
    ```
    或者直接双击运行`bms`目录里的`runserver.bat`

# 4. 使用项目

## 4.1. 初始化数据库
初始化50万条图书信息
* Method: 不限，GET、POST、HEAD、OPTIONS、PUT、PATCH、DELETE、TRACE 和 CONNECT这九种方法都可以
* URL: http://127.0.0.1:8000/init_database
## 4.2. 增
新增一条图书信息
* Method: POST
* URL: http://127.0.0.1:8000/books_info
* Body: 
{
    "name":"三国演义",
    "author":"罗贯中",
    "publisher":"人民文学出版社",
    "price":39.5,
    "number":50
}
## 4.3. 删
删除一条图书信息
* Method: DELETE
* URL: http://127.0.0.1:8000/books_info
* Body: 
{
    "id":500001
}
## 4.4. 改
更改一条图书信息
* Method: PUT
* URL: http://127.0.0.1:8000/books_info
* Body: 
{
    "id":1,
    "name":"三国演义",
    "author":"罗贯中",
    "publisher":"人民文学出版社",
    "price":39.5,
    "number":50
}
## 4.5. 查
查询一页的N条图书信息
获取第几页的数据（page是页数，size是每页展示多少条数据）：
* Method: GET
* URL: http://127.0.0.1:8000/books_info?page=1&size=20
