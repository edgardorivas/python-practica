# Generated by Django 4.1.1 on 2022-10-04 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('tipoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tipousuario')),
            ],
        ),
    ]
