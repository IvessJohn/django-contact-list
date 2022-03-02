# Generated by Django 4.0.2 on 2022-03-01 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=15, null=True, unique=True)),
                ('name', models.CharField(max_length=96)),
                ('email', models.CharField(blank=True, max_length=96)),
                ('relationship', models.CharField(choices=[('FAMILY', 'Family'), ('FRIENDS', 'Friends'), ('RELATIVES', 'Relatives'), ('COWORKERS', 'Coworkers'), ('BUSINESS', 'Business')], max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
