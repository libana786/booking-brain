# Generated by Django 4.2.5 on 2023-10-08 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking_brain', '0007_alter_passenger_return_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Date_created', models.DateTimeField(auto_now_add=True)),
                ('Data', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='passenger',
            name='Return_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]