from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status

from apps.traffic.api.serializers import *


class TrafficBoroYear(generics.ListAPIView):
    """
        Tráfico por barrio y año
    """
    serializer_class = TrafficOneSerializer

    def get_queryset(self, boro=None, year=None):
        if boro and year:
            try:
                traffic_volume = self.get_serializer().Meta.model.objects.filter(year=year, boro=boro)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return traffic_volume

    def list(self, request, boro, year):
        traffic_volume = self.get_queryset(boro, year)
        data = self.get_serializer(traffic_volume, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class TrafficBoroYearMonth(generics.ListAPIView):
    """
        Tráfico por barrio, año y mes
    """
    serializer_class = TrafficOneSerializer

    def get_queryset(self, boro=None, year=None, month=None):
        if boro and year and month:
            try:
                traffic_volume = self.get_serializer().Meta.model.objects.filter(year=year, boro=boro, month=month)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return traffic_volume

    def list(self, request, boro, year, month):
        traffic_volume = self.get_queryset(boro, year, month)
        data = self.get_serializer(traffic_volume, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class TrafficBoroYearMonthHour(generics.ListAPIView):
    """
        Tráfico por barrio, año, mes y hora
    """
    serializer_class = TrafficOneSerializer

    def get_queryset(self, boro=None, year=None, month=None, hour=None):
        if boro and year and month and hour:
            try:
                traffic_volume = self.get_serializer().Meta.model.objects.filter(year=year, boro=boro, month=month, hour=hour)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return traffic_volume

    def list(self, request, boro, year, month, hour):
        traffic_volume = self.get_queryset(boro, year, month, hour)
        data = self.get_serializer(traffic_volume, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class TrafficAltBoroYearMonth(generics.ListAPIView):
    """
        Información alternativa por barrio, año y mes
    """
    serializer_class = TrafficAltSerializer

    def get_queryset(self, boro=None, year=None, month=None):
        if boro and year and month:
            try:
                traffic_volume = self.get_serializer().Meta.model.objects.filter(year=year, boro=boro, month=month)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return traffic_volume

    def list(self, request, boro, year, month):
        traffic_volume = self.get_queryset(boro, year, month)
        data = self.get_serializer(traffic_volume, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class ModelViewSet(generics.ListAPIView):
    """
        Información de barrios y sus calles
    """
    serializer_class = ModelSerializer

    def get_queryset(self):
        try:
            traffic_volume = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return traffic_volume

    def list(self, request):
        traffic_volume = self.get_queryset()
        data = self.get_serializer(traffic_volume, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)