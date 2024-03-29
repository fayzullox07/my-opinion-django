# Generated by Django 3.2.6 on 2022-06-07 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('emoji', models.ImageField(upload_to='post/emojies/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('surname', models.CharField(blank=True, max_length=50)),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images/')),
                ('gender', models.CharField(blank=True, choices=[('erkak', 'ERKAK'), ('ayol', 'AYOL'), ('nomalum', 'ANIQMAS')], max_length=10)),
                ('age', models.PositiveIntegerField(default=0)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('body', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('emoji', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='emojies', to='main.emoji')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='main.tag')),
            ],
        ),
    ]
