# # news/tests/test_trial.py
# from django.test import TestCase
# import unittest
# from notes.models import Note



# class TestNews(TestCase):
#     # Все нужные переменные сохраняем в атрибуты класса.
#     TITLE = 'Заголовок новости'
#     TEXT = 'Тестовый текст'
    
#     @classmethod
#     def setUpTestData(cls):
#         cls.notes = Note.objects.create(
#             # При создании объекта обращаемся к константам класса через cls.
#             title=cls.TITLE,
#             text=cls.TEXT,
#         )

#     @unittest.skip('Этот тест мы просто пропускаем')
#     def test_successful_creation(self):
#         notes_count = Note.objects.count()
#         self.assertEqual(notes_count, 1)

#     @unittest.skip('Этот тест мы просто пропускаем')
#     def test_title(self):
#         # Чтобы проверить равенство с константой -
#         # обращаемся к ней через self, а не через cls:
#         self.assertEqual(self.notes.title, self.TITLE)