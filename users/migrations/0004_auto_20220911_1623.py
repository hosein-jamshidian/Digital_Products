# Generated by Django 3.2 on 2022-09-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220911_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'Device', 'verbose_name_plural': 'Devices'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'web'), (2, 'ios'), (3, 'android')], default=1, verbose_name='device type'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_uuid',
            field=models.UUIDField(null=True, verbose_name='device uuid'),
        ),
        migrations.AlterField(
            model_name='device',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last time login'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.BooleanField(help_text='if male is True , if female is False and null is unset', null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='nickname'),
        ),
    ]
