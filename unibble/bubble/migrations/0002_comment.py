# Generated by Django 3.2.9 on 2021-11-06 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('bubble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=200)),
                ('bubble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bubble.bubble')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.unibber')),
            ],
        ),
    ]