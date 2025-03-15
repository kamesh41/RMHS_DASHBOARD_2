# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rake_handling', '0004_alter_rakeentry_wagon_tippler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rakeentry',
            name='area',
        ),
        migrations.RemoveField(
            model_name='rakeentry',
            name='shift',
        ),
        migrations.RenameField(
            model_name='rakenotification',
            old_name='read',
            new_name='is_read',
        ),
        migrations.AlterField(
            model_name='rakenotification',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterModelOptions(
            name='rakenotification',
            options={'ordering': ['-timestamp']},
        ),
    ] 