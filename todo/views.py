from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

# Create a To-Do item
class TodoCreateView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Read a single To-Do item
class TodoDetailView(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Read all To-Do items
class TodoListView(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Update a To-Do item
class TodoUpdateView(generics.UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Delete a To-Do item
class TodoDeleteView(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
