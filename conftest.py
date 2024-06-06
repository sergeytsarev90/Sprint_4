import pytest
from main import BooksCollector

@pytest.fixture()
def collection_2books():
    collector = BooksCollector()
    collector.add_new_book('King in yellow')
    collector.set_book_genre('King in yellow', 'Ужасы')
    collector.add_new_book('Марсианин')
    collector.set_book_genre('Марсианин', 'Фантастика')

    return collector
