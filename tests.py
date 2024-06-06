from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize('book', ['House of leaves', 'Маникюр для покойника', '123'])
    def test_add_book_book_added(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert book in collector.get_books_genre().keys()

    @pytest.mark.parametrize('book', ['', None, 123, 'name longer than 41 symbols name longer than 41 symbols'])
    def test_add_wrong_book_book_not_added(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert not book in collector.get_books_genre().keys()

    def test_add_book_second_time_book_not_added(self, collection_2books):
        collection_2books.add_new_book('King in yellow')
        assert len(collection_2books.get_books_genre()) == 2

    @pytest.mark.parametrize('book, genre', [['House of leaves', 'Ужасы'], ['Маникюр для покойника', 'Детективы']])
    def test_add_genre_added_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_get_books_by_genre_returns_right_book(self, collection_2books):
        collection_2books.add_new_book('Вредные советы')
        collection_2books.set_book_genre('Вредные советы', 'Комедии')
        assert 'Вредные советы' in collection_2books.get_books_with_specific_genre('Комедии')

    def test_get_books_for_children_returns_only_children(self, collection_2books):
        collection_2books.add_new_book('Вредные советы')
        collection_2books.set_book_genre('Вредные советы', 'Комедии')
        assert len(collection_2books.get_books_for_children()) == 2

    def test_add_and_delete_book_from_favorites(self, collection_2books):
        collection_2books.add_book_in_favorites('King in yellow')
        assert 'King in yellow' in collection_2books.get_list_of_favorites_books()
        collection_2books.delete_book_from_favorites('King in yellow')
        assert not 'King in yellow' in collection_2books.get_list_of_favorites_books()
