# Generated by Django 2.2 on 2019-04-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_acesso', models.CharField(max_length=8, unique=True)),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.TextField(null=True)),
                ('ementa', models.TextField(null=True)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('professor', models.ManyToManyField(to='aplication.Professor')),
            ],
        ),
    ]
