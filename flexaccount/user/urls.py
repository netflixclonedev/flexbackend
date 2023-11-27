from django.urls import path
from . import views
urlpatterns=[
    #path("lgb",views.index,name='index'),
    #path("login/",views.login,name='login'),
    #path("signup/",views.signup,name='signup'),
    path("des/",views.des,name="des"),
    path("landingpage/",views.lpage,name="lpage"),
    path("create/",views.create,name="create"),
    path("signin1/",views.signin1,name="signin1"),
    path("signin2/",views.signin2,name="signin2"),
    path("forgot/",views.forgot,name="forgot"),
    path("otp/",views.otp,name="otp"),
    path("reset/",views.resetpassw,name="resetpassw"),
]