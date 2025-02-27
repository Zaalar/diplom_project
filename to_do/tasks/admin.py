from django.contrib import admin

from tasks.models import Category, Priority, Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
   pass

@admin.register(Category)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Priority)
class TaskAdmin(admin.ModelAdmin):
    pass


