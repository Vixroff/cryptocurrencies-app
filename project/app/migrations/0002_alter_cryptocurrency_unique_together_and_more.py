# Generated by Django 4.2.1 on 2023-06-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cryptocurrency',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='cryptocurrency',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='name',
            field=models.CharField(unique=True, verbose_name='Название'),
        ),
    ]
