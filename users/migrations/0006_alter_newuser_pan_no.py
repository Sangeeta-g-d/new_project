# Generated by Django 4.1.7 on 2023-11-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_user_passwordreset_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='pan_no',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
