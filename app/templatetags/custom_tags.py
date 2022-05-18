from atexit import register
from django import template

from app.models import Availability, Hospital

register=template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    return 'bg-danger'


@register.simple_tag
def get_availabilitys(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')


@register.simple_tag
def is_option_selected(selected_option_id, pk):
    if selected_option_id == str(pk):
        return 'selected'
    return ''


