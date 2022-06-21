from django.contrib import admin

from main.models import List, Task


@admin.register(List)
class ListModel(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )


@admin.register(Task)
class TaskModel(admin.ModelAdmin):
    list_filter = ('text', )
    list_display = ('text', )


