from django.contrib import admin
from django.urls import path
from django.shortcuts import render, HttpResponse, redirect

def login(request):  # login函数
    if request.method == "GET":  # 前端如果是get请求
        return render(request, 'login.html')  # 返回HTML页面。
    elif request.method == "POST":  # 前端如果是post请求
        username = request.POST.get("username")  # 获取POST请求中的username值
        password = request.POST.get("password")  # 获取密码值
        if username == "zy" and password == "12345":
            return redirect("/index/")    #重定向到index页面
        else:  # 如果用户名或者密码错误，返回登录页面
            return render(request, "login.html")


def index(request):  # index函数
    return render(request, "index.html")