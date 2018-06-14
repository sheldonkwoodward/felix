# sheldon woodward
# 6/13/18


class WikiRouter:
    """
        A router to control all database operations on models in the
        wiki application.
        """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to wiki.db.
        """
        if model._meta.app_label == 'wiki':
            return 'wiki'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to wiki.db.
        """
        if model._meta.app_label == 'wiki':
            return 'wiki'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'wiki' or obj2._meta.app_label == 'wiki':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the wiki app only appears in the wiki.db
        database.
        """
        if app_label == 'wiki':
            return db == 'wiki'
        return None