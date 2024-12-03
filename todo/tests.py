from django.test import TestCase
from .models import TodoItem

class TodoModelTest(TestCase):
    def setUp(self):
        TodoItem.objects.create(title='Test Task', description='Description of Test Task')

    def test_todo_creation(self):
        task = TodoItem.objects.get(title='Test Task')
        self.assertEqual(task.title, 'Test Task')
