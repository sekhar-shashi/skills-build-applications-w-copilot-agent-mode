from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username', 'team', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'team')
    search_fields = ('email', 'username')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'team')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
