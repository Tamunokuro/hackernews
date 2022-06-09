from django.contrib import admin
from .models import Story, Job, Comment

admin.site.site_header = 'HACKERNEWS APP'
admin.site.site_title = 'HACKERNEWS APP'
admin.site.index_title = 'HACKERNEWS APP'

# Register your models here.
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['author','title','story_link','item_type','created']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_title','job_link', 'job_poster', 'created']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['commenter', 'item_type', 'comment', 'created']