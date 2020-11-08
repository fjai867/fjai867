# Generated by Django 3.0.6 on 2020-08-04 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_atletas', '0002_auto_20200704_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcion',
            name='Id_Atleta',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='username',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
