from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication
from django.db.models import Q

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.select_related('owner').all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # create: set owner to current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('search')
        status = self.request.query_params.get('status')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if status:
            qs = qs.filter(status=status)
        return qs

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.select_related('owner').all()
    serializer_class = TaskSerializer
    authentication_classes = [ SessionAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
