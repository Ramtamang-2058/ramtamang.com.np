# Generated by Django 3.2.5 on 2021-07-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mweb', '0011_portfolio_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
                ('cimage', models.ImageField(upload_to='')),
                ('cdate', models.DateTimeField()),
            ],
        ),
    ]
