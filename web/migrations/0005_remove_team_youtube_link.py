# Generated by Django 4.2.7 on 2023-12-14 05:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_testimonial_testimonial_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="youtube_link",
        ),
    ]
