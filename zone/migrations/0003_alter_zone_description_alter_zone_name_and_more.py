# Generated by Django 4.1.5 on 2023-01-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zone', '0002_zone_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='description',
            field=models.TextField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(default='Default name', max_length=100),
        ),
        migrations.AlterField(
            model_name='zone',
            name='zone_type',
            field=models.CharField(choices=[('NT', 'Natural'), ('TG', 'Technogenic'), ('AG', 'Anthropogenic'), ('EC', 'Ecological')], max_length=5),
        ),
    ]
