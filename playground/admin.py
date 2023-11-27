from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Topic

class TopicAdmin(MPTTModelAdmin):
    list_display = ('title', 'tree_actions', 'indented_title')
    list_display_links = ('indented_title',)

admin.site.register(Topic, TopicAdmin)