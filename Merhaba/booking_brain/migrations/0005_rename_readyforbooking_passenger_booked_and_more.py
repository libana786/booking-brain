# Generated by Django 4.2.5 on 2023-09-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_brain', '0004_payment_ticket_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='ReadyForBooking',
            new_name='Booked',
        ),
        migrations.AddField(
            model_name='passenger',
            name='Paid',
            field=models.BooleanField(default=False),
        ),
    ]
