from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home, name="home"),
    path('register/',views.register,name= 'register'),
    path('register1/',views.register1,name="register1"),
    path('login/',views.login,name="login"),
    path('login1/',views.login1,name="login1"),
    path('logout/',views.logout,name= "logout"),\
    path('uploadquestion/',views.uploadquestion,name= "uploadquestion"),
    path('question/', views.question, name="question"),
    path('answers/<int:id>/', views.answers,name= "answers"),
    path('points/<int:qid>/<str:email>/',views.points,name="points"),
    path('profile/',views.profile,name="profile"),
    path('follow/<int:id>/<str:email>/',views.follow,name="follow"),
    path('updateprofile/',views.updateprofile,name="updateprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('password/',views.password, name='password'),
    path('changepass/', views.changepass, name= "changepass"), 



]