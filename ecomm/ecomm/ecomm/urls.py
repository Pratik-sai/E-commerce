
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('od_app/',include(('od_app.urls','od_app'), namespace='od_app')),
]
