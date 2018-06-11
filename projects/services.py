import json

class ProjectService():

    @classmethod
    def all(cls, model):
        return model.objects.all()


    @classmethod
    def get(cls, model, id):
        return model.objects.get(pk=id)


    @classmethod
    def create(cls, model, attributes):
        instance = model()
        json_object = json.loads(attributes)
        keys = json_object.keys()

        for key in keys:
            setattr(instance, key, json_object[key])

        instance.save()
        return instance


    @classmethod
    def update(cls, model, id, attributes):
        instance = model.objects.get(pk=id)
        json_object = json.loads(attributes)
        keys = json_object.keys()

        for key in keys:
            setattr(instance, key, json_object[key])

        instance.save()
        return instance

    @classmethod
    def destroy(cls, model, id):
        instance = model.objects.get(pk=id)
        return instance.delete()


class Response():
    
    def __init__(self, content, success, status):
        self.__content = content
        self.__success = success
        self.__status = status

    def get_content(self):
        return self.__content

    def get_success(self):
        return self.__content

    def get_status(self):
        return self.__content
