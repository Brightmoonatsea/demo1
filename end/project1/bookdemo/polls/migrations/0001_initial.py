# Generated by Django 3.0.3 on 2020-02-17 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='投票问题')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '投票表',
                'verbose_name_plural': '投票表',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='选项')),
                ('votes', models.PositiveIntegerField(default=0, verbose_name='投票的数目')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question', verbose_name='所属问题')),
            ],
            options={
                'verbose_name': '选项表',
                'verbose_name_plural': '选项表',
                'ordering': ['-create_date'],
            },
        ),
    ]
