from django.core.exceptions import ValidationError

from reservation.models import Reservation


def check_reservation_ability(id, data):
    """
    :param id, data:
    :return: ValidationError if the room was earlier reserved at the requested duration time.
    """
    reservation = Reservation.objects.get(id=id)
    mem = {}
    for item in ['start_date', 'end_date', 'room']:
        if data.get(item) is not None:
            mem[item] = data.get(item)
        else:
            mem[item] = getattr(reservation, item)
    reserved = Reservation.objects.values('start_date', 'end_date').filter(room=mem['room']).exclude(id=id)
    duration = (mem['start_date'], mem['end_date'] - mem['start_date'])
    for item in reserved:
        sold_out = (item['start_date'], item['end_date'] - item['start_date'])
        if duration[0] > sold_out[0]:
            remaining_time = duration[0] - sold_out[0]
            if (sold_out[1] - remaining_time).days >= 0:
                raise ValidationError(message=f"Room number: {data.get('room')} is already "
                                              f"reserved at requested date.",
                                      code='Invalid')
        if duration[0] == sold_out[0]:
            raise ValidationError(message=f"Room number: {data.get('room')} is already "
                                          f"reserved at requested date.",
                                  code='Invalid')
        if duration[0] < sold_out[0]:
            remaining_time = sold_out[0] - duration[0]
            if (duration[1] - remaining_time).days >= 0:
                raise ValidationError(message=f"Room number: {data.get('room')} is already "
                                              f"reserved at requested date.",
                                      code='Invalid')
