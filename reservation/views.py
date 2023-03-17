from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Guest, Hotel, Room, Reservation
from .serializers import GuestSerializer, HotelSerializer, RoomSerializer, ReservationSerializer


def html_report(request):
    """
    :param request:
    :return: report as Html in your browser.
    """
    reservations = Reservation.objects.all()
    return render(request, 'html_report.html', {'reservations': reservations})


def text_report(request):
    """
    :return: report as text file.
    """
    reservations = Reservation.objects.all()
    response = HttpResponse(content_type='text,plain')
    response['content-Disposition'] = 'attachment; file="reservations.text'
    for reservation in reservations:
        response.write(f"{reservation.guest.name} - {reservation.room} - {reservation.start_date} -"
                       f" {reservation.end_date}\n")
    return response


class GuestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class HotelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
