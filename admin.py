from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Ticket)
admin.site.register(Status)
admin.site.register(Statusticket)
admin.site.register(Comments)
admin.site.register(Image)