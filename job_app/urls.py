from django.urls import path
from . import views
app_name = 'job_app'

urlpatterns=[
    path('',views.home,name='home'),
]
