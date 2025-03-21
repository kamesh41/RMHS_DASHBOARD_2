# Generated by Django 5.1.7 on 2025-03-13 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeding',
            name='area',
        ),
        migrations.RemoveField(
            model_name='feeding',
            name='material',
        ),
        migrations.RemoveField(
            model_name='feeding',
            name='shift',
        ),
        migrations.RemoveField(
            model_name='receiving',
            name='area',
        ),
        migrations.RemoveField(
            model_name='receiving',
            name='material',
        ),
        migrations.RemoveField(
            model_name='receiving',
            name='shift',
        ),
        migrations.RemoveField(
            model_name='reclaiming',
            name='area',
        ),
        migrations.RemoveField(
            model_name='reclaiming',
            name='material',
        ),
        migrations.RemoveField(
            model_name='reclaiming',
            name='shift',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='description',
            new_name='sub_areas',
        ),
        migrations.RemoveField(
            model_name='material',
            name='description',
        ),
        migrations.AddField(
            model_name='area',
            name='is_combined',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shift',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shift',
            name='name',
            field=models.CharField(choices=[('A', 'Shift A'), ('B', 'Shift B'), ('C', 'Shift C')], max_length=1),
        ),
        migrations.CreateModel(
            name='CrushingOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reported_by', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('crusher', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.area')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.material')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.shift')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeedingOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reported_by', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('destination', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.area')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.material')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.shift')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReceivingOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reported_by', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.area')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.material')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.shift')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReclaimingOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reported_by', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.area')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.material')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.shift')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Crushing',
        ),
        migrations.DeleteModel(
            name='Feeding',
        ),
        migrations.DeleteModel(
            name='Receiving',
        ),
        migrations.DeleteModel(
            name='Reclaiming',
        ),
    ]
