from django.urls import path

from .views import ping, sleep_async, sleep_sync

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("sleep-sync/", sleep_sync, name="sleep_sync"),
    path("sleep-async/", sleep_async, name="sleep_async"),
]
