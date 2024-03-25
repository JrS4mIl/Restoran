# Generated by Django 5.0.2 on 2024-03-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='fooditem',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]