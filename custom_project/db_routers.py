class HackcraftdbRouter:
    """
    A router to control all database operations on models in the
    hackcraft application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read hackcraft models go to hackcraft db.
        """
        if model._meta.app_label == 'hackcraft_app':
            return 'hackcraft'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write hackcraft models go to hackcraft db.
        """
        if model._meta.app_label == 'hackcraft_app':
            return 'hackcraft'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the hackcraft app is involved.
        """
        if obj1._meta.app_label == 'hackcraft_app' or \
           obj2._meta.app_label == 'hackcraft_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the hackcraft app only appears in the 'hackcraft'
        database.
        """
        if app_label == 'hackcraft_app':
            return db == 'hackcraft'
        return None
