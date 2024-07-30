from django.urls import path
from .views import home, SignupView,LoginView

urlpatterns = [
    path('', home, name="home"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
]





