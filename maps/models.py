from django import forms
from django.contrib.gis.db import models
from leaflet.forms.fields import PointField
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class cafe_location(forms.Form):
    Name = forms.IntegerField()
    Geo = models.TextField()


class x(models.Model):
    SB = models.CharField(max_length=255)
    latitude = models.PointField()
    longitude = models.PointField()

    def __str__(self):
        return self.SB

    point = PointField()

    @property
    def lat_lon(self):
        return list(getattr(self.point, 'COORDINATES', [])[::-1])


class AdSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'SB'
        fields = ('ll',)
