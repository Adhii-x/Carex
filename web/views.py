from django.http import HttpResponse
import json
from django.shortcuts import render,get_object_or_404,redirect
from .models import About,Service,Work,Testimonial,Team,Blog
from .forms import Booking,ContactForm


# Create your views here.

def index(request):
    abouts = About.objects.all()
    services = Service.objects.all()
    works = Work.objects.all()
    testimonials = Testimonial.objects.all()
    team_members = Team.objects.all()
    blogs = Blog.objects.all()

    context = {
        "is_index": True,
        "abouts": abouts,
        "services": services,
        "works": works,
        "testimonials": testimonials,
        "team_members": team_members,
        "blogs": blogs,
    }
    return render(request, "web/index.html", context)





def about(request):
    abouts = About.objects.all()
    context = {
        "is_index": True,
        "abouts": abouts,
        }
    return render(request, "web/about.html", context)

def services(request):
    services = Service.objects.all()
    context = {
        "is_services": True ,
        "services": services,
        }
    return render(request, "web/services.html", context)

def service_detail(request,slug):
    selected_service = Service.objects.get(slug=slug)
    service=Service.objects.all()
    context={
            "selected_service": selected_service,
            "services": service,
            }
    return render(request,'web/service-details.html',context)


def pricing(request):
     context = {
         "is_pricing": True
         }
     return render(request, "web/pricing.html", context)


def team_detail(request, slug):
    team_members = get_object_or_404(Team, slug=slug)
    fields = ['biography', 'education', 'awards']  # Add more fields as needed
    context = {
        "team_members": team_members,
        "fields": fields,
    }
    return render(request, 'web/team-details.html', context)


def blog(request):
     blogs = Blog.objects.all()
     context = {
         "is_services": True,
          "blogs": blogs,
         }
     return render(request, "web/blog.html", context)


def blog_detail(request, slug):
    blogs = get_object_or_404(Blog, slug=slug)
    context = {
        "blogs": blogs,
    }
    return render(request, "web/blog-details.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the valid form data (e.g., save to the database)
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
        form = ContactForm()
    context = {"contact": form}
    return render(request, "web/contact.html", context)
