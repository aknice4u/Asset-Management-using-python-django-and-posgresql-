# Generated by Django 4.0.1 on 2022-01-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetsmgt', '0003_alter_assets_is_disposed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='is_disposed',
            field=models.IntegerField(default=0),
        ),
    ]
