# Generated by Django 5.0.1 on 2024-01-26 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0003_remove_enquiry_course_enquiry_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_app.course'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_app.department'),
        ),
    ]
