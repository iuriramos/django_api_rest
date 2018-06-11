# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db  import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def all(self):
    #     return ModelUtils.all(self)
    #
    #
    # def get(self, id):
    #     return ModelUtils.get(self, id)
    #
    #
    # def create(self, json_object):
    #     return ModelUtils.create(self, json_object)
    #
    #
    # def update(self, id, json_object):
    #     return ModelUtils.update(self, id, json_object)
    #
    #
    # def destroy(self):
    #     return ModelUtils.destroy(self)


    def __str__(self):
        return self.title
