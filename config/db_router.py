class DbRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'core':
            return "default"
        elif model._meta.app_label == 'app1_fuss':
            return "app1_fuss_db"
        elif model._meta.app_label == 'xui':
            return "xui_db"
        elif model._meta.app_label == 'xui_one':
            return "xui_one_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'core':
            return "default"
        elif model._meta.app_label == 'app1_fuss':
            return "app1_fuss_db"
        elif model._meta.app_label == 'xui':
            return "xui_db"
        elif model._meta.app_label == 'xui_one':
            return "xui_one_db"
        return None