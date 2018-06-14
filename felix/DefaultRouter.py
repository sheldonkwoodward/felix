# sheldon woodward
# 6/13/18


class DefaultRouter:
    """
        A router to control all database operations on models in the
        default application.
        """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to default.db.
        """
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to default.db.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the default app only appears in the default.db
        database.
        """
        return db == 'default'