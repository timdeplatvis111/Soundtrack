# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Serie(models.Model):
    serieid = models.IntegerField(db_column='serieID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=255)
    rating = models.IntegerField()
    studio = models.CharField(max_length=255)
    serienaam = models.CharField(db_column='serieNaam', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie'

class Soundtrack(models.Model):
    soundtrackid = models.IntegerField(db_column='soundtrackID', primary_key=True)  # Field name made lowercase.
    catagory = models.CharField(max_length=11)
    rating = models.IntegerField()
    description = models.CharField(max_length=11)
    seriessoundtrackid = models.ForeignKey(Serie, models.DO_NOTHING, db_column='SeriesSoundtrackID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'soundtrack'

class Componist(models.Model):
    componistid = models.IntegerField(db_column='componistID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'componist'

class Song(models.Model):
    songid = models.IntegerField(db_column='songID', primary_key=True)  # Field name made lowercase.
    singer = models.CharField(max_length=255)
    songsoundtrackid = models.ForeignKey('Soundtrack', models.DO_NOTHING, db_column='SongSoundtrackID')  # Field name made lowercase.
    songcomponistid = models.ForeignKey(Componist, models.DO_NOTHING, db_column='SongComponistID')  # Field name made lowercase.
    songnaam = models.CharField(db_column='songNaam', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'song'

