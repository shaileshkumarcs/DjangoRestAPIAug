# Generated by Django 2.0 on 2018-08-20 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradigms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programmers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='languages',
            name='paradigm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Paradigms'),
        ),
        migrations.AddField(
            model_name='programmers',
            name='languages',
            field=models.ManyToManyField(to='languages.Languages'),
        ),
    ]