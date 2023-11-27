from django.urls import path
from .views import NoteCreateView, NoteUpdateView, NoteDeleteView, NoteDetailView

urlpatterns = [
    path('playground/create/', NoteCreateView.as_view(), name='note_create'),
    path('playground/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('playground/<int:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('playground/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]