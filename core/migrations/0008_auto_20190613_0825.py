# Generated by Django 2.2.2 on 2019-06-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190612_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativo',
            name='id',
        ),
        migrations.AlterField(
            model_name='ativo',
            name='ip',
            field=models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='Número do IP'),
        ),
    ]
