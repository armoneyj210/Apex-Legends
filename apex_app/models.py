from django.db import models


class Map(models.Model):
    name = models.CharField(max_length=30)
    map_url = models.TextField

    def __str__(self):
        return self.name


class WeaponType(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField

    def __str__(self):
        return self.name


class Attachment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=30)
    weapon_type = models.ForeignKey(WeaponType, on_delete=models.CASCADE, related_name='weapon_types')
    ammo = models.CharField(max_length=20)
    attachments = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='weapon_attachments')
    image_url = models.TextField

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=20)
    passive_ability = models.CharField(max_length=30)
    ability = models.CharField(max_length=30)
    super = models.CharField(max_length=30)
    image_url = models.TextField
    background = models.TextField
    skin = models.CharField(max_length=200)
    kills = models.IntegerField

    def __str__(self):
        return self.name


class Skin(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.TextField
    character = models.ForeignKey(on_delete=models.CASCADE, related_name='skins')

    def __str__(self):
        return self.name
