# Generated by Django 5.1.6 on 2025-03-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_type_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('shop_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('services_title', models.CharField(max_length=255)),
            ],
        ),
    ]
