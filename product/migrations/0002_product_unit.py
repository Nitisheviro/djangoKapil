# Generated by Django 3.0.7 on 2020-06-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]