from django.urls import path, include


urlpatterns = [
    path("backend/api/", include("api.urls")),
]
