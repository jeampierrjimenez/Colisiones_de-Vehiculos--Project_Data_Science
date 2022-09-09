from django.db import models

# Modelos a partir de tablas de la base de datos


class MotorVehicleCollisionsCrashes(models.Model):
    id_collision = models.CharField(db_column='ID_COLLISION', primary_key=True, max_length=100)  # Field name made lowercase.
    crash_date = models.CharField(db_column='CRASH_DATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    crash_time = models.CharField(db_column='CRASH_TIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    week_day = models.CharField(db_column='WEEK_DAY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='MONTH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borough = models.CharField(db_column='BOROUGH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='LATITUDE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='LONGITUDE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    on_street_name = models.CharField(db_column='ON_STREET_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    off_street_name = models.CharField(db_column='OFF_STREET_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_persons_injured = models.CharField(db_column='NUMBER_OF_PERSONS_INJURED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_persons_killed = models.CharField(db_column='NUMBER_OF_PERSONS_KILLED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_pedestrians_injured = models.CharField(db_column='NUMBER_OF_PEDESTRIANS_INJURED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_pedestrians_killed = models.CharField(db_column='NUMBER_OF_PEDESTRIANS_KILLED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_cyclist_injured = models.CharField(db_column='NUMBER_OF_CYCLIST_INJURED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_cyclist_killed = models.CharField(db_column='NUMBER_OF_CYCLIST_KILLED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_motorist_injured = models.CharField(db_column='NUMBER_OF_MOTORIST_INJURED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_motorist_killed = models.CharField(db_column='NUMBER_OF_MOTORIST_KILLED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contributing_factor_vehicle_1 = models.CharField(db_column='CONTRIBUTING_FACTOR_VEHICLE_1', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'motor_vehicle_collisions_crashes'


class MonthCrashPerc(models.Model):
    month = models.IntegerField(db_column='MONTH', primary_key=True)  # Field name made lowercase.
    collision_count = models.IntegerField(db_column='COLLISION_COUNT', blank=True, null=True)  # Field name made lowercase.
    perc = models.FloatField(db_column='PERC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'month_crash_perc'


class TimeCrashPerc(models.Model):
    crash_time = models.TimeField(db_column='CRASH_TIME', primary_key=True)  # Field name made lowercase.
    collision_count = models.IntegerField(db_column='COLLISION_COUNT', blank=True, null=True)  # Field name made lowercase.
    perc = models.FloatField(db_column='PERC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_crash_perc'


class ZoneCrash(models.Model):
    id_zone_crash = models.AutoField(db_column='ID_ZONE_CRASH', primary_key=True)  # Field name made lowercase.
    borough = models.CharField(db_column='BOROUGH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    collision_count = models.IntegerField(db_column='COLLISION_COUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zone_crash'


class PublicDamage(models.Model):
    id_public_damage = models.AutoField(db_column='ID_PUBLIC_DAMAGE', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    crash_time = models.CharField(db_column='CRASH_TIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'public_damage'



class LicenceStates(models.Model):
    id_licence_states = models.AutoField(db_column='ID_LICENCE_STATES', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    driver_license_jurisdiction = models.CharField(db_column='DRIVER_LICENSE_JURISDICTION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'licence_states'



class FactorBySex(models.Model):
    id_factor_by_sex = models.AutoField(db_column='ID_FACTOR_BY_SEX', primary_key=True)  # Field name made lowercase.
    crash_year = models.IntegerField(db_column='CRASH_YEAR', blank=True, null=True)  # Field name made lowercase.
    driver_sex = models.CharField(db_column='DRIVER_SEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contributing_factor = models.CharField(db_column='CONTRIBUTING_FACTOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factor_by_sex'


class DataMonthlyByType(models.Model):
    periodo = models.CharField(db_column='PERIODO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    qty_bicyclist = models.IntegerField(db_column='QTY_BICYCLIST', blank=True, null=True)  # Field name made lowercase.
    qty_occupant = models.IntegerField(db_column='QTY_OCCUPANT', blank=True, null=True)  # Field name made lowercase.
    qty_other_motorized = models.IntegerField(db_column='QTY_OTHER_MOTORIZED', blank=True, null=True)  # Field name made lowercase.
    qty_pedestrian = models.IntegerField(db_column='QTY_PEDESTRIAN', blank=True, null=True)  # Field name made lowercase.
    qty_total = models.IntegerField(db_column='QTY_TOTAL', blank=True, null=True)  # Field name made lowercase.
    id_data_monthly_by_type = models.AutoField(db_column='ID_DATA_MONTHLY_BY_TYPE', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_monthly_by_type'


class DataMonthlyByStatus(models.Model):
    periodo = models.CharField(db_column='PERIODO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    qty_apparent_death = models.IntegerField(db_column='QTY_APPARENT_DEATH', blank=True, null=True)  # Field name made lowercase.
    qty_conscious = models.IntegerField(db_column='QTY_CONSCIOUS', blank=True, null=True)  # Field name made lowercase.
    qty_does_not_apply = models.IntegerField(db_column='QTY_DOES_NOT_APPLY', blank=True, null=True)  # Field name made lowercase.
    qty_incoherent = models.IntegerField(db_column='QTY_INCOHERENT', blank=True, null=True)  # Field name made lowercase.
    qty_semiconscious = models.IntegerField(db_column='QTY_SEMICONSCIOUS', blank=True, null=True)  # Field name made lowercase.
    qty_shock = models.IntegerField(db_column='QTY_SHOCK', blank=True, null=True)  # Field name made lowercase.
    qty_unconscious = models.IntegerField(db_column='QTY_UNCONSCIOUS', blank=True, null=True)  # Field name made lowercase.
    qty_unknown = models.IntegerField(db_column='QTY_UNKNOWN', blank=True, null=True)  # Field name made lowercase.
    qty_total = models.IntegerField(db_column='QTY_TOTAL', blank=True, null=True)  # Field name made lowercase.
    id_data_monthly_by_status = models.AutoField(db_column='ID_DATA_MONTHLY_BY_STATUS', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_monthly_by_status'


class DataMonthlyBySex(models.Model):
    periodo = models.CharField(db_column='PERIODO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    qty_male = models.IntegerField(db_column='QTY_MALE', blank=True, null=True)  # Field name made lowercase.
    qty_female = models.IntegerField(db_column='QTY_FEMALE', blank=True, null=True)  # Field name made lowercase.
    qty_undefined = models.IntegerField(db_column='QTY_UNDEFINED', blank=True, null=True)  # Field name made lowercase.
    qty_total = models.IntegerField(db_column='QTY_TOTAL', blank=True, null=True)  # Field name made lowercase.
    id_monthly_by_sex = models.AutoField(db_column='ID_MONTHLY_BY_SEX', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_monthly_by_sex'


class DataMonthlyByInjury(models.Model):
    periodo = models.CharField(db_column='PERIODO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    qty_injured = models.IntegerField(db_column='QTY_INJURED', blank=True, null=True)  # Field name made lowercase.
    qty_killed = models.IntegerField(db_column='QTY_KILLED', blank=True, null=True)  # Field name made lowercase.
    qty_unspecified = models.IntegerField(db_column='QTY_UNSPECIFIED', blank=True, null=True)  # Field name made lowercase.
    qty_total = models.IntegerField(db_column='QTY_TOTAL', blank=True, null=True)  # Field name made lowercase.
    id_monthly_by_injury = models.AutoField(db_column='ID_MONTHLY_BY_INJURY', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_monthly_by_injury'


class YearMonthCrashCount(models.Model):
    year = models.CharField(db_column='YEAR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='MONTH', max_length=45, blank=True, null=True)  # Field name made lowercase.
    collision_count = models.IntegerField(db_column='COLLISION_COUNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    id_year_month_crash_count = models.AutoField(db_column='ID_YEAR_MONTH_CRASH_COUNT', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'year_month_crash_count'


class DayCrashPerc(models.Model):
    week_day = models.IntegerField(db_column='WEEK_DAY', primary_key=True)  # Field name made lowercase.
    collision_count = models.IntegerField(db_column='COLLISION_COUNT', blank=True, null=True)  # Field name made lowercase.
    perc = models.FloatField(db_column='PERC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'day_crash_perc'


class Licence(models.Model):
    id_licence = models.IntegerField(db_column='ID_LICENCE', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    driver_licence = models.CharField(db_column='DRIVER_LICENCE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'licence'








