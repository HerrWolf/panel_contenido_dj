# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AndroidV2Devices(models.Model):
    cve_user = models.IntegerField()
    account = models.CharField(max_length=100)
    validity = models.DateField(blank=True, null=True)
    xui_id = models.IntegerField(blank=True, null=True)
    xui_user = models.CharField(max_length=100, blank=True, null=True)
    xui_password = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_v2_devices'


class AndroidV2Devices2(models.Model):
    cve_user = models.IntegerField()
    account = models.CharField(max_length=100)
    validity = models.DateField(blank=True, null=True)
    xui_id = models.IntegerField(blank=True, null=True)
    xui_user = models.CharField(max_length=100, blank=True, null=True)
    xui_password = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_v2_devices_2'


class CapitulosSerie(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_serie = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    temporada = models.IntegerField(blank=True, null=True)
    capitulo = models.IntegerField(blank=True, null=True)
    url_video = models.CharField(max_length=255, blank=True, null=True)
    cve_cat_formato_video = models.IntegerField(blank=True, null=True)
    subtitulo = models.CharField(max_length=500, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sinopsis = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=155, blank=True, null=True)
    fondo = models.CharField(max_length=180, blank=True, null=True)
    cve_uploader = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capitulos_serie'


class CatAudio(models.Model):
    cve = models.AutoField(primary_key=True)
    audio = models.CharField(max_length=55, db_collation='utf8mb3_spanish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_audio'


class CatCalidad(models.Model):
    cve = models.AutoField(primary_key=True)
    calidad = models.CharField(max_length=55, db_collation='utf8mb3_spanish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_calidad'


class CatCategorias(models.Model):
    cve = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_categorias'


class CatEpgCh(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_epg = models.CharField(max_length=120, blank=True, null=True)
    nombre_canal = models.CharField(max_length=180, blank=True, null=True)
    cve_tipo_servidor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_epg_ch'


class CatFormatoVideo(models.Model):
    cve = models.AutoField(primary_key=True)
    formato_video = models.CharField(max_length=155, db_collation='utf8mb3_spanish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_formato_video'


class CatPlataforma(models.Model):
    cve = models.AutoField(primary_key=True)
    plataforma = models.CharField(max_length=155, db_collation='utf8mb3_spanish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_plataforma'


class CatTipoContenido(models.Model):
    cve = models.AutoField(primary_key=True)
    tipo_contenido = models.CharField(max_length=55, db_collation='utf8mb3_spanish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tipo_contenido'


class CatTipoServidor(models.Model):
    cve = models.AutoField(primary_key=True)
    alias_servidor = models.CharField(max_length=88, blank=True, null=True)
    url = models.CharField(max_length=180, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tipo_servidor'


class Contenido(models.Model):
    cve = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=155, blank=True, null=True)
    titulo_latino = models.CharField(max_length=155, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    cve_cat_audio = models.IntegerField(blank=True, null=True)
    cve_cat_calidad = models.IntegerField(blank=True, null=True)
    cve_cat_categoria = models.CharField(max_length=80, blank=True, null=True)
    poster = models.CharField(max_length=155, blank=True, null=True)
    fondo = models.CharField(max_length=180, blank=True, null=True)
    anio = models.CharField(max_length=55, blank=True, null=True)
    clasificacion = models.CharField(max_length=55, blank=True, null=True)
    duracion = models.CharField(max_length=55, blank=True, null=True)
    pais = models.CharField(max_length=200, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    director = models.CharField(max_length=255, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    reparto = models.CharField(max_length=255, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    pedir_pin = models.IntegerField(blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField(blank=True, null=True)
    cve_uploader = models.IntegerField(blank=True, null=True)
    uploader = models.CharField(max_length=50, blank=True, null=True)
    cambio = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contenido'


class CreditosDealer(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_usuario = models.IntegerField(blank=True, null=True)
    creditos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creditos_dealer'


class Emailaccounts(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    client_identifier = models.CharField(max_length=150, blank=True, null=True)
    auth_token = models.CharField(max_length=150, blank=True, null=True)
    master_data = models.TextField(blank=True, null=True)
    is_in_use = models.IntegerField()
    used_at = models.DateTimeField(blank=True, null=True)
    last_user_used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emailaccounts'


class Epg(models.Model):
    id_canal = models.CharField(max_length=50, blank=True, null=True)
    canal = models.CharField(max_length=50, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    titulo = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    sub_titulo = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    descripcion = models.CharField(max_length=500, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'epg'


class Eventos(models.Model):
    cve = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=180, blank=True, null=True)
    poster = models.CharField(max_length=180, blank=True, null=True)
    url_video = models.CharField(max_length=255, blank=True, null=True)
    cve_epg = models.CharField(max_length=80, blank=True, null=True)
    cve_cat_categoria = models.IntegerField(blank=True, null=True)
    cve_servidor = models.IntegerField(blank=True, null=True)
    fondo = models.CharField(max_length=180, blank=True, null=True)
    servidor_epg = models.CharField(max_length=155, blank=True, null=True)
    epg_ahora = models.CharField(max_length=155, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    epg_despues = models.CharField(max_length=155, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    cve_uploader = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    cve_canal_epg = models.CharField(max_length=255, blank=True, null=True)
    cve_servidor_epg = models.CharField(max_length=255, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    visitas = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField()
    icono = models.CharField(max_length=180, blank=True, null=True)
    id_epg = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos'


class Favoritos(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_contenido = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    cve_usuario = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    tipo1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favoritos'


class HistorialCreditosDealer(models.Model):
    folio = models.AutoField(primary_key=True)
    creditos = models.IntegerField(blank=True, null=True)
    cve_cuenta = models.IntegerField(blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)
    cve_dealer = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    saldo_cuenta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_creditos_dealer'


class HistorialCreditosVendidos(models.Model):
    folio = models.AutoField(primary_key=True)
    creditos = models.IntegerField(blank=True, null=True)
    cve_cuenta = models.IntegerField(blank=True, null=True)
    inicio_cobertura = models.CharField(max_length=55, blank=True, null=True)
    fin_cobertura = models.CharField(max_length=55, blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)
    cve_dealer = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_creditos_vendidos'


class JellyfinUsers(models.Model):
    id_user_jellyfin = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    id_cuenta = models.CharField(max_length=100, blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha_vigencia = models.DateTimeField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    id_server_jellyfin = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jellyfin_users'


class JellyfinUsers2(models.Model):
    id_user_jellyfin = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    id_cuenta = models.CharField(max_length=100, blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha_vigencia = models.DateTimeField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    id_server_jellyfin = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jellyfin_users_2'


class JellyfinUsers3(models.Model):
    id_user_jellyfin = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    id_cuenta = models.CharField(max_length=100, blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha_vigencia = models.DateTimeField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    id_server_jellyfin = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jellyfin_users_3'


class LiveTv(models.Model):
    cve = models.AutoField(primary_key=True)
    poster = models.CharField(max_length=180, blank=True, null=True)
    url_video = models.CharField(max_length=255, blank=True, null=True)
    cve_epg = models.CharField(max_length=80, blank=True, null=True)
    cve_cat_categoria = models.IntegerField(blank=True, null=True)
    cve_servidor = models.IntegerField(blank=True, null=True)
    fondo = models.CharField(max_length=180, blank=True, null=True)
    servidor_epg = models.CharField(max_length=155, blank=True, null=True)
    epg_ahora = models.CharField(max_length=155, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    nombre = models.CharField(max_length=180, blank=True, null=True)
    epg_despues = models.CharField(max_length=155, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    cve_uploader = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    cve_canal_epg = models.CharField(max_length=255, blank=True, null=True)
    cve_servidor_epg = models.CharField(max_length=255, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    visitas = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField()
    icono = models.CharField(max_length=180, blank=True, null=True)
    id_epg = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_tv'


class LogCreditosUsuario(models.Model):
    cve = models.AutoField(primary_key=True)
    creditos = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    cve_usuario_vod = models.IntegerField(blank=True, null=True)
    cve_dealer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_creditos_usuario'


class LogHistorial(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_contenido = models.IntegerField(blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField(blank=True, null=True)
    cve_cat_plataforma = models.IntegerField(blank=True, null=True)
    cve_usuario_vod = models.IntegerField(blank=True, null=True)
    visitas = models.IntegerField(blank=True, null=True)
    fecha_uvisita = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_historial'


class LogueosFallidos(models.Model):
    cve = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=55, blank=True, null=True)
    intentos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logueos_fallidos'


class MensajesSistema(models.Model):
    cve = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    mensaje = models.CharField(max_length=600, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    panel = models.CharField(max_length=120, blank=True, null=True)
    usuario = models.CharField(max_length=55, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensajes_sistema'


class MovimientosDealer(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_dealer = models.IntegerField(blank=True, null=True)
    creditos = models.IntegerField(blank=True, null=True)
    movimientos = models.CharField(max_length=188, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    creditos_restantes = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos_dealer'


class PlexDevices(models.Model):
    id_dispositivo = models.CharField(max_length=255, blank=True, null=True)
    id_cuenta = models.TextField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha_vigencia = models.DateField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    idserveraccount = models.TextField(db_column='idServerAccount', blank=True, null=True)  # Field name made lowercase.
    name_device = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField()
    estado = models.IntegerField()
    ligues = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plex_devices'


class PlexDevices2(models.Model):
    id_dispositivo = models.CharField(max_length=255, blank=True, null=True)
    id_cuenta = models.TextField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha_vigencia = models.DateField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    idserveraccount = models.TextField(db_column='idServerAccount', blank=True, null=True)  # Field name made lowercase.
    name_device = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField()
    estado = models.IntegerField()
    ligues = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plex_devices_2'


class PlexDevicesEmail(models.Model):
    id_dispositivo = models.IntegerField(blank=True, null=True)
    id_cuenta = models.CharField(max_length=50, blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    id_email_account = models.IntegerField(blank=True, null=True)
    master_data = models.TextField(blank=True, null=True)
    fecha_vigencia = models.DateField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plex_devices_email'


class Sale(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_emisor = models.IntegerField()
    cve_receptor = models.IntegerField()
    saldo_anterior_emisor = models.TextField()
    saldo_anterior_receptor = models.TextField()
    tipo_transaccion = models.TextField()
    cantidad_creditos_transaccion = models.TextField()
    saldo_actual_emisor = models.TextField()
    saldo_actual_receptor = models.TextField()
    nombre_emisor = models.TextField()
    nombre_receptor = models.TextField()
    fecha_transaccion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sale'


class Sale2(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_emisor = models.IntegerField()
    cve_receptor = models.IntegerField()
    saldo_anterior_emisor = models.TextField()
    saldo_anterior_receptor = models.TextField()
    tipo_transaccion = models.TextField()
    cantidad_creditos_transaccion = models.TextField()
    saldo_actual_emisor = models.TextField()
    saldo_actual_receptor = models.TextField()
    nombre_emisor = models.TextField()
    nombre_receptor = models.TextField()
    fecha_transaccion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sale2'


class Sales2(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_emisor = models.IntegerField()
    cve_receptor = models.IntegerField()
    saldo_anterior_emisor = models.TextField()
    saldo_anterior_receptor = models.TextField()
    tipo_transaccion = models.TextField()
    cantidad_creditos_transaccion = models.TextField()
    saldo_actual_emisor = models.TextField()
    saldo_actual_receptor = models.TextField()
    nombre_emisor = models.TextField()
    nombre_receptor = models.TextField()
    fecha_transaccion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sales_2'


class Seller(models.Model):
    cve = models.AutoField(primary_key=True)
    name = models.TextField()
    user = models.TextField()
    password = models.TextField()
    user_type = models.TextField()
    status = models.IntegerField()
    plex = models.IntegerField()
    cve_reg_user = models.TextField(blank=True, null=True)
    credits = models.IntegerField()
    register_at = models.DateTimeField()
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller'


class Sellers2(models.Model):
    cve = models.AutoField(primary_key=True)
    name = models.TextField()
    user = models.TextField()
    password = models.TextField()
    user_type = models.TextField()
    status = models.IntegerField()
    plex = models.IntegerField()
    cve_reg_user = models.TextField(blank=True, null=True)
    credits = models.IntegerField()
    register_at = models.DateTimeField()
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellers_2'


class Serveraccounts(models.Model):
    nombre_server = models.TextField()
    nombre_cuenta = models.TextField()
    ip_server = models.TextField()
    email = models.TextField()
    password = models.TextField()
    max_devices = models.IntegerField()
    client_identifier = models.TextField(blank=True, null=True)
    auth_token = models.TextField(blank=True, null=True)
    devices = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serveraccounts'


class Serveraccounts2(models.Model):
    nombre_server = models.TextField()
    nombre_cuenta = models.TextField()
    ip_server = models.TextField()
    email = models.TextField()
    password = models.TextField()
    max_devices = models.IntegerField()
    client_identifier = models.TextField()
    auth_token = models.TextField()
    devices = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'serveraccounts_2'


class Serverjellyfin(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    max_users = models.IntegerField(blank=True, null=True)
    server_users = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serverjellyfin'


class Serverjellyfin2(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    max_users = models.IntegerField(blank=True, null=True)
    server_users = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serverjellyfin_2'


class Sinopsis(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_contenido = models.IntegerField(blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField(blank=True, null=True)
    sinopsis = models.TextField(db_collation='utf8mb3_spanish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinopsis'


class Subtitulos(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_contenido = models.IntegerField(blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField(blank=True, null=True)
    subtitulo = models.CharField(max_length=155, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subtitulos'


class TemasKaraoke(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_karaoke = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    num_tema = models.IntegerField(blank=True, null=True)
    url_video = models.CharField(max_length=255, blank=True, null=True)
    cve_cat_formato_video = models.IntegerField(blank=True, null=True)
    subtitulo = models.CharField(max_length=255, blank=True, null=True)
    sinopsis = models.TextField(db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    cve_uploader = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temas_karaoke'


class TipoUsuario(models.Model):
    cve = models.IntegerField(primary_key=True)
    tipo_usuario = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class UrlVideo(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_contenido = models.IntegerField(blank=True, null=True)
    cve_cat_tipo_contenido = models.IntegerField(blank=True, null=True)
    cve_cat_formato_video = models.IntegerField(blank=True, null=True)
    url_video = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url_video'


class User(models.Model):
    cve = models.AutoField(primary_key=True)
    account = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    device = models.TextField(blank=True, null=True)
    validity = models.DateTimeField(blank=True, null=True)
    cve_register = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    register_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Users2(models.Model):
    cve = models.AutoField(primary_key=True)
    account = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    device = models.TextField(blank=True, null=True)
    validity = models.DateTimeField(blank=True, null=True)
    cve_register = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    register_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_2'


class Usuario(models.Model):
    cve = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=55, blank=True, null=True)
    contrasenia = models.CharField(max_length=105, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    fecha_uconexion = models.DateTimeField(blank=True, null=True)
    ip_uconexion = models.CharField(max_length=35, blank=True, null=True)
    tipo_usuario = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    notas = models.CharField(max_length=250, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    cve_dealer_registro = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    demos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioRoku(models.Model):
    cve = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=55, blank=True, null=True)
    contrasenia = models.CharField(max_length=55, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    pin = models.CharField(max_length=55, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    cve_dealer = models.IntegerField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    fecha_uconexion = models.DateTimeField(blank=True, null=True)
    ip_uconexion = models.CharField(max_length=55, blank=True, null=True)
    idu_dispositivo = models.CharField(max_length=85, blank=True, null=True)
    dispositivo = models.CharField(max_length=155, blank=True, null=True)
    avatar = models.IntegerField(blank=True, null=True)
    adultos = models.IntegerField(blank=True, null=True)
    dealer_name = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    device = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    pais = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    isp = models.CharField(max_length=200, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lon = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lat = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    uconexion = models.IntegerField(blank=True, null=True)
    viendo = models.CharField(max_length=155, blank=True, null=True)
    viendo_tipo_contenido = models.CharField(max_length=55, blank=True, null=True)
    unlink = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    cuenta = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_roku'


class UsuarioRoku2(models.Model):
    cve = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=55, blank=True, null=True)
    contrasenia = models.CharField(max_length=55, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    pin = models.CharField(max_length=55, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    cve_dealer = models.IntegerField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    fecha_uconexion = models.DateTimeField(blank=True, null=True)
    ip_uconexion = models.CharField(max_length=55, blank=True, null=True)
    idu_dispositivo = models.CharField(max_length=85, blank=True, null=True)
    dispositivo = models.CharField(max_length=155, blank=True, null=True)
    avatar = models.IntegerField(blank=True, null=True)
    adultos = models.IntegerField(blank=True, null=True)
    dealer_name = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    device = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    pais = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    isp = models.CharField(max_length=200, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lon = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lat = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    uconexion = models.IntegerField(blank=True, null=True)
    viendo = models.CharField(max_length=155, blank=True, null=True)
    viendo_tipo_contenido = models.CharField(max_length=55, blank=True, null=True)
    unlink = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    cuenta = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_roku_2'


# class UsuarioVod(models.Model):
#     cve = models.AutoField(primary_key=True)
#     usuario = models.CharField(max_length=55, blank=True, null=True)
#     contrasenia = models.CharField(max_length=55, blank=True, null=True)
#     nombre = models.CharField(max_length=80, blank=True, null=True)
#     pin = models.CharField(max_length=55, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     cve_dealer = models.IntegerField(blank=True, null=True)
#     fecha_vencimiento = models.DateTimeField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     fecha_uconexion = models.DateTimeField(blank=True, null=True)
#     ip_uconexion = models.CharField(max_length=55, blank=True, null=True)
#     idu_dispositivo1 = models.CharField(max_length=85, blank=True, null=True)
#     idu_dispositivo2 = models.CharField(max_length=85, blank=True, null=True)
#     idu_dispositivo3 = models.CharField(max_length=85, blank=True, null=True)
#     dispositivo = models.CharField(max_length=155, blank=True, null=True)
#     avatar = models.IntegerField(blank=True, null=True)
#     adultos = models.IntegerField(blank=True, null=True)
#     dealer_name = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     estado = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     pais = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     isp = models.CharField(max_length=200, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     lon = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     lat = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     uconexion = models.IntegerField(blank=True, null=True)
#     viendo = models.CharField(max_length=155, blank=True, null=True)
#     viendo_tipo_contenido = models.CharField(max_length=55, blank=True, null=True)
#     unlink = models.IntegerField(blank=True, null=True)
#     codigo = models.CharField(max_length=10, blank=True, null=True)
#     link = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'usuario_vod'
#
#
# class UsuarioVod2(models.Model):
#     cve = models.AutoField(primary_key=True)
#     usuario = models.CharField(max_length=55, blank=True, null=True)
#     contrasenia = models.CharField(max_length=55, blank=True, null=True)
#     nombre = models.CharField(max_length=80, blank=True, null=True)
#     pin = models.CharField(max_length=55, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     cve_dealer = models.IntegerField(blank=True, null=True)
#     fecha_vencimiento = models.DateTimeField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     fecha_uconexion = models.DateTimeField(blank=True, null=True)
#     ip_uconexion = models.CharField(max_length=55, blank=True, null=True)
#     idu_dispositivo1 = models.CharField(max_length=85, blank=True, null=True)
#     idu_dispositivo2 = models.CharField(max_length=85, blank=True, null=True)
#     idu_dispositivo3 = models.CharField(max_length=85, blank=True, null=True)
#     dispositivo = models.CharField(max_length=155, blank=True, null=True)
#     avatar = models.IntegerField(blank=True, null=True)
#     adultos = models.IntegerField(blank=True, null=True)
#     dealer_name = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     estado = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     pais = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     isp = models.CharField(max_length=200, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     lon = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     lat = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
#     uconexion = models.IntegerField(blank=True, null=True)
#     viendo = models.CharField(max_length=155, blank=True, null=True)
#     viendo_tipo_contenido = models.CharField(max_length=55, blank=True, null=True)
#     unlink = models.IntegerField(blank=True, null=True)
#     codigo = models.CharField(max_length=10, blank=True, null=True)
#     link = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'usuario_vod_2'


