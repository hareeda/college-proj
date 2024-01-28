# Generated by Django 5.0.1 on 2024-01-25 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('mailId', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=255)),
                ('courses', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('materials', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_app.department')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ('name',),
            },
        ),
    ]
