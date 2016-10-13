# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='circRNA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organism', models.CharField(max_length=10, verbose_name=b'organism')),
                ('position', models.TextField(help_text=b'genome browser link', validators=[django.core.validators.URLValidator()])),
                ('strand', models.CharField(max_length=5, verbose_name=b'strand', blank=True)),
                ('circRNA_ID', models.CharField(max_length=100, verbose_name=b'circRNA_ID', blank=True)),
                ('genomic_length', models.IntegerField(verbose_name=b'Genomic length', blank=True)),
                ('spliced_length', models.IntegerField(verbose_name=b'Spliced length', blank=True)),
                ('samples', models.TextField(verbose_name=b'samples', blank=True)),
                ('scores', models.TextField(verbose_name=b'scores', blank=True)),
                ('repeats', models.CharField(blank=True, max_length=50, verbose_name=b'Repeats', choices=[(b'LINE', b'LINE'), (b'SINE', b'SINE')])),
                ('annotation', models.CharField(blank=True, max_length=50, verbose_name=b'Annotation', choices=[(b'LINE', b'LINE'), (b'SINE', b'SINE')])),
                ('best_transcript', models.TextField(verbose_name=b'Best transcript', blank=True)),
                ('gene_symbol', models.CharField(max_length=100, verbose_name=b'Gene symbol', blank=True)),
                ('circRNA_study', models.TextField(verbose_name=b'circRNA study', blank=True)),
                ('comments', models.CharField(max_length=1000, blank=True)),
            ],
        ),
    ]
