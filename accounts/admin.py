from django.contrib import admin
from accounts.models import UserProfile

admin.site.register(UserProfile)

admin.site.site_header = 'Administration'

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user')

	def user_info(self, obj):
		return obj.bio

