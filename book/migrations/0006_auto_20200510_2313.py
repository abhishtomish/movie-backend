# Generated by Django 3.0.6 on 2020-05-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20200510_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='author', to='book.Book'),
        ),
    ]
