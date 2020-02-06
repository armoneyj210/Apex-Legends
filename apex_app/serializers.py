from rest_framework import serializers
from .models import Skin, Character, Attachment, WeaponType, Map, Weapon


class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = '__all__'


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class WeaponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponType
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):
    weapon_types = WeaponTypeSerializer(many=True, read_only=True)
    weapon_attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Weapon
        fields = 'name', 'ammo', 'image_url, weapon_types, weapon_attachments'


class CharacterSerializer(serializers.ModelSerializer):
    skins = SkinSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = 'name', 'passive_ability', 'ability', 'super', 'image_url', 'background', 'skins', 'kills'