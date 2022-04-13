
https://www.runoob.com/django/django-first-app.html

```
创建一个项目：
django-admin startproject blog
```

```
启动服务器：
python manage.py runserver
```
```
视图配置：
在blog_django_framework\blog_django_framework新建views.py,复制一下代码

from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello world ! ")