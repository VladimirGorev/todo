# Generated by Django 3.1.4 on 2020-12-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
                ('expire_date', models.DateTimeField(blank=True)),
                ('list_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listmodel')),
            ],
        ),
    ]
