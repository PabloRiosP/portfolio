from django.contrib import admin
from .models import Hard_Skill, Soft_Skill, Credential_Emitter, Credential, Project

@admin.register(Hard_Skill)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Soft_Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Credential_Emitter)
class CredentialEmitterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publication_date')
    list_display_links = ('id', 'name')

