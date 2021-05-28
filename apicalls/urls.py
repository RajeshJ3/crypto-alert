from django.urls import path
from apicalls import views

urlpatterns = [
    path("", views.APICall.as_view())
]
