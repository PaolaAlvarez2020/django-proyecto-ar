# Generated by Django 4.1.3 on 2022-11-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_alter_persona_ci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='personas'),
        ),
    ]
