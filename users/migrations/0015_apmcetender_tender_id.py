# Generated by Django 4.1.7 on 2023-12-05 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_apmcetender_delete_apmc'),
    ]

    operations = [
        migrations.AddField(
            model_name='apmcetender',
            name='tender_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.apmctender'),
        ),
    ]
