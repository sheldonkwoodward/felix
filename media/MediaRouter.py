# sheldon woodward
# 6/13/18


class MediaRouter:
    """
        A router to control all database operations on models in the
        media application.
        """
    def db_for_read(self, model, **hints):
        """
        Attempts to read media models go to media.db.
        """
        if model._meta.app_label == 'media':
            return 'media'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write media models go to media.db.
        """
        if model._meta.app_label == 'media':
            return 'media'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the media app is involved.
        """
        if obj1._meta.app_label == 'media' or obj2._meta.app_label == 'media':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the media app only appears in the media.db
        database.
        """
        if app_label == 'media':
            return db == 'media'
        return None