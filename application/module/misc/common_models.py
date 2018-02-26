from django.core.cache import cache
from django.db import models


class AbustractCachedModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(AbustractCachedModel, self).save()
        cache.delete(self.get_cache_path(self.id))
        if hasattr(self, 'user_id'):
            cache.delete(self.get_cache_user_path(self.user_id))
        cache.delete(self.get_cache_all_path())

    def delete(self, *args, **kwargs):
        cache.delete(self.get_cache_path(self.id))
        if hasattr(self, 'user_id'):
            cache.delete(self.get_cache_user_path(self.user_id))
        cache.delete(self.get_cache_all_path())
        super(AbustractCachedModel, self).delete()

    @classmethod
    def get_cache_path(cls, pk):
        # classmethodはclassからもinstanceからも呼ばれるので
        if hasattr(cls, '__name__'):
            return '{}/{}/'.format(cls.__name__, pk)
        return '{}/{}/'.format(cls.__class__.__name__, pk)

    @classmethod
    def get_cache_user_path(cls, user_id):
        # classmethodはclassからもinstanceからも呼ばれるので
        if hasattr(cls, '__name__'):
            return '{}/{}/user/'.format(cls.__name__, user_id)
        return '{}/{}/user/'.format(cls.__class__.__name__, user_id)

    @classmethod
    def get_cache_all_path(cls):
        # classmethodはclassからもinstanceからも呼ばれるので
        if hasattr(cls, '__name__'):
            return '{}/all/'.format(cls.__name__)
        return '{}/all/'.format(cls.__class__.__name__)

    @classmethod
    def get_cache(cls, pk):
        cache_path = cls.get_cache_path(pk)
        model = cache.get(cache_path, None)
        if model is None:
            try:
                model = cls.objects.get(pk=pk)
                cache.set(cache_path, model, (3600 * 24))
            except cls.DoesNotExist:
                pass
        return model

    @classmethod
    def get_cache_user(cls, user_id):
        cache_path = cls.get_cache_user_path(user_id)
        models = cache.get(cache_path, None)
        if models is None:
            models = cls.objects.filter(user_id=user_id)
            cache.set(cache_path, models, (3600 * 24))
        return models

    @classmethod
    def get_cache_all(cls):
        cache_path = cls.get_cache_all_path()
        models = cache.get(cache_path, None)
        if models is None:
            models = list(cls.objects.all())
            cache.set(cache_path, models, (3600 * 24))
        return models
