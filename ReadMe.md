该仓库仅为测试demo

使用Python3+Django+SQLite3实现：
```bash
pip install django
django-admin.exe startproject bms
python .\manage.py startapp app
```

先初始化数据库：
```py
py.exe .\manage.py makemigrations
py.exe .\manage.py migrate
```
再插入50万条数据
http://127.0.0.1:8000/init_database

获取第几页的数据（page是页数，size是每页展示多少条数据）：
http://127.0.0.1:8000/get_books_info?page=1&size=20
