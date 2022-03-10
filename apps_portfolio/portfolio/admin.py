from django.contrib import admin
from .models import Skill_Type, Skill, Credential_Type, Credential, Project

@admin.register(Skill_Type)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Credential_Type)
class CredentialTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')

