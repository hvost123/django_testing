from django.test import TestCase

from notes.models import Note


class TestNote(TestCase):
    TITLE = 'Заголовок новости'
    TEXT = 'Тестовый текст'

    @classmethod
    def setUpTestData(cls):
        cls.news = Note.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
        )

    def test_successful_creation(self):
        note_count = Note.objects.count()
        self.assertEqual(note_count, 1)

    def test_title(self):
        self.assertEqual(self.note.title, self.TITLE)
