# Generated by Django 4.2.6 on 2024-02-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_apmcetender_rs_alter_apmctender_rs'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
