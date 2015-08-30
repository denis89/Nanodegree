import webbrowser

class Movie():
  valid_ratings = ["G", "PG", "PG-13", "R"]
   def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube ):
      self.title = movie_title
      self.storyline = movie_storyline
      self.poster_image_url = poster_image
      self.trailer_youtube_url = trailer_youtube
# These are variables
# A function will be declared.
# Self is an argument, which refers to the object.
  def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)
  