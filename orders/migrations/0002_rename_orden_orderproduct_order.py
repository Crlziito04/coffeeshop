# Generated by Django 5.0.7 on 2024-07-22 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='orden',
            new_name='order',
        ),
    ]
