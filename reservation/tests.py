from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import Guest, Hotel, Room, Reservation
from datetime import date


class GuestTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('reservation.urls'))
    ]

    def setUp(self):
        Guest.objects.create(name='kian')
        Hotel.objects.create(name='california')
        Room.objects.create(room_number=119, hotel=Hotel.objects.get(name='california'))
        Reservation.objects.create(guest=Guest.objects.get(id=1),
                                   room=Room.objects.get(id=1),
                                   start_date=date(2023, 6, 1),
                                   end_date=date(2023, 6, 10))
        Reservation.objects.create(guest=Guest.objects.get(id=1),
                                   room=Room.objects.get(id=1),
                                   start_date=date(2023, 6, 20, ),
                                   end_date=date(2023, 6, 30))

    def test_list_create_guest(self):
        url = reverse('guest-list')
        data = {'name': 'kian'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'kian')

    def test_list_get_guest(self):
        url = reverse('guest-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_guest(self):
        url = reverse('guest-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'kian')

    def test_detail_put_guest(self):
        url = reverse('guest-detail', kwargs={'pk': 1})
        data = {'name': 'tom'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'tom')

    def test_detail_patch_guest(self):
        url = reverse('guest-detail', kwargs={'pk': 1})
        data = {'name': 'sam'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'sam')

    def test_detail_delete_guest(self):
        url = reverse('guest-detail', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_post_hotel(self):
        url = reverse('hotel-list')
        data = {'name': 'paradise'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'paradise')

    def test_list_get_hotel(self):
        url = reverse('hotel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_hotel(self):
        url = reverse('hotel-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_put_hotel(self):
        url = reverse('hotel-detail', kwargs={'pk': 1})
        data = {'name': 'hilton'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'hilton')

    def test_detail_patch_hotel(self):
        url = reverse('hotel-detail', kwargs={'pk': 1})
        data = {'name': 'ibis'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'ibis')

    def test_detail_delete_hotel(self):
        url = reverse('hotel-detail', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_post_room(self):
        url = reverse('room-list')
        data = {'room_number': 109, 'hotel': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_get_room(self):
        url = reverse('room-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_room(self):
        url = reverse('room-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_put_room(self):
        url = reverse('room-detail', kwargs={'pk': 1})
        data = {'room_number': 106, 'hotel': 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['room_number'], 106)

    def test_detail_patch_room(self):
        url = reverse('room-detail', kwargs={'pk': 1})
        data = {'room_number': 201}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['room_number'], 201)

    def test_detail_delete_room(self):
        url = reverse('room-detail', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_post_reservation(self):
        url = reverse('reservation-list')
        data = {'guest': 1,
                'room': 1,
                'start_date': date(2023, 4, 1),
                'end_date': date(2023, 4, 25)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['guest'], 1)
        self.assertEqual(response.data['room'], 1)
        self.assertEqual(response.data['start_date'], '2023-04-01')
        self.assertEqual(response.data['end_date'], '2023-04-25')

    def test_list_get_reservation(self):
        url = reverse('reservation-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_reservation(self):
        url = reverse('reservation-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_put_reservation(self):
        url = reverse('reservation-detail', kwargs={'pk': 1})
        data = {'guest': 1,
                'room': 1,
                'start_date': date(2020, 4, 1),
                'end_date': date(2020, 4, 24)}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['end_date'], '2020-04-24')

    def test_detail_patch_reservation(self):
        url = reverse('reservation-detail', kwargs={'pk': 1})
        data = {'start_date': date(2023, 4, 6)}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['start_date'], '2023-04-06')

    def test_detail_delete_reservation(self):
        url = reverse('reservation-detail', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_post_reservation_condition(self):
        url = reverse('reservation-list')
        data = {'guest': 1,
                'room': 1,
                'start_date': date(2023, 6, 5),
                'end_date': date(2023, 6, 15)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0][2:-2], 'Room number: 119 in california is already reserved at '
                                                 'requested date.')

    def test_detail_put_reservation_condition(self):
        url = reverse('reservation-detail', kwargs={'pk': 1})
        data = {'guest': 1,
                'room': 1,
                'start_date': date(2023, 6, 25),
                'end_date': date(2023, 6, 29)}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["non_field_errors"][0][2:-2], 'Room number: 119 in california is already '
                                                                     'reserved at requested date.')

    def test_detail_patch_reservation_condition(self):
        url = reverse('reservation-detail', kwargs={'pk': 1})
        data = {'start_date': date(2023, 6, 25),
                'end_date': date(2023, 6, 29)}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
