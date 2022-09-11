from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _


from .models import User,Province,UserProfile,Device

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None,{"fields":("username","password")}),
        (_("personal info"),{"fields":("first_name","last_name","phone_number","email")}),
        (_("permissions"),{"fields":("is_active","is_staff","is_superuser","groups","user_permissions")}),
        (_("important dates"),{"fields":("last_login","date_joined")}))
    add_fieldsets =(
        (None,{
            'classes':('wide'),
            'fields':('username','phone_number','password1','password2')}))
    list_display = ('username','phone_number','email','is_staff')
    search_fields = ('username__exact',)
    ordering = ('-id',)
    def get_search_results(self, request, queryset, search_term):
        queryset,may_have_duplicates=super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int=int(search_term)
        except ValueError:
            pass
        else:
            queryset=self.model.objects.filter(phone_number=search_term_as_int)
        return queryset,may_have_duplicates

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "gender", "province"]
    list_filter = ["user"]
    search_fields = ["province"]

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id","user", "device_type", "device_os","device_model","app_version","created_time"]
    list_filter = ["user"]
    search_fields = ["user","device_type",""]

admin.site.unregister(Group)
admin.site.register(Province)
admin.site.register(User,MyUserAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Device,DeviceAdmin)




