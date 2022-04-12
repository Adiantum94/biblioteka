import random
from datetime import date

today = date.today()

class Production:
   def __init__(self, title, year, genre, views):
       self.title = title
       self.year = year
       self.genre = genre
       self.views = views

   def __str__(self):
    return f'"{self.title}" ({self.year}){self.views}' 

   def play(self):
    self.views += 1

class Movie(Production):
   pass
   
class Series(Production):
   def __init__(self, season, episode, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.season = season 
       self.episode = episode      
   def __str__(self):
    return f'"{self.title}" S{self.season}E{self.episode} {self.views}'

def get_movies():
  movies=[]
  for i in library:
   if isinstance(i, Movie):
       movies.append(i)
  by_title = sorted(movies, key=lambda movie: movie.title)
  for i in by_title:
        print(i)

def get_series():
  series=[]
  for i in library:
   if isinstance(i, Series):
       series.append(i)
  by_title = sorted(series, key=lambda serie: serie.title)
  for i in by_title:
        print(i)

def search(title):
    for i in library:
        if i.title == title:
            print(i)

def generate_views():
    choice= random.choice(library)
    choice.views= choice.views + random.randint(1, 100)

def multiple_generate_views():
    for i in range(11):
        generate_views()

def top_titles( content_type, value):
    if content_type == "movie":
      movies=[]
      for i in library:
        if isinstance(i, Movie):
          movies.append(i)
      by_views = sorted(movies, key=lambda movie: movie.views)
      by_views = by_views[::-1]
      top_views = by_views[:value]
      for i in top_views:
        print(i)

    elif content_type == "series":
      series=[]
      for i in library:
        if isinstance(i, Series):
          series.append(i)
      by_views = sorted(series, key=lambda serie: serie.views)
      by_views = by_views[::-1]
      top_views = by_views[:value]
      for i in top_views:
        print(i) 

PulpFiction = Movie(title= 'Pulp Fiction', year= '1994', genre= 'criminal', views= 0) 
Friends = Series(title='Friends', year='1994', genre='comedy', views=0, season='10', episode='24')   
HarryPotter = Movie(title= 'Harry Potter', year= '2001', genre= 'fantasy', views= 0)
Titanic = Movie(title= 'Titanic', year= '1997', genre= 'melodramat', views= 0)
Lost = Series(title='Lost', year='2004', genre='thriller', views=0, season='06', episode='24')
FightClub = Movie(title= 'Fight Club', year= '1999', genre= 'thriller', views= 0)
Inception = Movie(title= 'Inception', year= '2010', genre= 'sci-fi', views= 0)
GameofThrones = Series(title='Game of Thrones', year='2011', genre='fantasy', views=0, season='08', episode='10')
ThorRagnarok = Movie(title= 'Thor: Ragnarok', year= '2017', genre= 'fantasy', views= 0)
StrangerThings = Series(title='Stranger Things', year='2016', genre='sci-fi', views=0, season='04', episode='09')
BigHero6 = Movie(title= 'Big Hero 6', year= '2014', genre= 'animation', views= 0)
RickandMorty = Series(title='Rick and Morty', year='2013', genre='comedy', views=0, season='05', episode='10')
TheMartian = Movie(title= 'The Martian', year= '2015', genre= 'sci-fi', views= 0)
Arcane = Series(title='Arcane', year='2021', genre='fantasy', views=0, season='01', episode='09')
BlackMirror = Series(title='Black Mirror', year='2011', genre='sci-fi', views=0, season='05', episode='06')
Sherlock = Series(title='Sherlock', year='2010', genre='criminal', views=0, season='04', episode='03')

library=[PulpFiction, Friends, HarryPotter, Titanic, Lost, FightClub, Inception, GameofThrones, ThorRagnarok, StrangerThings, BigHero6, RickandMorty, TheMartian, Arcane, BlackMirror, Sherlock]


print("BIBLIOTEKA FILMÓW")
print('FILMY:')
get_movies()
print('SERIALE:')
get_series()
multiple_generate_views()
print(f'NAJPOPULARNIEJSZE FILMY DNIA {today}:')
top_titles( "movie", 3)
print(f'NAJPOPULARNIEJSZE SERIALE DNIA {today}:')
top_titles( "series", 3)