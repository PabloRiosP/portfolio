from django.urls import path
from .views import renderProjects, renderProjectDetail, renderTest

app_name = 'projects'

urlpatterns = [
    path('', renderProjects, name='projects'),
    path('projects/<int:Id>', renderProjectDetail, name='project'),
    path('test', renderTest, name='test')
]
