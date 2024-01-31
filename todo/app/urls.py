from django.urls import path
from django.shortcuts import HttpResponse,render
from app.views import home,login,signup,add_todo,signout,delete_todo,cong

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('add-todo/' , add_todo ),
    path('delete-todo/<int:id>' , delete_todo ),
    path('logout/',signout),
    path('signup/',signup,name="signup"),
    path('signup/cong/',cong,name="cong"),

]
