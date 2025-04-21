# from yanote.settings import NEWS_COUNT_ON_HOME_PAGE
# # news/tests/test_content.py
# from django.conf import settings
# from django.test import TestCase
# # Импортируем  reverse(), она понадобится для получения адреса страницы.
# from django.urls import reverse
# # from datetime import datetime, timedelta
# from django.contrib.auth import get_user_model
# # Дополнительно к News импортируем модель комментария.
# from notes.models import Note
# # from django.utils import timezone
# # from notes.forms import CommentForm


# User = get_user_model()


# class TestHomePage(TestCase):
#     LIST_URL = reverse('notes:list')

#     @classmethod
#     def setUpTestData(cls):
#         all_notes = [
#             Note(
#                 title=f'Новость {index}',
#                 text='Просто текст.',
#                 author_id=1,
#                 slug=index,
#                 # Для каждой новости уменьшаем дату на index дней от today,
#                 # где index - счётчик цикла.
#                 # date=today - timedelta(days=index)
#             )
#             for index in range(1, settings.NEWS_COUNT_ON_HOME_PAGE + 1)
#         ]
#         Note.objects.bulk_create(all_notes)
#         cls.author = User.objects.create(username='1')

#     def test_notes_count(self):
#         # Загружаем главную страницу.
#         response = self.client.get(self.LIST_URL, kwargs={'slug': 2})
#         # Код ответа не проверяем, его уже проверили в тестах маршрутов.
#         # Получаем список объектов из словаря контекста.
#         object_list = response.context['object_list']
#         # Определяем количество записей в списке.
#         notes_count = object_list.count()
#         # Проверяем, что на странице именно 10 новостей.
#         self.assertEqual(notes_count, settings.NEWS_COUNT_ON_HOME_PAGE)

#     # def test_notes_order(self):
#     #     response = self.client.get(self.HOME_URL)
#     #     object_list = response.context['object_list']
#     #     # Получаем даты новостей в том порядке,
#               как они выведены на странице.
#     #     all_dates = [notes.date for notes in object_list]
#     #     # Сортируем полученный список по убыванию.
#     #     sorted_dates = sorted(all_dates, reverse=True)
#     #     # Проверяем, что исходный список был отсортирован правильно.
#     #     self.assertEqual(all_dates, sorted_dates)


# # class TestDetailPage(TestCase):

# #     @classmethod
# #     def setUpTestData(cls):
# #         cls.notes = Note.objects.create(
# #             title='Тестовая новость', text='Просто текст.'
# #         )
# #         # Сохраняем в переменную адрес страницы с новостью:
# #         cls.detail_url = reverse('notes:detail', args=(cls.notes.id,))
# #         cls.author = User.objects.create(username='Комментатор')
# #         # Запоминаем текущее время:
# #         now = timezone.now()
# #         # Создаём комментарии в цикле.
# #         for index in range(10):
# #             # Создаём объект и записываем его в переменную.
# #             comment = Comment.objects.create(
# #                 news=cls.notes, author=cls.author, text=f'Tекст {index}',
# #             )
# #             # Сразу после создания меняем время создания комментария.
# #             comment.created = now + timedelta(days=index)
# #             # И сохраняем эти изменения.
# #             comment.save()

# #     def test_comments_order(self):
# #         response = self.client.get(self.detail_url)
# #         # Проверяем, что объект новости находится в словаре контекста
# #         # под ожидаемым именем - названием модели.
# #         self.assertIn('notes', response.context)
# #         # Получаем объект новости.
# #         news = response.context['notes']
# #         # Получаем все комментарии к новости.
# #         all_comments = news.comment_set.all()
# #         # Собираем временные метки всех комментариев.
# #         all_timestamps = [comment.created for comment in all_comments]
# #         # Сортируем временные метки, менять порядок сортировки не надо.
# #         sorted_timestamps = sorted(all_timestamps)
# #         # Проверяем, что временные метки отсортированы правильно.
# #         self.assertEqual(all_timestamps, sorted_timestamps)

# #     def test_anonymous_client_has_no_form(self):
# #         response = self.client.get(self.detail_url)
# #         self.assertNotIn('form', response.context)

#     # def test_authorized_client_has_form(self):
#     #     # Авторизуем клиент при помощи ранее созданного пользователя.
#     #     self.client.force_login(self.author)
#     #     response = self.client.get(self.detail_url)
#     #     self.assertIn('form', response.context)
#     #     # Проверим, что объект формы соответствует нужному классу формы.
#     #     self.assertIsInstance(response.context['form'], CommentForm)
