from django.contrib import admin

from travel.models import City, CityImages, Blog

admin.site.register(City)
admin.site.register(Blog)
admin.site.register(CityImages)