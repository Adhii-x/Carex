from django.http import HttpResponse
import json
from .forms import Booking

def main_context(request):
    if request.method == "POST":
        form = Booking(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/json"
        )
    else:
        form = Booking()

    context = {"booking": form}
    return context