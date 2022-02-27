from django.contrib import admin
from .models import Project, Credential, Skill

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
