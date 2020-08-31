from django.shortcuts import render
from django.views import generic
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from django.db import models as x
from maps.models import x, AdSerializer

class index(generic.TemplateView):
    template_name = 'html.html'

class AdViewSet(ReadOnlyModelViewSet):
    bbox_filter_field = 'Starbucks'
    filter_backends = (InBBoxFilter,)
    serializer_class = AdSerializer


def pass_variable(request):
    lat = x.latitude
    long = x.longitude
    starbucks_locations = x.Starbucks
    lat_long = list(zip(lat, long))
    return render(request, 'html.html', {'titles': starbucks_locations}, {'lat_long': lat_long})


def request(request):
    data = x.objects.all()
    context = {
        'starbucks_locations': data,
    }
    return render(request, 'html.html', context)
