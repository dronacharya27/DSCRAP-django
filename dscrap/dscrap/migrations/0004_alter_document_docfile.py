# Generated by Django 4.2.2 on 2023-06-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscrap', '0003_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='dscrap/images'),
        ),
    ]