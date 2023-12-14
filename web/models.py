from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.

class About(models.Model):
    # service = models.ForeignKey("web.Service", on_delete=models.CASCADE)
    about_title = models.CharField(max_length=200,blank=True,null=True,verbose_name='Title name')
    about_image = models.ImageField(upload_to="work/",blank=True,null=True)
    about_content = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = ('About')
        verbose_name_plural = ('Abouts')

    def __str__(self):
        return str(self.about_title)    

class Service(models.Model):
    service_name = models.CharField(max_length=50,blank=True,null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    service_image = models.ImageField(upload_to="services/",blank=True,null=True)
    service_content = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = ('Service')
        verbose_name_plural = ('Services')

    def __str__(self):
        return str(self.service_name)
    
class Work(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True,verbose_name='Title name')
    work_content = models.TextField()
    order_num = models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = ('Work')
        verbose_name_plural = ('Works')

    def __str__(self):
        return str(self.title)
    
class Testimonial(models.Model):
    testimonial_image = models.ImageField(upload_to="testimonial_image/")
    testimonial_name = models.CharField(max_length=120,blank=True,null=True)
    position = models.CharField(max_length=120,blank=True,null=True)
    testimonial_content  = models.TextField()

    class Meta:
        verbose_name = ('Testimonial')
        verbose_name_plural = ('Testimonials')

    def __str__(self):
        return str(self.testimonial_name)
    
class Team(models.Model):
    member_name = models.CharField(max_length=50,blank=True,null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    member_image = models.ImageField(upload_to="services/",blank=True,null=True)
    member_position = models.CharField(max_length=50,blank=True,null=True)
    member_email = models.CharField(max_length=100,blank=True,null=True)
    about_title = models.CharField(max_length=100,blank=True,null=True)
    about_content = models.TextField(blank=True,null=True)
    education_content = models.TextField(blank=True,null=True)
    awards_content = models.TextField(blank=True,null=True)
    biography_content = models.TextField(blank=True,null=True)
    facebook_link = models.URLField(blank=True,null=True)
    youtube_link = models.URLField(blank=True,null=True)
    instagram_link = models.URLField(blank=True,null=True)

    class Meta:
        verbose_name = ('Team')
        verbose_name_plural = ('Teams')
     
    def __str__(self):
        return str(self.member_name)


class Blog(models.Model):
    user = models.CharField(max_length=120,blank=True,null=True)
    user_image = models.ImageField(upload_to="blog/")
    date = models.DateField(default=timezone.now)
    sub_title = models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    image = models.ImageField(upload_to="blog/")
    second_image = models.ImageField(upload_to="blog/")
    content = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = ('Blog')
        verbose_name_plural = ('Blogs')

    def __str__(self):
        return str(self.title)
    

TIME_CHOICES = [
    ('20:00 pm', '8:00 pm'),
    ('18:00 pm', '6:00 pm'),
    ('16:00 pm', '4:00 pm'),
    ('7:00 pm', '7:00 pm'),
]

SERVICES_MASTER = [
    ('service_master', 'Service Master'),
    ('micheal', 'Micheal'),
    ('daniel', 'Daniel'),
]

SERVICES_CHOICES = [
    ('car_towing', 'Car Towing'),
    ('hail_damage', 'Hail Damage'),
    ('car_wash', 'Car Wash'),
]

    
class Booking(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
    service_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    service_time = models.CharField(max_length=120, choices=TIME_CHOICES)
    services = models.CharField(max_length=50, choices=SERVICES_CHOICES, blank=True, null=True)
    service_master = models.CharField(max_length=120, choices=SERVICES_MASTER, blank=True, null=True)

    class Meta:
        verbose_name = ('Booking')
        verbose_name_plural = ('Bookings')

    def __str__(self):
        return str(self.name)
    
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')

    def __str__(self):
        return str(self.name)