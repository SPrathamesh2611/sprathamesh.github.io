from django.contrib import admin
from resume.models import Skill,Project,ContactMessage

# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactMessage)