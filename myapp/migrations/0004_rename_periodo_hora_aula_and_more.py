# Generated by Django 5.0.3 on 2024-04-13 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_turma_num_sala'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Periodo',
            new_name='Hora_aula',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='periodo',
            new_name='hora_aula',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='periodo',
            new_name='ano',
        ),
    ]
