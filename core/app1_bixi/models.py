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


class AndroidV2Devices3(models.Model):
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
        db_table = 'android_v2_devices_3'


class CapitulosSerie(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_serie = models.ForeignKey('Contenido', models.DO_NOTHING, db_column='cve_serie')
    nombre = models.CharField(max_length=120)
    temporada = models.IntegerField()
    capitulo = models.IntegerField()
    url_video = models.CharField(max_length=250)
    cve_cat_formato_video = models.IntegerField()
    subtitulo = models.IntegerField()
    sinopsis = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=120)
    fondo = models.CharField(max_length=120)
    estado = models.IntegerField()
    xui = models.IntegerField(blank=True, null=True)
    cve_uploader = models.ForeignKey('Users', models.DO_NOTHING, db_column='cve_uploader')
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'capitulos_serie'


class CatAudio(models.Model):
    cve = models.AutoField(primary_key=True)
    audio = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'cat_audio'


class CatCalidad(models.Model):
    cve = models.AutoField(primary_key=True)
    calidad = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'cat_calidad'


class CatCategorias(models.Model):
    cve = models.AutoField(primary_key=True)
    categoria = models.CharField(unique=True, max_length=80)
    cve_cat_tipo_contenido = models.ForeignKey('CatTipoContenido', models.DO_NOTHING, db_column='cve_cat_tipo_contenido')
    orden = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_categorias'


class CatFormatoVideo(models.Model):
    cve = models.AutoField(primary_key=True)
    formato_video = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'cat_formato_video'


class CatTipoContenido(models.Model):
    cve = models.AutoField(primary_key=True)
    tipo_contenido = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'cat_tipo_contenido'


class Contenido(models.Model):
    cve = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    titulo_latino = models.CharField(max_length=200)
    cve_cat_audio = models.ForeignKey(CatAudio, models.DO_NOTHING, db_column='cve_cat_audio')
    cve_cat_calidad = models.IntegerField()
    cve_cat_categoria = models.ForeignKey(CatCategorias, models.DO_NOTHING, db_column='cve_cat_categoria')
    poster = models.CharField(max_length=200)
    fondo = models.CharField(max_length=200)
    anio = models.CharField(max_length=10, blank=True, null=True)
    clasificacion = models.CharField(max_length=40, blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    pais = models.CharField(max_length=200, blank=True, null=True)
    director = models.CharField(max_length=200, blank=True, null=True)
    reparto = models.CharField(max_length=200, blank=True, null=True)
    pedir_pin = models.IntegerField()
    cve_cat_tipo_contenido = models.IntegerField()
    cve_uploader = models.ForeignKey('Users', models.DO_NOTHING, db_column='cve_uploader')
    tmdb = models.CharField(max_length=20)
    xui = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contenido'


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


class LinkingCode(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=35)
    code = models.CharField(max_length=20, blank=True, null=True)
    dispositivo = models.CharField(max_length=120, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linking_code'


class LinkingCode3(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=35)
    code = models.CharField(max_length=20, blank=True, null=True)
    dispositivo = models.CharField(max_length=120, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linking_code_3'


class LiveTv(models.Model):
    cve = models.AutoField(primary_key=True)
    poster = models.CharField(max_length=120)
    url_video = models.CharField(max_length=120)
    cve_epg = models.IntegerField()
    cve_cat_categoria = models.ForeignKey(CatCategorias, models.DO_NOTHING, db_column='cve_cat_categoria')
    cve_servidor = models.IntegerField()
    fondo = models.CharField(max_length=120, blank=True, null=True)
    servidor_epg = models.IntegerField(blank=True, null=True)
    epg_ahora = models.CharField(max_length=120, blank=True, null=True)
    nombre = models.CharField(max_length=120)
    epg_despues = models.CharField(max_length=120, blank=True, null=True)
    cve_uploader = models.ForeignKey('Users', models.DO_NOTHING, db_column='cve_uploader')
    status = models.IntegerField()
    orden = models.IntegerField(blank=True, null=True)
    cve_canal_epg = models.IntegerField()
    cve_servidor_epg = models.IntegerField()
    visitas = models.IntegerField()
    fecha = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    cve_cat_tipo_contenido = models.IntegerField()
    icono = models.CharField(max_length=120, blank=True, null=True)
    id_epg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_tv'


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


class PlexDevices3(models.Model):
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
        db_table = 'plex_devices_3'


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


class Sales3(models.Model):
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
        db_table = 'sales_3'


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


class Sellers3(models.Model):
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
        db_table = 'sellers_3'


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


class Serveraccounts3(models.Model):
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
        db_table = 'serveraccounts_3'


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


class Serverjellyfin3(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    max_users = models.IntegerField(blank=True, null=True)
    server_users = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serverjellyfin_3'


class Sinopsis(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_contenido = models.ForeignKey(Contenido, models.DO_NOTHING, db_column='cve_contenido')
    cve_cat_tipo_contenido = models.IntegerField()
    sinopsis = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinopsis'


class UrlVideo(models.Model):
    cve = models.AutoField(primary_key=True)
    cve_contenido = models.ForeignKey(Contenido, models.DO_NOTHING, db_column='cve_contenido')
    cve_cat_tipo_contenido = models.IntegerField()
    cve_cat_formato_video = models.IntegerField()
    url_video = models.CharField(max_length=250)

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


class Users(models.Model):
    name = models.CharField(unique=True, max_length=80)
    user = models.CharField(unique=True, max_length=120)
    password = models.CharField(max_length=120)
    user_type = models.CharField(max_length=13)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Users3(models.Model):
    cve = models.AutoField(primary_key=True)
    account = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    device = models.TextField(blank=True, null=True)
    authorization = models.TextField(blank=True, null=True)
    plex_tv_account = models.TextField(blank=True, null=True)
    validity = models.DateTimeField(blank=True, null=True)
    cve_register = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    register_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_3'


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


class UsuarioRoku3(models.Model):
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
        db_table = 'usuario_roku_3'


class UsuarioVod(models.Model):
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
    idu_dispositivo1 = models.CharField(max_length=85, blank=True, null=True)
    idu_dispositivo2 = models.CharField(max_length=85, blank=True, null=True)
    idu_dispositivo3 = models.CharField(max_length=85, blank=True, null=True)
    dispositivo = models.CharField(max_length=155, blank=True, null=True)
    avatar = models.IntegerField(blank=True, null=True)
    adultos = models.IntegerField(blank=True, null=True)
    dealer_name = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    estado = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    pais = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    isp = models.CharField(max_length=200, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lon = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lat = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    uconexion = models.IntegerField(blank=True, null=True)
    viendo = models.CharField(max_length=155, blank=True, null=True)
    viendo_tipo_contenido = models.CharField(max_length=55, blank=True, null=True)
    unlink = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_vod'


class UsuarioVod3(models.Model):
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
    idu_dispositivo1 = models.CharField(max_length=85, blank=True, null=True)
    idu_dispositivo2 = models.CharField(max_length=85, blank=True, null=True)
    idu_dispositivo3 = models.CharField(max_length=85, blank=True, null=True)
    dispositivo = models.CharField(max_length=155, blank=True, null=True)
    avatar = models.IntegerField(blank=True, null=True)
    adultos = models.IntegerField(blank=True, null=True)
    dealer_name = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    estado = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    pais = models.CharField(max_length=180, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    isp = models.CharField(max_length=200, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lon = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    lat = models.CharField(max_length=80, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    uconexion = models.IntegerField(blank=True, null=True)
    viendo = models.CharField(max_length=155, blank=True, null=True)
    viendo_tipo_contenido = models.CharField(max_length=55, blank=True, null=True)
    unlink = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_vod_3'
