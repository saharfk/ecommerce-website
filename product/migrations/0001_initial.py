# Generated by Django 3.0.7 on 2022-06-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Info', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Info', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Info', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('URL', models.CharField(blank=True, max_length=120)),
                ('Info', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]