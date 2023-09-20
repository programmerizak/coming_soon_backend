from django.contrib import admin
from .models import Service, Subscriber



class SubscriberAdmin(admin.TabularInline):
	model = Subscriber
	extra = 0
	fields = ['email','active','created']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['service_name','service_url','no_subscribers','active','created']
	inlines = [SubscriberAdmin,]





# # admin.py in your app
# from django.contrib import admin
# from .models import Service, Subscriber

# class SubscriberAdmin(admin.TabularInline):
#     model = Subscriber
#     extra = 0
#     fields = ['email', 'created']  # Include the 'created' field in the inline


# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ['service_name', 'service_url', 'active', 'created']
#     inlines = [SubscriberAdmin]


# @admin.register(Subscriber)
# class SubscriberModelAdmin(admin.ModelAdmin):
#     list_display = ['email', 'service', 'active', 'created']  # Add 'created' to list_display
#     list_filter = ['service', 'active']
#     search_fields = ['email']
