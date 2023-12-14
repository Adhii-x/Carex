from django.http import HttpResponse
import json
from .forms import BookingForm

def main_context(request):
    context = {"bookingform": BookingForm()}
    return context