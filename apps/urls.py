from django.urls import path, include

urlpatterns = [
    path('user/', include('users.urls')),
    path('company/', include('company.urls'))
]
