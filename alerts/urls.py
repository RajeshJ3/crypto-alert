from django.urls import path
from alerts import views

urlpatterns = [
    path("sync/", views.Sync.as_view())
]
