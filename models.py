# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Componist(models.Model):
    componistid = models.IntegerField(db_column='componistID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'componist'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Serie(models.Model):
    serieid = models.IntegerField(db_column='serieID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=255)
    rating = models.IntegerField()
    studio = models.CharField(max_length=255)
    serienaam = models.CharField(db_column='serieNaam', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie'

class Song(models.Model):
    songid = models.IntegerField(db_column='songID', primary_key=True)  # Field name made lowercase.
    singer = models.CharField(max_length=255)
    songsoundtrackid = models.ForeignKey('Soundtrack', models.DO_NOTHING, db_column='SongSoundtrackID')  # Field name made lowercase.
    songcomponistid = models.ForeignKey(Componist, models.DO_NOTHING, db_column='SongComponistID')  # Field name made lowercase.
    songnaam = models.CharField(db_column='songNaam', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'song'

class Soundtrack(models.Model):
    soundtrackid = models.IntegerField(db_column='soundtrackID', primary_key=True)  # Field name made lowercase.
    catagory = models.CharField(max_length=11)
    rating = models.IntegerField()
    description = models.CharField(max_length=11)
    seriessoundtrackid = models.ForeignKey(Serie, models.DO_NOTHING, db_column='SeriesSoundtrackID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'soundtrack'

class User(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'

class Usercomponistfavorite(models.Model):
    usercomponistfavoriteid = models.IntegerField(db_column='UserComponistFavoriteID', primary_key=True)  # Field name made lowercase.
    useridcomponistfavorite = models.ForeignKey(User, models.DO_NOTHING, db_column='UserIDComponistFavorite')  # Field name made lowercase.
    componistiduserfavorite = models.ForeignKey(Componist, models.DO_NOTHING, db_column='ComponistIDUserFavorite')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usercomponistfavorite'

class Usersoundtrackrating(models.Model):
    usersoundtrackratingid = models.IntegerField(db_column='UserSoundtrackRatingID', primary_key=True)  # Field name made lowercase.
    useridsoundtrackrating = models.ForeignKey(User, models.DO_NOTHING, db_column='UserIDSoundtrackRating')  # Field name made lowercase.
    soundtrackuseridrating = models.ForeignKey(Soundtrack, models.DO_NOTHING, db_column='SoundtrackUserIDRating')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usersoundtrackrating'
