# Generated by Django 4.2.19 on 2025-03-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(verbose_name='Номер стола')),
                ('items', models.JSONField(verbose_name='Список блюд и цены')),
                ('total_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Общая стоимость')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('ready', 'Готово'), ('paid', 'Оплачено')], default='pending', max_length=10, verbose_name='Статус заказа')),
            ],
        ),
    ]
