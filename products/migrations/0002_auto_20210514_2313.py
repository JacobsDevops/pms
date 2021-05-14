# Generated by Django 3.2.3 on 2021-05-14 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterField(
            model_name='actions',
            name='action_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Tarih-Saat'),
        ),
    ]
