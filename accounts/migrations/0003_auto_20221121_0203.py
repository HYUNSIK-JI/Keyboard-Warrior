# Generated by Django 3.2.13 on 2022-11-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221121_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='signal',
        ),
    ]
