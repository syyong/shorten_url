# Generated by Django 2.2 on 2019-05-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten_url', '0002_auto_20190502_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='code',
            field=models.TextField(blank=True, editable=False, max_length=254, null=True, unique=True),
        ),
    ]
