from django.urls import path
from .views import renderHome, renderProject

app_name = 'projects'

urlpatterns = [
    path('', renderHome, name='home'),
    path('projects/<int:Id>', renderProject, name='project'),
]
