# Generated by Django 3.2.9 on 2021-11-06 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bubble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('live', '대기중'), ('confirmed', '확정됨'), ('expired', '만료됨')], default='live', max_length=10)),
                ('created', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('title', models.TextField(max_length=50)),
                ('content', models.TextField(blank=True, max_length=500, null=True)),
                ('category', models.PositiveSmallIntegerField(blank=True, choices=[('live', '대기중'), ('confirmed', '확정됨'), ('expired', '만료됨')])),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.unibber')),
            ],
        ),
    ]
