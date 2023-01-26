
from django.contrib import admin
from django.urls import path
from crm.views import auth_admin, today




urlpatterns = [
    path('admin/', admin.site.urls),
    path('authorization/', auth_admin),
    path('index/', auth_admin),
    path('start/', today),

    

]
