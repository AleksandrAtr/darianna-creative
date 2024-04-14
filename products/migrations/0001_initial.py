# Generated by Django 3.2.24 on 2024-04-09 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('type', models.CharField(choices=[('artsale', 'Art sale'), ('photosession', 'Photography session'), ('workshop', 'Workshop')], max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ArtSale',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.CharField(choices=[('6x9', '6 by 9'), ('11x17', '11 by 17'), ('23x35', '23 by 35'), ('polaroid', 'Polaroid')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhotographySession',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('session_type', models.CharField(choices=[('45MIN', 'Express Portrait Session (45 minutes)'), ('120MIN', 'Extended Portrait Session (120 minutes)'), ('360MIN', 'Intensive Portrait Session (360 minutes)')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('session_type', models.CharField(choices=[('HALF-DAY', 'Half-Day Workshop'), ('ONE-DAY', 'One-Day Workshop'), ('TWO-DAY', 'Two-Day Workshop')], max_length=8)),
            ],
        ),
    ]
