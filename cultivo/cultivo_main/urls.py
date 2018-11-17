from django.urls import path,include
from . import views
from django.conf.urls import url
from django.views import generic


app_name="cultivo_main"    #called namespacing of urls,,,so as to distinguish between similar named urls 				#of different apps
urlpatterns=[
    path(r'',views.TemplateView.as_view(),name="home"),
    # path(r'contactus',views.TemplateView_con.as_view(),name="contact"),

    path(r'result',views.work,name="result"),
    # path(r'form_signin',views.)
    # path('upload',views.upload,name="upload"),
]