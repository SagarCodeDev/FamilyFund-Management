# Generated by Django 4.1.2 on 2023-03-15 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0009_alter_expenses_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]