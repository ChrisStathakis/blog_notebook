from django.urls import path
from .views import (NoteHomepageView, validate_new_note_view, NoteUpdateView, pinned_view, delete_note_view,

                    )

app_name = 'notes'

urlpatterns = [
    path('', NoteHomepageView.as_view(), name='home'),
    path('pinned/<int:pk>/', pinned_view, name='pinned'),
    path('validate-note-creation/', validate_new_note_view, name='validate_note_creation'),
    path('note/update/<int:pk>/', NoteUpdateView.as_view(), name='note_update'),
    path('note/delete/<int:pk>/', delete_note_view, name="delete_note"),

]
