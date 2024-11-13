from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view

from rest_framework.response import Response
from catalogue.models import Prices, Shows
from catalogue.serializers import PricesSerializer, ShowSerializer

from rest_framework import generics
from catalogue.models import Prices
from catalogue.serializers import PricesSerializer
from catalogue.views import group_required


class ShowListView(generics.ListAPIView):
    queryset = Shows.objects.all()
    serializer_class = ShowSerializer


@method_decorator(group_required('Admin'), name='dispatch')
class PricesListCreateView(generics.ListCreateAPIView):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer


def prices_by_show(request, show_id):
    # Récupérer le spectacle correspondant à show_id
    show = get_object_or_404(Shows, id=show_id)

    # Récupérer les tarifs associés à ce spectacle
    prices = Prices.objects.filter(shows=show)

    # Renvoyer les informations au template
    return render(request, 'prices_by_show.html', {'show': show, 'prices': prices})
