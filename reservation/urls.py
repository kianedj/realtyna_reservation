from django.urls import path
from . import views

urlpatterns = [
    path('guest/', views.GuestListCreateAPIView.as_view(), name='guest-list'),
    path('guest/<int:pk>/', views.GuestRetrieveUpdateDestroyAPIView.as_view(), name='guest-detail'),
    path('hotel/', views.HotelListCreateAPIView.as_view(), name='hotel-list'),
    path('hotel/<int:pk>/', views.HotelRetrieveUpdateDestroyAPIView.as_view(), name='hotel-detail'),
    path('room/', views.RoomListCreateAPIView.as_view(), name='room-list'),
    path('room/<int:pk>/', views.RoomRetrieveUpdateDestroyAPIView.as_view(), name='room-detail'),
    path('reservation/', views.ReservationListCreateAPIView.as_view(), name='reservation-list'),
    path('reservation/<int:pk>/', views.ReservationRetrieveUpdateDestroyAPIView.as_view(),
         name='reservation-detail'),

    path("text_report/", views.text_report, name='text_report'),
    path('html_report/', views.html_report, name='html_report')
]
