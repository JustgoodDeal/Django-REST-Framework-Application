from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User, Project, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','due_date','project','user',)


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = ('title','get_users', 'get_tasks')

    def get_users(self, project):
        return ', '.join(project.users.values_list('username',flat=True))
    get_users.short_description = 'users'
        
    def get_tasks(self, project):
        return ', '.join(project.tasks.values_list('title',flat=True))
    get_tasks.short_description = 'tasks'      


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    inlines = [TaskInline]
    list_display = ('username','email','role','is_superuser', 'get_projects','task')
    search_fields = ('username','email','role',)
    list_filter = ('is_superuser', 'role',)
    fieldsets =  (
            (None, {'fields': ('username','email','role','password',)}),
            ('Permissions', {'fields': ('is_superuser',)}),
    )

    def get_projects(self, user):
        return ', '.join(user.projects.values_list('title',flat=True))
    get_projects.short_description = 'projects'

admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.unregister(Group)
admin.site.site_header = 'Task Manager'
