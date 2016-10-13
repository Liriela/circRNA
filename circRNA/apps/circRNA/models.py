from django.db import models

from django.core.validators import URLValidator

class circRNA(models.Model):
    """docstring for circRNA."""

    REPEATS = (
        ('LINE', 'LINE'),
        ('SINE', 'SINE')
    )
    ANNOTATION = (
        ('ALT_DONOR', 'ALT_DONOR'),
        ('CDS', 'CDS'),
        ('coding', 'coding'),
        ('UTR3', 'UTR3'),
    )
    
    organism = models.CharField(max_length=10, verbose_name='organism')
    position = models.TextField(validators=[URLValidator()], help_text="genome browser link")
    strand = models.CharField(max_length=5, verbose_name='strand', blank=True)
    circRNA_ID = models.CharField(max_length=100, verbose_name='circRNA_ID', blank=True)
    genomic_length = models.IntegerField(verbose_name='Genomic length', blank=True)
    spliced_length = models.IntegerField(verbose_name='Spliced length', blank=True)  
    samples = models.TextField(verbose_name='samples', blank=True)
    scores = models.TextField(verbose_name='scores', blank=True)
    repeats = models.CharField(max_length=50, verbose_name='Repeats', choices=REPEATS, blank=True)
    annotation = models.CharField(max_length=50, verbose_name='Annotation', choices=REPEATS, blank=True)
    best_transcript = models.TextField(verbose_name='Best transcript', blank=True)
    gene_symbol = models.CharField(max_length=100, verbose_name='Gene symbol', blank=True) 
    circRNA_study = models.TextField(verbose_name='circRNA study', blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.circRNA_ID