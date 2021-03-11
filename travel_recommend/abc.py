# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_no = models.AutoField(primary_key=True)
    admin_id = models.CharField(max_length=20)
    admin_passwd = models.CharField(max_length=20)
    admin_name = models.CharField(max_length=20)
    admin_jik = models.CharField(max_length=20, blank=True, null=True)
    admin_acc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    first_name = models.CharField(max_length=150)
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


class Board(models.Model):
    num = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=4000, blank=True, null=True)
    bwrite = models.DateField(blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class Buser(models.Model):
    buser_no = models.IntegerField(primary_key=True)
    buser_name = models.CharField(max_length=10)
    buser_loc = models.CharField(max_length=10, blank=True, null=True)
    buser_tel = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buser'


class Cardinfo(models.Model):
    card_ownerid = models.ForeignKey('User', models.DO_NOTHING, db_column='card_ownerid', blank=True, null=True)
    card_owner = models.CharField(max_length=20, blank=True, null=True)
    card_comp = models.CharField(max_length=20, blank=True, null=True)
    card_no = models.CharField(max_length=20, blank=True, null=True)
    card_passwd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cardinfo'


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


class Faqboard(models.Model):
    faq_no = models.AutoField(db_column='FAQ_NO', primary_key=True)  # Field name made lowercase.
    faq_title = models.CharField(db_column='FAQ_TITLE', max_length=50)  # Field name made lowercase.
    faq_content = models.TextField(db_column='FAQ_CONTENT')  # Field name made lowercase.
    faq_date = models.DateTimeField(db_column='FAQ_DATE')  # Field name made lowercase.
    faq_type = models.CharField(db_column='FAQ_TYPE', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faqboard'


class Gogek(models.Model):
    gogek_no = models.IntegerField(primary_key=True)
    gogek_name = models.CharField(max_length=10)
    gogek_tel = models.CharField(max_length=20, blank=True, null=True)
    gogek_jumin = models.CharField(max_length=14, blank=True, null=True)
    gogek_damsano = models.ForeignKey('Jikwon', models.DO_NOTHING, db_column='gogek_damsano', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gogek'


class Inquery(models.Model):
    inq_no = models.AutoField(primary_key=True)
    inq_title = models.CharField(max_length=50)
    inq_context = models.TextField(blank=True, null=True)
    inq_ddate = models.DateTimeField(blank=True, null=True)
    inq = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    inq_gnum = models.IntegerField(blank=True, null=True)
    inq_onum = models.IntegerField(blank=True, null=True)
    inq_nested = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inquery'


class Jikwon(models.Model):
    jikwon_no = models.IntegerField(primary_key=True)
    jikwon_name = models.CharField(max_length=10)
    buser_num = models.IntegerField()
    jikwon_jik = models.CharField(max_length=10, blank=True, null=True)
    jikwon_pay = models.IntegerField(blank=True, null=True)
    jikwon_ibsail = models.DateField(blank=True, null=True)
    jikwon_gen = models.CharField(max_length=4, blank=True, null=True)
    jikwon_rating = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jikwon'


class Newbook(models.Model):
    nb_no = models.AutoField(primary_key=True)
    nb_name = models.CharField(max_length=30)
    nb_author = models.CharField(max_length=50, blank=True, null=True)
    nb_inter = models.CharField(max_length=20, blank=True, null=True)
    nb_genre = models.CharField(max_length=20)
    nb_comp = models.CharField(max_length=20, blank=True, null=True)
    nb_bdate = models.DateTimeField(blank=True, null=True)
    nb_stock = models.IntegerField(blank=True, null=True)
    nb_price = models.IntegerField(blank=True, null=True)
    nb_scount = models.IntegerField(blank=True, null=True)
    nb_readcnt = models.IntegerField(blank=True, null=True)
    nb_plot = models.TextField()
    nb_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newbook'


class ObFile(models.Model):
    idx = models.AutoField(primary_key=True)
    ob_no = models.IntegerField()
    original_file_name = models.CharField(max_length=260)
    stored_file_name = models.CharField(max_length=36)
    file_size = models.IntegerField(blank=True, null=True)
    ob_rdate = models.DateField()
    del_gb = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ob_file'


class Oldbook(models.Model):
    ob_no = models.AutoField(primary_key=True)
    ob_name = models.CharField(max_length=30)
    ob_author = models.CharField(max_length=50)
    ob_inter = models.CharField(max_length=50, blank=True, null=True)
    ob_genre = models.CharField(max_length=20)
    ob_comp = models.CharField(max_length=20)
    ob_bdate = models.DateTimeField(blank=True, null=True)
    ob_state = models.CharField(max_length=20, blank=True, null=True)
    ob_price = models.IntegerField()
    ob_scount = models.IntegerField(blank=True, null=True)
    ob_readcnt = models.IntegerField(blank=True, null=True)
    ob_donor = models.CharField(max_length=20, blank=True, null=True)
    ob_comment = models.CharField(max_length=30, blank=True, null=True)
    ob_image = models.CharField(max_length=100, blank=True, null=True)
    ob_ddate = models.DateTimeField(blank=True, null=True)
    ob_userid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oldbook'


class Orderinfo(models.Model):
    order_no = models.AutoField(primary_key=True)
    orderlist_no = models.CharField(max_length=20)
    order_person = models.CharField(max_length=20)
    order_id = models.CharField(max_length=20, blank=True, null=True)
    order_bookno = models.IntegerField()
    order_booktype = models.CharField(max_length=5)
    order_date = models.DateTimeField()
    order_passwd = models.CharField(max_length=20, blank=True, null=True)
    order_scount = models.IntegerField()
    order_paytype = models.CharField(max_length=5)
    order_state = models.CharField(max_length=10)
    order_sum = models.IntegerField()
    order_address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'orderinfo'


class Rentinfo(models.Model):
    rent_no = models.IntegerField(blank=True, null=True)
    rent_id = models.CharField(max_length=20)
    rent_sdate = models.DateTimeField()
    rent_edate = models.DateTimeField()
    rent_ecount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rentinfo'


class Review(models.Model):
    review_no = models.AutoField(primary_key=True)
    review = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    review_bookno = models.ForeignKey(Newbook, models.DO_NOTHING, db_column='review_bookno', blank=True, null=True)
    review_context = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    review_rate = models.IntegerField(blank=True, null=True)
    review_gonggam = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'


class Travel(models.Model):
    tourid = models.IntegerField(db_column='tourId', primary_key=True)  # Field name made lowercase.
    city = models.CharField(max_length=10, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    genre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel'


class Treview(models.Model):
    treview_no = models.AutoField(primary_key=True)
    treview_id = models.CharField(max_length=20, blank=True, null=True)
    tourid = models.IntegerField(db_column='tourId', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treview'


class Tuser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=10, blank=True, null=True)
    user_pwd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tuser'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=20)
    user_passwd = models.CharField(max_length=30)
    user_tel = models.CharField(max_length=20)
    user_addr = models.CharField(max_length=100)
    user_zip = models.CharField(max_length=10)
    user_mail = models.CharField(max_length=30)
    user_rentcnt = models.IntegerField(blank=True, null=True)
    user_point = models.IntegerField(blank=True, null=True)
    user_birth = models.CharField(max_length=20)
    user_penalty = models.IntegerField(blank=True, null=True)
    user_dcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
