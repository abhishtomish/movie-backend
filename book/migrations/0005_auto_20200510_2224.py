# Generated by Django 3.0.6 on 2020-05-10 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='book.Book'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('books', models.ManyToManyField(to='book.Book')),
            ],
        ),
    ]
