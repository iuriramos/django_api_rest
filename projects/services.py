from .serializers import ProjectSerializer
import json

class ProjectService():

    @classmethod
    def all(cls, model):
        instance = model.objects.all()
        serializer = ProjectSerializer(instance=instance, many=True)
        return serializer.data


    @classmethod
    def get(cls, model, id):
        instance = model.objects.get(pk=id)
        serializer = ProjectSerializer(instance=instance, many=False)
        return serializer.data


    @classmethod
    def create(cls, model, attributes):
        instance = model()
        json_object = json.loads(attributes)
        keys = json_object.keys()

        for key in keys:
            setattr(instance, key, json_object[key])

        instance.save()
        serializer = ProjectSerializer(instance=instance, many=False)

        return serializer.data


    @classmethod
    def update(cls, model, id, attributes):
        instance = model.objects.get(pk=id)
        json_object = json.loads(attributes)
        keys = json_object.keys()

        for key in keys:
            setattr(instance, key, json_object[key])

        instance.save()
        serializer = ProjectSerializer(instance=instance, many=False)

        return serializer.data


    @classmethod
    def destroy(cls, model, id):
        instance = model.objects.get(pk=id)
        return instance.delete()


class Response():
    
    def __init__(self, content, success, status):
        self.__content__ = content
        self.__success__ = success
        self.__status__  = status


    def get_content(self):
        return self.__content


    def get_success(self):
        return self.__content


    def get_status(self):
        return self.__content
