# Generated by Django 4.1 on 2022-08-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_key', models.CharField(help_text='The shortened URL.', max_length=7, unique=True)),
                ('original_url', models.URLField(help_text='The original URL.')),
                ('user_id', models.BigIntegerField(help_text='User ID', null=True)),
                ('created_time', models.DateField(help_text='The Short URL created time.', null=True)),
            ],
        ),
    ]