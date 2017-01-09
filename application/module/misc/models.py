# -*- coding: utf-8 -*-

from django.db import models


class ExceptionTraceback(models.Model):
    """
    例外ログ
    """
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    user_id = models.CharField(max_length=255, db_index=True, blank=True, default=None)
    view_name = models.CharField(max_length=255, blank=True, default=None)
    request_path = models.CharField(max_length=1024, blank=True, default=None)
    exception_type = models.CharField(max_length=255, blank=True, default=None)
    exception_message = models.TextField(blank=True, default=None)
    traceback_log = models.TextField(blank=True, default=None)
    post_data = models.TextField(blank=True, default=None)
