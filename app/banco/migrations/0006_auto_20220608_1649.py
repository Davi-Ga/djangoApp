# Generated by Django 3.2.13 on 2022-06-08 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0005_auto_20220608_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='tipo',
            field=models.CharField(blank=True, choices=[(1, 'Celular'), (0, 'Fixo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='tipo1',
            field=models.CharField(blank=True, choices=[(1, 'Celular'), (0, 'Fixo')], max_length=1),
        ),
    ]