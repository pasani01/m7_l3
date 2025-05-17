from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,   
    ListAPIView
)
from .permissions import isOwnerOrSuperuser
from rest_framework.permissions import IsAuthenticated
from .serializers import AuthorListSerializer, AuthorDetailSerializer, AuthorCreateSerializer
from .models import Author



class AuthorCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'
    filterset_fields = [ 'brith_date',]
    search_fields = ['name']
    

class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = [isOwnerOrSuperuser]
    lookup_field = 'slug'

