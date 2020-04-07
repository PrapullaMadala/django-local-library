import pytest

from catalogapp.models import Author


@pytest.mark.django_db
class TestAuthor:
    def test_author_instance(self):
        author = Author.objects.create(first_name='prapulla', last_name='madala')
        assert author.first_name == 'prapulla'
        assert author.last_name == 'madala'


