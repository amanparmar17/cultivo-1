# Generated by Django 2.1.1 on 2018-11-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultivo_main', '0012_pred_one_org_mean_gross_production_value_constant_2004_2006_million_us_dollar'),
    ]

    operations = [
        migrations.AddField(
            model_name='pred_three',
            name='exports_mean',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='pred_three',
            name='imports_mean',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='pred_three',
            name='production_mean',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=12),
        ),
    ]
