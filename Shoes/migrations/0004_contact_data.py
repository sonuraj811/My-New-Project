# Generated by Django 4.0.4 on 2023-01-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoes', '0003_product_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
