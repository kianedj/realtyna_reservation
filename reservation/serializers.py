from rest_framework import serializers
from .models import Hotel, Guest, Room, Reservation
from django.core.exceptions import ValidationError
from .helper import check_reservation_ability


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)

    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        try:
            return Room.create(**validated_data)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))


class ReservationSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='room.hotel.name', read_only=True)
    guest_name = serializers.CharField(source='guest.name', read_only=True)
    room_number = serializers.CharField(source='room.room_number', read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):
        """
        Override to handel conditional model creation in POST method requests.
        :param validated_data:
        :return: created model or raise Error
        """
        try:
            return Reservation.create(**validated_data)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

    def validate(self, data):
        """
        Override to Handle conditional model update in PUT and PATCH method requests.
        :param data:
        :return: data or raise Error
        """
        if self.instance is not None:
            try:
                check_reservation_ability(id=self.instance.id, data=data)
                return data
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        else:
            return data
