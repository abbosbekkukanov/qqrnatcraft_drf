from django.contrib import admin
from .models import Banner, Craftsmanship, Craftsmanshiplist, OurTeam, SocialMediaLink
# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'img']  # Admin panelda ko'rsatiladigan maydonlar

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'img', 'profession'] 

class CraftsmanshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'img']  # Admin panelda ko'rsatiladigan maydonlar

class CraftsmanshipListAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'img'] 

class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'icon']

admin.site.register(Craftsmanship, CraftsmanshipAdmin)
admin.site.register(Craftsmanshiplist, CraftsmanshipListAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(SocialMediaLink, SocialMediaLinkAdmin)


