# Generated by Django 4.2.2 on 2023-06-26 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscrap', '0008_alter_document_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='useraddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
