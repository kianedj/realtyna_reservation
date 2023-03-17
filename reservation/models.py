from django.db import models
from django.core.exceptions import ValidationError


class Guest(models.Model):
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return f"{self.name}"


class Hotel(models.Model):
    name = models.CharField(max_length=255,
                            blank=False,
                            unique=True)

    def __str__(self):
        return f"Hotel name: {self.name}"


class Room(models.Model):
    room_number = models.IntegerField()
    hotel = models.ForeignKey(Hotel,
                              blank=False,
                              on_delete=models.CASCADE)

    @classmethod
    def create(cls, **validated_data):
        room = Room.objects.filter(hotel=validated_data.get('hotel'),
                                   room_number=validated_data.get('room_number'))
        if len(room) is not 0:
            raise ValidationError(f"You already have room No. {validated_data.get('room_number')} "
                                  f"at {validated_data.get('hotel')}.")
        return cls.objects.create(**validated_data)

    def __str__(self):
        return f"{self.room_number} in {self.hotel.name}"


class Reservation(models.Model):
    guest = models.ForeignKey(Guest,
                              blank=False,
                              on_delete=models.CASCADE)
    room = models.ForeignKey(Room,
                             blank=False,
                             on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    @classmethod
    def create(cls, **validated_data):
        """
        if the room is already reserved it will raise validation error, Conditional creation for this model,
        it's going to create reservation except the room requested was reserved at the required time duration.
        note: it supposed to reject reservation at the same days of entrance and exit compare to another reservation,
        in case you needed to accept this situation just change '>=' to '>' and '<=' to '<'.
        :param validated_data:
        :return: ValidationError or Object
        """
        reserved = Reservation.objects.values('start_date', 'end_date').filter(room=validated_data.get('room'))
        duration = (validated_data.get('start_date'), validated_data.get('end_date') - validated_data.get('start_date'))

        for item in reserved:
            sold_out = (item['start_date'], item['end_date'] - item['start_date'])
            if duration[0] > sold_out[0]:
                remaining_time = duration[0] - sold_out[0]
                if (sold_out[1] - remaining_time).days >= 0:
                    raise ValidationError(message=f"Room number: {validated_data.get('room')} is already "
                                          f"reserved at requested date.",
                                          code='Invalid')
            if duration[0] == sold_out[0]:
                raise ValidationError(message=f"Room number: {validated_data.get('room')} is already "
                                      f"reserved at requested date.",
                                      code='Invalid')

            if duration[0] < sold_out[0]:
                remaining_time = sold_out[0] - duration[0]
                if (duration[1] - remaining_time).days >= 0:
                    raise ValidationError(message=f"Room number: {validated_data.get('room')} is already "
                                          f"reserved at requested date.",
                                          code='Invalid')

        return cls.objects.create(**validated_data)

    def __str__(self):
        return f"{self.guest.name} has reserved room No. {self.room.room_number} from {self.start_date} to" \
               f" {self.end_date}"
