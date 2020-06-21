# Generated by Django 3.0.6 on 2020-05-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36, unique=True)),
                ('description', models.TextField(blank=True, max_length=256)),
                ('price', models.FloatField(default=0)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='covers/')),
            ],
        ),
    ]