# Generated by Django 3.2.13 on 2022-11-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='status_type',
            field=models.IntegerField(choices=[(1, '거래중'), (2, '거래완료')], default=1),
        ),
    ]
