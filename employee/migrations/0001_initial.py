# Generated by Django 4.0.2 on 2022-04-11 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'education',
            },
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'role',
            },
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sirname', models.CharField(max_length=100)),
                ('work', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('hiring_date', models.DateField()),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.education')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.role')),
            ],
            options={
                'verbose_name_plural': 'employee',
            },
        ),
    ]