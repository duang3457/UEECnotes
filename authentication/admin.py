from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import MyUser

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    def get_post_name(self, obj):
        return obj.post.post_name if obj.post else None

    get_post_name.short_description = 'Post Name'  # 设置列的标题

    # 定义添加用户时显示的字段集
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'future_major', 'email', 'get_post_name'),
        }),
    )

    # 定义修改用户时显示的字段集
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('future_major', 'get_post_name')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'future_major', 'get_post_name')

admin.site.register(MyUser, MyUserAdmin)