# Generated by Django 3.0.3 on 2020-02-06 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('passive_ability', models.CharField(max_length=30)),
                ('ability', models.CharField(max_length=30)),
                ('super', models.CharField(max_length=30)),
                ('skin', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ammo', models.CharField(max_length=20)),
                ('attachments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapon_attachments', to='apex_app.Attachment')),
                ('weapon_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapon_types', to='apex_app.WeaponType')),
            ],
        ),
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skins', to='apex_app.Character')),
            ],
        ),
    ]
