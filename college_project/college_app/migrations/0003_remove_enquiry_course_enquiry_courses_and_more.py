# Generated by Django 5.0.1 on 2024-01-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0002_remove_enquiry_courses_enquiry_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='course',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='courses',
            field=models.CharField(default=143, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='department',
            field=models.CharField(max_length=255),
        ),
    ]