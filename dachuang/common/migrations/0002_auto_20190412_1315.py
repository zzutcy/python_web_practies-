# Generated by Django 2.1.7 on 2019-04-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
                ('hostname', models.CharField(max_length=200)),
                ('ipv4addr', models.CharField(max_length=200)),
                ('macaddr', models.CharField(max_length=200)),
                ('ipv6addr', models.CharField(max_length=200)),
                ('duid', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='center',
        ),
    ]
