


from django.urls  import path
from.views import RegisterView, LoginView


urlpatterns = [
    path('',RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='register')

]
