# Generated by Django 4.2.1 on 2023-05-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='ordererd',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ordererd_date',
        ),
        migrations.AddField(
            model_name='order',
            name='ordererd_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
