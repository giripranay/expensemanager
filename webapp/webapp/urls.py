from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('expensemanager/', include('expensemanager.urls')),
    path('admin/', admin.site.urls),
]
