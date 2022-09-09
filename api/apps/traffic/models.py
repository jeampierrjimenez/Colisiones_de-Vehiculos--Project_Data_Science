from django.db import models


class TrafficVolume(models.Model):
    boro = models.CharField(db_column='BORO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wktgeom = models.CharField(db_column='WKTGEOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='DAY', blank=True, null=True)  # Field name made lowercase.
    hour = models.IntegerField(db_column='HOUR', blank=True, null=True)  # Field name made lowercase.
    volumen = models.FloatField(db_column='VOLUMEN', blank=True, null=True)  # Field name made lowercase.
    id_traffic = models.AutoField(db_column='ID_TRAFFIC', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'traffic_volume'


class TrafficVolumeAlt(models.Model):
    boro = models.CharField(db_column='BORO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='DAY', blank=True, null=True)  # Field name made lowercase.
    vol = models.FloatField(db_column='VOL', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='STREET', max_length=40, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    id_traffic_volume_alt = models.AutoField(db_column='ID_TRAFFIC_VOLUME_ALT', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'traffic_volume_alt'


class CalleBarrioLe(models.Model):
    boro = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    boro_le = models.IntegerField(blank=True, null=True)
    street_le = models.IntegerField(blank=True, null=True)
    id_calle_barrio_le = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'calle_barrio_le'



