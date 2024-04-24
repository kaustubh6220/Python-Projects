# urls.py
from django.urls import path
from login import views

urlpatterns = [
    
    path('', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('adminlogin.html', views.studentlogin, name='studentlogin'),
    path('admindashboard.html', views.admindashboard_view, name='admindashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('catagory.html', views.catagory, name='catagory'),
    path('studentdata.html', views.studentdata, name='studentdata'),
    path('halldata.html', views.halldata, name='halldata'),
    path('stusemI.html', views.stusemI, name='stusemI'),
    path('stusemII.html', views.stusemII, name='stusemII'),
    path('stusemIII.html', views.stusemIII, name='stusemIII'),
    path('stusemIV.html', views.stusemIV, name='stusemIV'),
    path('stusemV.html', views.stusemV, name='stusemV'),
    path('stusemVI.html', views.stusemVI, name='stusemVI'),
    path('stusemVII.html', views.stusemVII, name='stusemVII'),
    path('stusemVIII.html', views.stusemVIII, name='stusemVIII'),
    path('semIstudata', views.semIstudata, name='semIstudata'),  
    path('deletesemIstu', views.deletesemIstu, name='deletesemIstu'), 
    path('uploadhalldata', views.uploadhalldata, name='uploadhalldata'),  
    path('deletehall', views.deletehall, name='deletehall'),   
    path('I_additional.html', views.I_additional, name='I_additional'),
    path('hallreport.html', views.hallreport, name='hallreport'),
    path('semIhallreport', views.semIhallreport, name='semIhallreport'),
    # path('hall_view.html', views.hall_view, name='semIhallreport'),
]
