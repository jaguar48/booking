# Generated by Django 2.2.10 on 2021-10-04 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('callapp', '0009_auto_20211004_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_account', models.CharField(max_length=50)),
                ('to_account', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
