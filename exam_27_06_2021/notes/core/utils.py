from notes.note.models import Note
from notes.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()

    return profile


def get_notes_count():
    notes_count = len(Note.objects.all())
    return notes_count