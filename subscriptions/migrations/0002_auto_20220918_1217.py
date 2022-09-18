# Generated by Django 3.2 on 2022-09-18 07:47

from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='sku',
            field=models.CharField(db_index=True, max_length=20, validators=[utils.validators.SKUValidator()], verbose_name='stock keeping unit'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='subscriptions.package'),
        ),
    ]