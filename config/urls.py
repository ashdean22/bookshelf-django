from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include("catalog.api_urls")),
    path("books/", include("catalog.urls")),
    path("", RedirectView.as_view(url="/books/", permanent=False)),
]