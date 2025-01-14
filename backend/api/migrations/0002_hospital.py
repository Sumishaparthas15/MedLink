# Generated by Django 3.2.12 on 2024-06-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='hospital_photos/')),
                ('password', models.CharField(max_length=250)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
