from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Student, Faculty, AdminEmployee, HelpingStaff, Reviewer, NonReviewer


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('type', 'email', 'name', 'phone', 'nsu_id', 'nsu_card', 'is_staff', 'is_active',)
    list_filter = ('type', 'email', 'name', 'phone', 'nsu_id', 'nsu_card', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('type', 'email', 'name', 'phone', 'nsu_id', 'nsu_card')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(AdminEmployee)
admin.site.register(HelpingStaff)
admin.site.register(Reviewer)
admin.site.register(NonReviewer)
