#### < project_05 >



190215 | Django + Bootstrap 페이지 구현

MY_PROJECT/        
​    **project_05/**
​        templates/
​            base.html
​        __init__.py            
​        settings.py           

​        urls.py            
​        wsgi.py        
​    **detail/**
​        static/
​            detail/
​                images/
​                    ...
​                stylesheets/
​                    style.css
​        templates/                
​            detail/
​                index.html
​                mypage.html
​                not_found.html
​                qna.html
​                signup.html
​        __init__.py            
​        admin.py
​        apps.py            
​        models.py            
​        tests.py            
​        urls.py            
​        views.py       
​    manage.py        
​    README.md
​            
​            
< MY_PROJECT final structure >
(my_project) chelseashin:~/workspace/MY_PROJECT $ tree
.
├── db.sqlite3
├── **detail**
│   ├── init.py
│   ├── pycache
│   │   ├── init.cpython-36.pyc
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── init.py
│   │   └── pycache
│   │       └── init.cpython-36.pyc
│   ├── models.py
│   ├── static
│   │   └── detail
│   │       ├── images
│   │       │   ├── back.jpg
│   │       │   ├── background.jpg
│   │       │   ├── in-love.png
│   │       │   ├── original.png
│   │       │   ├── snoopy.jpg
│   │       │   ├── snoopy2.png
│   │       │   └── sss.png
│   │       └── stylesheets
│   │           └── style.css
│   ├── templates
│   │   └── detail
│   │       ├── index.html
│   │       ├── mypage.html
│   │       ├── not_found.html
│   │       ├── qna.html
│   │       └── signup.html
│   ├── tests.py
│   └── views.py
├── manage.py
└── **project_05**
​    ├── init.py
​    ├── pycache__
​    │   ├── init.cpython-36.pyc
​    │   ├── settings.cpython-36.pyc
​    │   ├── urls.cpython-36.pyc
​    │   └── wsgi.cpython-36.pyc
​    ├── settings.py
​    ├── templates
​    │   └── base.html
​    ├── urls.py
​    └── wsgi.py