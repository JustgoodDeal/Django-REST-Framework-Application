from django.test import TestCase
from rest_framework.test import APITestCase
from taskmanager.models import User, Project, Task

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.manager = User.objects.create(username='Petr', password='12345678q', email='any@mail.ru', role='Manager')
        self.developer = User.objects.create(username='Andy', password='12345678w', email='anyother@mail.ru', role='Developer')              
        self.client.force_authenticate(user=self.manager)
            
    def test_creation(self):             
        petr = User.objects.filter(username='Petr')
        self.assertEqual(petr.count(), 1)

    def test_get_method(self):
        url = 'http://127.0.0.1:8000/api/v1/taskmanager/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_method_for_manager(self):
        url = 'http://127.0.0.1:8000/api/v1/taskmanager/projects/'
        first_project = {'title':'first_project'}
        response = self.client.post(url, first_project)
        self.assertEqual(response.status_code, 201)

    def test_post_method_for_developer(self):
        self.client.force_authenticate(user=self.developer)
        url = 'http://127.0.0.1:8000/api/v1/taskmanager/projects/'
        second_project = {'title':'second_project'}
        response = self.client.post(url, second_project)
        self.assertEqual(response.status_code, 403)        

class RelationshipsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Roger', password='12345678c', email='my@mail.ru', role='Manager')       
        self.project = Project.objects.create(title='fast_project')        
        self.project.users.add(self.user)
        self.task = Task.objects.create(title='quick_task', description='Make it popular', due_date='2020-07-15', project=self.project, user=self.user)
        
    def test_creation(self):             
        self.assertEqual(User.objects.filter(username='Roger').count(), 1)
        self.assertEqual(Project.objects.filter(title='fast_project').count(), 1)
        self.assertEqual(Task.objects.filter(title='quick_task').count(), 1)

    def test_relationships(self):
        #self.assertEqual(self.task.project.title, self.project.title)
        #self.assertEqual(self.project.tasks.all()[0].title, self.task.title)
        self.assertEqual(Task.objects.filter(project__title='fast_project').count(), 1)        
        self.assertEqual(Task.objects.filter(user__username='Roger').count(), 1)
        self.assertEqual(Project.objects.filter(users__username='Roger').count(), 1)

    def test_relationships_after_removal(self):
        self.task.delete()
        self.assertEqual(Task.objects.filter(user__username='Roger').count(), 0)
        self.assertEqual(self.project.tasks.all().count(), 0)
        self.project.delete()
        self.assertEqual(Project.objects.filter(users__username='Roger').count(), 0)
        self.assertEqual(self.user.projects.all().count(), 0)
