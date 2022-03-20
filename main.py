class Movie:
   def __init__(self, title, year, genre, views):
       self.title = title
       self.year = year
       self.genre = genre
       self.views = views

   def __str__(self):
    return f'"{self.title}" ({self.year})' 

   def play(self):
    self.views += 1

class Series(Movie):
   def __init__(self, season, episode, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.season = season 
       self.episode = episode      
   def __str__(self):
    return f'"{self.title}" S{self.season}E{self.episode}'
