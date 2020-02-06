from rest_framework import viewsets
from .models import Skin, Character, Attachment, WeaponType, Map, Weapon
from .serializers import SkinSerializer, AttachmentSerializer, WeaponTypeSerializer, WeaponSerializer,\
    CharacterSerializer, MapSerializer


class CharacterView(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class SkinView(viewsets.ModelViewSet):
    queryset = Skin.objects.all()
    serializer_class = SkinSerializer


class AttachmentView(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class WeaponView(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponTypeView(viewsets.ModelViewSet):
    queryset = WeaponType.objects.all()
    serializer_class = WeaponTypeSerializer


class MapView(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer