# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessOutput(models.Model):
    access_output_id = models.AutoField(primary_key=True)
    output_name = models.CharField(max_length=255)
    output_key = models.CharField(max_length=255)
    output_ext = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'access_output'


class AdminSettings(models.Model):
    type = models.CharField(primary_key=True, max_length=128)
    value = models.CharField(max_length=4096)

    class Meta:
        managed = False
        db_table = 'admin_settings'


class BlockedIps(models.Model):
    ip = models.CharField(unique=True, max_length=39)
    notes = models.TextField()
    date = models.IntegerField()
    attempts_blocked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blocked_ips'


class BlockedUserAgents(models.Model):
    user_agent = models.CharField(max_length=255)
    exact_match = models.IntegerField()
    attempts_blocked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blocked_user_agents'


class Bouquets(models.Model):
    bouquet_name = models.TextField()
    bouquet_channels = models.TextField()
    bouquet_series = models.TextField()
    bouquet_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bouquets'


class ClientLogs(models.Model):
    stream_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    client_status = models.CharField(max_length=255)
    query_string = models.TextField()
    user_agent = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    extra_data = models.TextField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_logs'


class Created(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    category_id = models.IntegerField()
    stream_display_name = models.IntegerField()
    stream_source = models.IntegerField()
    stream_icon = models.IntegerField()
    notes = models.IntegerField()
    created_channel_location = models.IntegerField()
    enable_transcode = models.IntegerField()
    transcode_attributes = models.IntegerField()
    custom_ffmpeg = models.IntegerField()
    movie_propeties = models.IntegerField()
    movie_subtitles = models.IntegerField()
    read_native = models.IntegerField()
    target_container = models.IntegerField()
    stream_all = models.IntegerField()
    remove_subtitles = models.IntegerField()
    custom_sid = models.IntegerField()
    epg_id = models.IntegerField()
    channel_id = models.IntegerField()
    epg_lang = models.IntegerField()
    order = models.IntegerField()
    auto_restart = models.IntegerField()
    transcode_profile_id = models.IntegerField()
    pids_create_channel = models.IntegerField()
    cchannel_rsources = models.IntegerField()
    gen_timestamps = models.IntegerField()
    added = models.IntegerField()
    series_no = models.IntegerField()
    direct_source = models.IntegerField()
    tv_archive_duration = models.IntegerField()
    tv_archive_server_id = models.IntegerField()
    tv_archive_pid = models.IntegerField()
    movie_symlink = models.IntegerField()
    redirect_stream = models.IntegerField()
    rtmp_output = models.IntegerField()
    number = models.IntegerField()
    allow_record = models.IntegerField()
    probesize_ondemand = models.IntegerField()
    custom_map = models.IntegerField()
    external_push = models.IntegerField()
    delay_minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'created'


class CreditsLog(models.Model):
    target_id = models.IntegerField()
    admin_id = models.IntegerField()
    amount = models.FloatField()
    date = models.IntegerField()
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'credits_log'


class Cronjobs(models.Model):
    description = models.TextField()
    filename = models.CharField(max_length=255)
    run_per_mins = models.IntegerField()
    run_per_hours = models.IntegerField()
    enabled = models.IntegerField()
    pid = models.IntegerField()
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cronjobs'


class DashboardStatistics(models.Model):
    type = models.CharField(max_length=16)
    time = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dashboard_statistics'


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=255)
    device_key = models.CharField(max_length=255)
    device_filename = models.CharField(max_length=255)
    device_header = models.TextField()
    device_conf = models.TextField()
    device_footer = models.TextField()
    default_output = models.IntegerField()
    copy_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class Enigma2Actions(models.Model):
    device_id = models.IntegerField()
    type = models.TextField()
    key = models.TextField()
    command = models.TextField()
    command2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'enigma2_actions'


class Enigma2Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    mac = models.CharField(max_length=255)
    user_id = models.IntegerField()
    modem_mac = models.CharField(max_length=255)
    local_ip = models.CharField(max_length=255)
    public_ip = models.CharField(max_length=255)
    key_auth = models.CharField(max_length=255)
    enigma_version = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    lversion = models.TextField()
    token = models.CharField(max_length=32)
    last_updated = models.IntegerField()
    watchdog_timeout = models.IntegerField()
    lock_device = models.IntegerField()
    telnet_enable = models.IntegerField()
    ftp_enable = models.IntegerField()
    ssh_enable = models.IntegerField()
    dns = models.CharField(max_length=255)
    original_mac = models.CharField(max_length=255)
    rc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enigma2_devices'


class Enigma2Failed(models.Model):
    original_mac = models.CharField(max_length=255)
    virtual_mac = models.CharField(max_length=255)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enigma2_failed'


class Epg(models.Model):
    epg_name = models.CharField(max_length=255)
    epg_file = models.CharField(max_length=300)
    integrity = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.IntegerField(blank=True, null=True)
    days_keep = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'epg'


class EpgData(models.Model):
    epg_id = models.IntegerField()
    title = models.CharField(max_length=255)
    lang = models.CharField(max_length=10)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    channel_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'epg_data'


class IspAddon(models.Model):
    isp = models.TextField()
    blocked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'isp_addon'


class Licence(models.Model):
    licence_key = models.CharField(max_length=29)
    show_message = models.IntegerField()
    update_available = models.IntegerField()
    reshare_deny_addon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licence'


class LoginFlood(models.Model):
    username = models.CharField(max_length=128)
    ip = models.CharField(max_length=64)
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_flood'


class LoginLogs(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    data = models.TextField()
    login_ip = models.CharField(max_length=255)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login_logs'


class MagClaims(models.Model):
    mag_id = models.IntegerField()
    stream_id = models.IntegerField()
    real_type = models.CharField(max_length=10)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mag_claims'


class MagDevices(models.Model):
    mag_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    bright = models.IntegerField()
    contrast = models.IntegerField()
    saturation = models.IntegerField()
    aspect = models.TextField()
    video_out = models.CharField(max_length=20)
    volume = models.IntegerField()
    playback_buffer_bytes = models.IntegerField()
    playback_buffer_size = models.IntegerField()
    audio_out = models.IntegerField()
    mac = models.CharField(max_length=50)
    ip = models.CharField(max_length=20, blank=True, null=True)
    ls = models.CharField(max_length=20, blank=True, null=True)
    ver = models.CharField(max_length=300, blank=True, null=True)
    lang = models.CharField(max_length=50, blank=True, null=True)
    locale = models.CharField(max_length=30)
    city_id = models.IntegerField(blank=True, null=True)
    hd = models.IntegerField()
    main_notify = models.IntegerField()
    fav_itv_on = models.IntegerField()
    now_playing_start = models.IntegerField(blank=True, null=True)
    now_playing_type = models.IntegerField()
    now_playing_content = models.CharField(max_length=50, blank=True, null=True)
    time_last_play_tv = models.IntegerField(blank=True, null=True)
    time_last_play_video = models.IntegerField(blank=True, null=True)
    hd_content = models.IntegerField()
    image_version = models.CharField(max_length=350, blank=True, null=True)
    last_change_status = models.IntegerField(blank=True, null=True)
    last_start = models.IntegerField(blank=True, null=True)
    last_active = models.IntegerField(blank=True, null=True)
    keep_alive = models.IntegerField(blank=True, null=True)
    playback_limit = models.IntegerField()
    screensaver_delay = models.IntegerField()
    stb_type = models.CharField(max_length=20)
    sn = models.CharField(max_length=255, blank=True, null=True)
    last_watchdog = models.IntegerField(blank=True, null=True)
    created = models.IntegerField()
    country = models.CharField(max_length=5, blank=True, null=True)
    plasma_saving = models.IntegerField()
    ts_enabled = models.IntegerField(blank=True, null=True)
    ts_enable_icon = models.IntegerField()
    ts_path = models.CharField(max_length=35, blank=True, null=True)
    ts_max_length = models.IntegerField()
    ts_buffer_use = models.CharField(max_length=15)
    ts_action_on_exit = models.CharField(max_length=20)
    ts_delay = models.CharField(max_length=20)
    video_clock = models.CharField(max_length=10)
    rtsp_type = models.IntegerField()
    rtsp_flags = models.IntegerField()
    stb_lang = models.CharField(max_length=15)
    display_menu_after_loading = models.IntegerField()
    record_max_length = models.IntegerField()
    plasma_saving_timeout = models.IntegerField()
    now_playing_link_id = models.IntegerField(blank=True, null=True)
    now_playing_streamer_id = models.IntegerField(blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    device_id2 = models.CharField(max_length=255, blank=True, null=True)
    hw_version = models.CharField(max_length=255, blank=True, null=True)
    parent_password = models.CharField(max_length=20)
    spdif_mode = models.IntegerField()
    show_after_loading = models.CharField(max_length=60)
    play_in_preview_by_ok = models.IntegerField()
    hdmi_event_reaction = models.IntegerField()
    mag_player = models.CharField(max_length=20, blank=True, null=True)
    play_in_preview_only_by_ok = models.CharField(max_length=10)
    watchdog_timeout = models.IntegerField()
    fav_channels = models.TextField()
    tv_archive_continued = models.TextField()
    tv_channel_default_aspect = models.CharField(max_length=255)
    last_itv_id = models.IntegerField()
    units = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)
    lock_device = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mag_devices'


class MagEvents(models.Model):
    status = models.IntegerField()
    mag_device_id = models.IntegerField()
    event = models.CharField(max_length=20)
    need_confirm = models.IntegerField()
    msg = models.TextField()
    reboot_after_ok = models.IntegerField()
    auto_hide_timeout = models.IntegerField(blank=True, null=True)
    send_time = models.IntegerField()
    additional_services_on = models.IntegerField()
    anec = models.IntegerField()
    vclub = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mag_events'


class MagLogs(models.Model):
    mag_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mag_logs'


class MemberGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.TextField()
    group_color = models.CharField(max_length=7)
    is_banned = models.IntegerField()
    is_admin = models.IntegerField()
    is_reseller = models.IntegerField()
    total_allowed_gen_trials = models.IntegerField()
    total_allowed_gen_in = models.CharField(max_length=255)
    delete_users = models.IntegerField()
    allowed_pages = models.TextField()
    can_delete = models.IntegerField()
    reseller_force_server = models.IntegerField()
    create_sub_resellers_price = models.FloatField()
    create_sub_resellers = models.IntegerField()
    alter_packages_ids = models.IntegerField()
    alter_packages_prices = models.IntegerField()
    reseller_client_connection_logs = models.IntegerField()
    reseller_assign_pass = models.IntegerField()
    allow_change_pass = models.IntegerField()
    allow_import = models.IntegerField()
    allow_export = models.IntegerField()
    reseller_trial_credit_allow = models.IntegerField()
    edit_mac = models.IntegerField()
    edit_isplock = models.IntegerField()
    reset_stb_data = models.IntegerField()
    reseller_bonus_package_inc = models.IntegerField()
    allow_download = models.IntegerField()
    minimum_trial_credits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member_groups'


class MovieContainers(models.Model):
    container_id = models.AutoField(primary_key=True)
    container_extension = models.CharField(max_length=255)
    container_header = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'movie_containers'


class Packages(models.Model):
    package_name = models.CharField(max_length=255)
    is_trial = models.IntegerField()
    is_official = models.IntegerField()
    trial_credits = models.FloatField()
    official_credits = models.FloatField()
    trial_duration = models.IntegerField()
    trial_duration_in = models.CharField(max_length=255)
    official_duration = models.IntegerField()
    official_duration_in = models.CharField(max_length=255)
    groups = models.TextField()
    bouquets = models.TextField()
    can_gen_mag = models.IntegerField()
    only_mag = models.IntegerField()
    output_formats = models.TextField()
    is_isplock = models.IntegerField()
    max_connections = models.IntegerField()
    is_restreamer = models.IntegerField()
    force_server_id = models.IntegerField()
    can_gen_e2 = models.IntegerField()
    only_e2 = models.IntegerField()
    forced_country = models.CharField(max_length=2)
    lock_device = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'packages'


class PanelLogs(models.Model):
    log_message = models.TextField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'panel_logs'


class RegUserlog(models.Model):
    owner = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    date = models.IntegerField()
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'reg_userlog'


class RegUsers(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ip = models.CharField(max_length=255, blank=True, null=True)
    date_registered = models.IntegerField()
    verify_key = models.TextField(blank=True, null=True)
    last_login = models.IntegerField(blank=True, null=True)
    member_group_id = models.IntegerField()
    verified = models.IntegerField()
    credits = models.FloatField()
    notes = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    default_lang = models.TextField()
    reseller_dns = models.TextField()
    owner_id = models.IntegerField()
    override_packages = models.TextField(blank=True, null=True)
    google_2fa_sec = models.CharField(max_length=50)
    dark_mode = models.IntegerField()
    sidebar = models.IntegerField()
    expanded_sidebar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reg_users'


class ResellerImex(models.Model):
    reg_id = models.IntegerField()
    header = models.TextField()
    data = models.TextField()
    accepted = models.IntegerField()
    finished = models.IntegerField()
    bouquet_ids = models.TextField()

    class Meta:
        managed = False
        db_table = 'reseller_imex'


class RtmpIps(models.Model):
    ip = models.CharField(unique=True, max_length=255)
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'rtmp_ips'


class Series(models.Model):
    title = models.CharField(max_length=255)
    category_id = models.IntegerField(blank=True, null=True)
    cover = models.CharField(max_length=255)
    cover_big = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    plot = models.TextField()
    cast = models.TextField()
    rating = models.IntegerField()
    director = models.CharField(max_length=255)
    releasedate = models.CharField(db_column='releaseDate', max_length=255)  # Field name made lowercase.
    last_modified = models.IntegerField()
    tmdb_id = models.IntegerField()
    seasons = models.TextField()
    episode_run_time = models.IntegerField()
    backdrop_path = models.TextField()
    youtube_trailer = models.TextField()

    class Meta:
        managed = False
        db_table = 'series'


class SeriesEpisodes(models.Model):
    season_num = models.IntegerField()
    series_id = models.IntegerField()
    stream_id = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'series_episodes'


class ServerActivity(models.Model):
    source_server_id = models.IntegerField()
    dest_server_id = models.IntegerField()
    stream_id = models.IntegerField()
    pid = models.IntegerField(blank=True, null=True)
    bandwidth = models.IntegerField()
    date_start = models.IntegerField()
    date_end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_activity'


class Settings(models.Model):
    id = models.IntegerField(primary_key=True)
    bouquet_name = models.TextField()
    live_streaming_pass = models.TextField()
    email_verify_sub = models.TextField()
    email_verify_cont = models.TextField()
    email_forgot_sub = models.TextField()
    email_forgot_cont = models.TextField()
    mail_from = models.TextField()
    smtp_host = models.TextField()
    smtp_port = models.IntegerField()
    min_password = models.IntegerField()
    username_strlen = models.IntegerField()
    username_alpha = models.IntegerField()
    allow_multiple_accs = models.IntegerField()
    allow_registrations = models.IntegerField()
    server_name = models.TextField()
    smtp_username = models.TextField()
    smtp_password = models.TextField()
    email_new_pass_sub = models.TextField()
    logo_url = models.TextField()
    email_new_pass_cont = models.TextField()
    smtp_from_name = models.TextField()
    confirmation_email = models.IntegerField()
    smtp_encryption = models.TextField()
    unique_id = models.TextField()
    copyrights_removed = models.IntegerField()
    copyrights_text = models.TextField()
    default_timezone = models.CharField(max_length=255)
    default_locale = models.CharField(max_length=20)
    allowed_stb_types = models.TextField()
    client_prebuffer = models.IntegerField()
    split_clients = models.CharField(max_length=255)
    stream_max_analyze = models.IntegerField()
    show_not_on_air_video = models.IntegerField()
    not_on_air_video_path = models.TextField()
    show_banned_video = models.IntegerField()
    banned_video_path = models.TextField()
    show_expired_video = models.IntegerField()
    expired_video_path = models.TextField()
    mag_container = models.CharField(max_length=255)
    probesize = models.IntegerField()
    allowed_ips_admin = models.TextField()
    block_svp = models.IntegerField()
    allow_countries = models.TextField()
    user_auto_kick_hours = models.IntegerField()
    show_in_red_online = models.IntegerField()
    disallow_empty_user_agents = models.IntegerField(blank=True, null=True)
    show_all_category_mag = models.IntegerField()
    default_lang = models.TextField(blank=True, null=True)
    autobackup_status = models.IntegerField()
    autobackup_pass = models.TextField()
    flood_limit = models.IntegerField()
    flood_ips_exclude = models.TextField()
    reshare_deny_addon = models.IntegerField()
    restart_http = models.IntegerField()
    css_layout = models.CharField(max_length=255)
    flood_seconds = models.IntegerField()
    flood_max_attempts = models.IntegerField()
    flood_apply_clients = models.IntegerField()
    flood_apply_restreamers = models.IntegerField()
    backup_source_all = models.IntegerField()
    flood_get_block = models.IntegerField()
    portal_block = models.IntegerField()
    streaming_block = models.IntegerField()
    stream_start_delay = models.IntegerField()
    hash_lb = models.IntegerField()
    vod_bitrate_plus = models.IntegerField()
    read_buffer_size = models.IntegerField()
    tv_channel_default_aspect = models.CharField(max_length=255)
    playback_limit = models.IntegerField()
    show_tv_channel_logo = models.IntegerField()
    show_channel_logo_in_preview = models.IntegerField()
    enable_connection_problem_indication = models.IntegerField()
    enable_pseudo_hls = models.IntegerField()
    vod_limit_at = models.IntegerField()
    client_area_plugin = models.CharField(max_length=255)
    persistent_connections = models.IntegerField()
    record_max_length = models.IntegerField()
    total_records_length = models.IntegerField()
    max_local_recordings = models.IntegerField()
    allowed_stb_types_for_local_recording = models.TextField()
    allowed_stb_types_rec = models.TextField()
    show_captcha = models.IntegerField()
    dynamic_timezone = models.IntegerField()
    stalker_theme = models.CharField(max_length=255)
    rtmp_random = models.IntegerField()
    api_ips = models.TextField()
    crypt_load_balancing = models.CharField(max_length=255)
    use_buffer = models.IntegerField()
    restreamer_prebuffer = models.IntegerField()
    audio_restart_loss = models.IntegerField()
    stalker_lock_images = models.TextField()
    channel_number_type = models.CharField(max_length=25)
    stb_change_pass = models.IntegerField()
    enable_debug_stalker = models.IntegerField()
    online_capacity_interval = models.SmallIntegerField()
    always_enabled_subtitles = models.IntegerField()
    test_download_url = models.CharField(max_length=255)
    xc_support_allow = models.IntegerField()
    e2_arm7a = models.CharField(max_length=255)
    e2_mipsel = models.CharField(max_length=255)
    e2_mips32el = models.CharField(max_length=255)
    e2_sh4 = models.CharField(max_length=255)
    e2_arm = models.CharField(max_length=255)
    api_pass = models.CharField(max_length=255)
    message_of_day = models.TextField()
    double_auth = models.IntegerField()
    mysql_remote_sec = models.IntegerField()
    enable_isp_lock = models.IntegerField()
    show_isps = models.IntegerField()
    userpanel_mainpage = models.TextField()
    save_closed_connection = models.IntegerField()
    client_logs_save = models.IntegerField()
    get_real_ip_client = models.CharField(max_length=255)
    case_sensitive_line = models.IntegerField()
    county_override_1st = models.IntegerField()
    disallow_2nd_ip_con = models.IntegerField()
    firewall = models.IntegerField()
    new_sorting_bouquet = models.IntegerField()
    split_by = models.CharField(max_length=255)
    use_mdomain_in_lists = models.IntegerField()
    use_https = models.TextField()
    priority_backup = models.IntegerField()
    use_buffer_table = models.IntegerField()
    tmdb_api_key = models.TextField()
    toggle_menu = models.IntegerField()
    mobile_apps = models.IntegerField()
    stalker_container_priority = models.TextField()
    gen_container_priority = models.TextField()
    tmdb_default = models.CharField(max_length=3)
    series_custom_name = models.IntegerField()
    mag_security = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'settings'


class Signals(models.Model):
    signal_id = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    server_id = models.IntegerField()
    rtmp = models.IntegerField()
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'signals'


class StreamCategories(models.Model):
    category_type = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    cat_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stream_categories'


class StreamLogs(models.Model):
    stream_id = models.IntegerField()
    server_id = models.IntegerField()
    date = models.IntegerField()
    error = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'stream_logs'


class StreamSubcategories(models.Model):
    sub_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    subcategory_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'stream_subcategories'


class StreamingServers(models.Model):
    server_name = models.CharField(max_length=255)
    domain_name = models.CharField(max_length=255)
    server_ip = models.CharField(max_length=255, blank=True, null=True)
    vpn_ip = models.CharField(max_length=255)
    ssh_password = models.TextField(blank=True, null=True)
    ssh_port = models.IntegerField(blank=True, null=True)
    diff_time_main = models.IntegerField()
    http_broadcast_port = models.IntegerField()
    total_clients = models.IntegerField()
    system_os = models.CharField(max_length=255, blank=True, null=True)
    network_interface = models.CharField(max_length=255)
    latency = models.FloatField()
    status = models.IntegerField()
    enable_geoip = models.IntegerField()
    geoip_countries = models.TextField()
    last_check_ago = models.IntegerField()
    can_delete = models.IntegerField()
    server_hardware = models.TextField()
    total_services = models.IntegerField()
    persistent_connections = models.IntegerField()
    rtmp_port = models.IntegerField()
    geoip_type = models.CharField(max_length=13)
    isp_names = models.TextField()
    isp_type = models.CharField(max_length=13)
    enable_isp = models.IntegerField()
    boost_fpm = models.IntegerField()
    http_ports_add = models.TextField()
    network_guaranteed_speed = models.IntegerField()
    https_broadcast_port = models.IntegerField()
    https_ports_add = models.TextField()
    whitelist_ips = models.TextField()
    watchdog_data = models.TextField()
    timeshift_only = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'streaming_servers'
        unique_together = (('server_ip', 'http_broadcast_port'),)


class Streams(models.Model):
    type = models.IntegerField()
    category_id = models.IntegerField(blank=True, null=True)
    stream_display_name = models.TextField()
    stream_source = models.TextField(blank=True, null=True)
    stream_icon = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created_channel_location = models.IntegerField(blank=True, null=True)
    enable_transcode = models.IntegerField()
    transcode_attributes = models.TextField()
    custom_ffmpeg = models.TextField()
    movie_propeties = models.TextField(blank=True, null=True)
    movie_subtitles = models.TextField()
    read_native = models.IntegerField()
    target_container = models.TextField(blank=True, null=True)
    stream_all = models.IntegerField()
    remove_subtitles = models.IntegerField()
    custom_sid = models.CharField(max_length=150, blank=True, null=True)
    epg_id = models.IntegerField(blank=True, null=True)
    channel_id = models.CharField(max_length=255, blank=True, null=True)
    epg_lang = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField()
    auto_restart = models.TextField()
    transcode_profile_id = models.IntegerField()
    pids_create_channel = models.TextField()
    cchannel_rsources = models.TextField()
    gen_timestamps = models.IntegerField()
    added = models.IntegerField()
    series_no = models.IntegerField()
    direct_source = models.IntegerField()
    tv_archive_duration = models.IntegerField()
    tv_archive_server_id = models.IntegerField()
    tv_archive_pid = models.IntegerField()
    movie_symlink = models.IntegerField()
    redirect_stream = models.IntegerField()
    rtmp_output = models.IntegerField()
    number = models.IntegerField()
    allow_record = models.IntegerField()
    probesize_ondemand = models.IntegerField()
    custom_map = models.TextField()
    external_push = models.TextField()
    delay_minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'streams'


class StreamsArguments(models.Model):
    argument_cat = models.CharField(max_length=255)
    argument_name = models.CharField(max_length=255)
    argument_description = models.TextField()
    argument_wprotocol = models.CharField(max_length=255, blank=True, null=True)
    argument_key = models.CharField(max_length=255)
    argument_cmd = models.CharField(max_length=255, blank=True, null=True)
    argument_type = models.CharField(max_length=255)
    argument_default_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streams_arguments'


class StreamsOptions(models.Model):
    stream_id = models.IntegerField()
    argument_id = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streams_options'


class StreamsSeasons(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_name = models.CharField(max_length=255)
    stream_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'streams_seasons'


class StreamsSys(models.Model):
    server_stream_id = models.AutoField(primary_key=True)
    stream_id = models.IntegerField()
    server_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    to_analyze = models.IntegerField()
    stream_status = models.IntegerField()
    stream_started = models.IntegerField(blank=True, null=True)
    stream_info = models.TextField()
    monitor_pid = models.IntegerField(blank=True, null=True)
    current_source = models.TextField(blank=True, null=True)
    bitrate = models.IntegerField(blank=True, null=True)
    progress_info = models.TextField()
    on_demand = models.IntegerField()
    delay_pid = models.IntegerField(blank=True, null=True)
    delay_available_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streams_sys'
        unique_together = (('stream_id', 'server_id'),)


class StreamsTypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    type_key = models.CharField(max_length=255)
    type_output = models.CharField(max_length=255)
    live = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'streams_types'


class SubresellerSetup(models.Model):
    reseller = models.IntegerField()
    subreseller = models.IntegerField()
    status = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subreseller_setup'


class SuspiciousLogs(models.Model):
    user_id = models.IntegerField()
    data = models.TextField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'suspicious_logs'


class Tickets(models.Model):
    member_id = models.IntegerField()
    title = models.CharField(max_length=255)
    status = models.IntegerField()
    admin_read = models.IntegerField()
    user_read = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tickets'


class TicketsReplies(models.Model):
    ticket_id = models.IntegerField()
    admin_reply = models.IntegerField()
    message = models.TextField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tickets_replies'


class TmdbAsync(models.Model):
    type = models.IntegerField()
    stream_id = models.IntegerField()
    status = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tmdb_async'


class TranscodingProfiles(models.Model):
    profile_id = models.AutoField(primary_key=True)
    profile_name = models.CharField(max_length=255)
    profile_options = models.TextField()

    class Meta:
        managed = False
        db_table = 'transcoding_profiles'


class UserActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    stream_id = models.IntegerField()
    server_id = models.IntegerField()
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    user_ip = models.CharField(max_length=39)
    container = models.CharField(max_length=50)
    date_start = models.IntegerField()
    date_end = models.IntegerField(blank=True, null=True)
    geoip_country_code = models.CharField(max_length=22)
    isp = models.CharField(max_length=255)
    external_device = models.CharField(max_length=255)
    divergence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_activity'


class UserActivityNow(models.Model):
    activity_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    stream_id = models.IntegerField()
    server_id = models.IntegerField()
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    user_ip = models.CharField(max_length=39)
    container = models.CharField(max_length=50)
    pid = models.IntegerField(blank=True, null=True)
    date_start = models.IntegerField()
    date_end = models.IntegerField(blank=True, null=True)
    geoip_country_code = models.CharField(max_length=22)
    isp = models.CharField(max_length=255)
    external_device = models.CharField(max_length=255)
    divergence = models.IntegerField(blank=True, null=True)
    hls_last_read = models.IntegerField(blank=True, null=True)
    hls_end = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_activity_now'


class UserOutput(models.Model):
    user_id = models.IntegerField()
    access_output_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_output'


class Users(models.Model):
    member_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    exp_date = models.IntegerField(blank=True, null=True)
    admin_enabled = models.IntegerField()
    enabled = models.IntegerField()
    admin_notes = models.TextField()
    reseller_notes = models.TextField()
    bouquet = models.TextField()
    max_connections = models.IntegerField()
    is_restreamer = models.IntegerField()
    allowed_ips = models.TextField()
    allowed_ua = models.TextField()
    is_trial = models.IntegerField()
    created_at = models.IntegerField()
    created_by = models.IntegerField()
    pair_id = models.IntegerField(blank=True, null=True)
    is_mag = models.IntegerField()
    is_e2 = models.IntegerField()
    force_server_id = models.IntegerField()
    is_isplock = models.IntegerField()
    as_number = models.CharField(max_length=30, blank=True, null=True)
    isp_desc = models.TextField(blank=True, null=True)
    forced_country = models.CharField(max_length=3)
    is_stalker = models.IntegerField()
    bypass_ua = models.IntegerField()
    play_token = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'


class WatchCategories(models.Model):
    type = models.IntegerField()
    genre_id = models.IntegerField()
    genre = models.CharField(max_length=64)
    category_id = models.IntegerField()
    bouquets = models.CharField(max_length=4096)

    class Meta:
        managed = False
        db_table = 'watch_categories'


class WatchFolders(models.Model):
    type = models.CharField(max_length=32)
    directory = models.CharField(max_length=2048)
    server_id = models.IntegerField()
    category_id = models.IntegerField()
    bouquets = models.CharField(max_length=4096)
    last_run = models.IntegerField()
    active = models.IntegerField()
    disable_tmdb = models.IntegerField()
    ignore_no_match = models.IntegerField()
    auto_subtitles = models.IntegerField()
    fb_bouquets = models.CharField(max_length=4096)
    fb_category_id = models.IntegerField()
    allowed_extensions = models.CharField(max_length=4096)

    class Meta:
        managed = False
        db_table = 'watch_folders'


class WatchOutput(models.Model):
    type = models.IntegerField()
    server_id = models.IntegerField()
    filename = models.CharField(max_length=4096)
    status = models.IntegerField()
    stream_id = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'watch_output'


class WatchSettings(models.Model):
    read_native = models.IntegerField()
    movie_symlink = models.IntegerField()
    auto_encode = models.IntegerField()
    transcode_profile_id = models.IntegerField()
    scan_seconds = models.IntegerField()
    percentage_match = models.IntegerField()
    ffprobe_input = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'watch_settings'


class XtreamMain(models.Model):
    update_available = models.IntegerField()
    root_ip = models.TextField()

    class Meta:
        managed = False
        db_table = 'xtream_main'
