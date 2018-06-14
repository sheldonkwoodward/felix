# sheldon woodward
# 6/13/18


class WikiDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'wiki':
            return 'wiki'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'wiki':
            return 'wiki'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'wiki' or obj2._meta.app_label == 'wiki':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'wiki':
            return db == 'wiki'
        return None