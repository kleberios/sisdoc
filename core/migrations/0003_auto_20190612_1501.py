# Generated by Django 2.2.2 on 2019-06-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190612_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='nome',
            field=models.CharField(max_length=40, verbose_name='Nome do Setor'),
        ),
    ]
