from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('water_app/', include('water_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('water_app.urls')),
]
