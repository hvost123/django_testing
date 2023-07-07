from datetime import date

import pytest
from django.conf import settings
from django.utils import timezone

from conftest import URL

pytestmark = pytest.mark.django_db


def test_news_count_order(client, news_list):
    """Проверка сортировки на главной."""
    response = client.get(URL.home)
    object_list = list(response.context['object_list'])
    assert isinstance(object_list[0].date, date)
    assert object_list == sorted(
        object_list, key=lambda x: x.date, reverse=True
    )


def test_news_count_quantity(client, news_list):
    """Проверка кол-ва новостей на главной."""
    response = client.get(URL.home)
    object_list = list(response.context['object_list'])
    assert len(object_list) == settings.NEWS_COUNT_ON_HOME_PAGE


def test_comments_order(client, news, comments_list):
    """Проверка сортировки комментариев."""
    response = client.get(URL.detail)
    assert 'news' in response.context
    news = response.context['news']
    all_comments = list(news.comment_set.all())
    """
    Не выходит избавится от избыточного приведения типа.
    Возможно не верно понимаю комментарий.
    В пачке не нашел контакта.
    """
    assert isinstance(all_comments[0].created, timezone.datetime)
    assert all_comments == sorted(all_comments, key=lambda x: x.created)


def test_client_has_form(client, admin_client, news):
    """Проверка доступности формы комментария."""
    response = client.get(URL.detail)
    admin_response = admin_client.get(URL.detail)
    assert ('form' in admin_response.context)
    assert ('form' not in response.context)
