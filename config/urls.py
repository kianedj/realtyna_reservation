from django.urls import path, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("docs/", include_docs_urls(title="Reservation API title", public=False)),
    path('', include("reservation.urls")),
]
