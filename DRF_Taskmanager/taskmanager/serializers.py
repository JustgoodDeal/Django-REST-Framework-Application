from rest_framework import serializers
from taskmanager.models import User, Project, Task


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','email','password','role','projects','task',)
        read_only_fields = ('task','projects')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'], 
                    role=validated_data['role'],)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url','title','users','tasks')

class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url','title','description','due_date','project','user')

