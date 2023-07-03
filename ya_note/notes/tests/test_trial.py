from django.test import TestCase

from notes.models import Note


class TestNote(TestCase):
    # Все нужные переменные сохраняем в атрибуты класса.
    TITLE = 'Заголовок новости'
    TEXT = 'Тестовый текст'


    @classmethod
    def setUpTestData(cls):
        cls.news = Note.objects.create(
            # При создании объекта обращаемся к константам класса через cls.
            title=cls.TITLE,
            text=cls.TEXT,
        )

    def test_successful_creation(self):
        note_count = Note.objects.count()
        self.assertEqual(note_count, 1)

    def test_title(self):
        # Чтобы проверить равенство с константой -
        # обращаемся к ней через self, а не через cls:
        self.assertEqual(self.note.title, self.TITLE) 