# Generated by Django 5.0.4 on 2024-04-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvelAutosApp', '0002_insurance_services_vehicletype_users_users_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='password', max_length=100, verbose_name='Person has to set Password for Login purpose'),
        ),
        migrations.AlterField(
            model_name='users',
            name='mail_address',
            field=models.EmailField(max_length=50, unique=True, verbose_name="Person's Mail Address"),
        ),
    ]
