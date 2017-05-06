# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

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
    last_name = models.CharField(max_length=30)
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


class CityHotelCount(models.Model):
    city_id = models.CharField(max_length=45, blank=True, null=True)
    city_name = models.CharField(max_length=45, blank=True, null=True)
    city_py = models.CharField(max_length=45, blank=True, null=True)
    hotel_count = models.IntegerField(blank=True, null=True)
    height_hotel_count = models.IntegerField(blank=True, null=True)
    middle_hotel_count = models.IntegerField(blank=True, null=True)
    low_hotel_count = models.IntegerField(blank=True, null=True)
    integral = models.IntegerField(blank=True, null=True)
    crawl_date = models.CharField(max_length=45, blank=True, null=True)
    analysis_date = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_hotel_count'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class HotelCityDistribution(models.Model):
    hotel_count_one = models.IntegerField(blank=True, null=True)
    hotel_count_two = models.IntegerField(blank=True, null=True)
    hotel_count_other = models.IntegerField(blank=True, null=True)
    modify_date = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_city_distribution'


class HotelPriceDistribution(models.Model):
    low_hotel_count = models.IntegerField(blank=True, null=True)
    middle_hotel_count = models.IntegerField(blank=True, null=True)
    height_hotel_count = models.IntegerField(blank=True, null=True)
    city_type = models.IntegerField(blank=True, null=True)
    modify_date = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_price_distribution'


class LyCity(models.Model):
    city_id = models.CharField(max_length=45, blank=True, null=True)
    city_name = models.CharField(max_length=45, blank=True, null=True)
    city_py = models.CharField(max_length=45)
    modify_time = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ly_city'


class LyHotCity(models.Model):
    city_id = models.CharField(max_length=45, blank=True, null=True)
    city_name = models.CharField(max_length=45, blank=True, null=True)
    youji_count = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    crawl_time = models.CharField(max_length=45, blank=True, null=True)
    reserve_col1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ly_hot_city'


class Monitor(models.Model):
    job_name = models.CharField(max_length=45, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=45, blank=True, null=True)
    run_status = models.IntegerField(blank=True, null=True)
    run_date = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor'


class Spider(models.Model):
    spider_name = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_3 = models.IntegerField(blank=True, null=True)
    spidercol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider'


class TestmodelTest(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'testmodel_test'


class User(models.Model):
    user_id = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    e_mail = models.CharField(max_length=45, blank=True, null=True)
    cell_phone = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_1 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_2 = models.CharField(max_length=45, blank=True, null=True)
    reserve_col_3 = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
