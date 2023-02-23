from django.urls import path
from accountapp.views import Hello_World

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', Hello_World, name='helloworld')
]