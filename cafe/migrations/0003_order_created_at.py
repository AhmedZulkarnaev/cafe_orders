# Generated by Django 4.2.19 on 2025-03-05 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_dish_remove_order_items_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
