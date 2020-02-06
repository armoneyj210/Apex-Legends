from django.contrib import admin
from .models import Skin, Character, Attachment, WeaponType, Map, Weapon


admin.site.register([Skin, Character, Attachment, WeaponType, Map, Weapon])
