# Generated by Django 4.2.2 on 2023-06-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscrap', '0002_remove_contact_contact_id_alter_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='images')),
            ],
        ),
    ]
