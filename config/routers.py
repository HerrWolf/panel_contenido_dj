# app/config/routers.py

class DefaultRouter:
    """
    Router para la base de datos principal (default).
    """

    def db_for_read(self, model, **hints):
        print('DefaultRouter')
        print(model._meta.app_label)
        if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin'] or \
                obj2._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return db == 'default'
        return None


# class GenericRouter:
#     def __init__(self):
#         pass  # No inicialices aquí
#
#     def db_for_read(self, model, **hints):
#         app_label = getattr(self, 'app_label', None)
#         db_name = getattr(self, 'db_name', None)
#         if app_label and model._meta.app_label == app_label:
#             return db_name
#         return None
#
#     def db_for_write(self, model, **hints):
#         app_label = getattr(self, 'app_label', None)
#         db_name = getattr(self, 'db_name', None)
#         if app_label and model._meta.app_label == app_label:
#             return db_name
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         app_label_router = getattr(self, 'app_label', None)
#         db_name = getattr(self, 'db_name', None)
#         if app_label_router and app_label == app_label_router:
#             return db == db_name
#         return False
#
#
# # Exporta las instancias configuradas
# app1_fuss_router = GenericRouter()
# app1_fuss_router.app_label = 'app1_fuss'
# app1_fuss_router.db_name = 'app1_fuss_db'
#
# xui_router = GenericRouter()
# xui_router.app_label = 'xui'
# xui_router.db_name = 'xui_db'
#
# xui_one_router = GenericRouter()
# xui_one_router.app_label = 'xui_one'
# xui_one_router.db_name = 'xui_one_db'


class App1FussRouter:
    def db_for_read(self, model, **hints):
        print('App1FussRouter')
        print(model._meta.app_label)
        if model._meta.app_label == 'app1_fuss':
            return 'app1_fuss_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1_fuss':
            return 'app1_fuss_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app1_fuss':
            return db == 'app1_fuss_db'
        return False


class XuiRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'xui':
            return 'xui_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'xui':
            return 'xui_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'xui':
            return db == 'xui_db'
        return False


class XuiOneRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'xui_one':
            return 'xui_one_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'xui_one':
            return 'xui_one_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'xui_one':
            return db == 'xui_one_db'
        return False