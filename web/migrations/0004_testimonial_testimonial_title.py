# Generated by Django 4.2.7 on 2023-12-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_alter_about_options_alter_blog_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonial",
            name="testimonial_title",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
