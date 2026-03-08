class Movie:
    country = 'USA'
    isOscarWinner = False
    def __init__(self, genre : str, sucsess: bool, age_limit: int, based_book: bool,title: str) -> None:
        self.genre = genre
        self.sucsess = sucsess
        self.age_limit = age_limit
        self.based_book = based_book
        self.title = title

    def __len__(self) -> str:
        return f'Фильм {self.title} не рекомендуется к просмотру лицам младше {self.age_limit} лет'

    def allow_watch(self, age: int) -> bool:
        return age >= self.age_limit

    def multy_genre(self,new_genre: str) -> str:
        return self.genre +' ,' +new_genre

    def multy_country(self,new_country: str) -> str:
        return self.country +' ,' +new_country

    def book_author(self, author:str) -> str:
        if self.based_book == True:
            return f'Фильм {self.title} основан на книге {author}'
movie1 = Movie('Триллер', True, 18, True, 'Бойцовский клуб')
movie2 = Movie('Романтика', True, 16, False, 'Титаник')

print(movie1.__len__())
print(movie2.allow_watch(18))
print(movie2.multy_genre('Трагедия'))


