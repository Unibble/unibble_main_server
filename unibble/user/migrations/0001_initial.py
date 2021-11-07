# Generated by Django 3.2.9 on 2021-11-06 07:13

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
            name='Unibber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('profile_img', models.ImageField(upload_to='')),
                ('major', models.CharField(choices=[('de', 'Default'), ('im', '인문계'), ('sh', '사회계'), ('sk', '상경계'), ('gy', '교육계'), ('gh', '공학계'), ('jy', '자연계'), ('med', '의약계'), ('ych', '예체능')], default='de', max_length=3)),
                ('nick_name', models.TextField(max_length=10)),
                ('phone_num', models.TextField(max_length=11)),
                ('student_type', models.CharField(choices=[('newb', '신입생'), ('stdn', '재학생'), ('grad', '졸업생')], default='stdn', max_length=4)),
                ('sns_link', models.TextField(default='연동 없음', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('campus', models.TextField(max_length=30, null=True)),
                ('unibber', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.unibber')),
            ],
        ),
    ]
