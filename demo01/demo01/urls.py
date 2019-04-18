"""demo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('booktest/', include('booktest.urls', namespace='booktest'))
]

"""
项目URL
urlpatterns 列表将路由与视图绑定在一起
"""

"""
去除硬编码

1、在应用urls.py添加app_name
2、在项目urls配置文件中 在include中添加命名空间
3、在应用配置文件中给url设置名字
4、在HTML中取出硬编码 {% url '命名空间:url名字' 参数 %}

"""



