# Generated by Django 2.0.3 on 2018-03-22 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import enumfields.fields
import freenodejobs.jobs.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_state', enumfields.fields.EnumIntegerField(enum=freenodejobs.jobs.enums.StateEnum)),
                ('new_state', enumfields.fields.EnumIntegerField(enum=freenodejobs.jobs.enums.StateEnum)),
                ('description', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_history_changes', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_history', to='jobs.Job')),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
    ]
