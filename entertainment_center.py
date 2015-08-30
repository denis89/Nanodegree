import media
# Den media.py file wird importiert.
toy_story = media.Movie("Toy Story", "A Story of a boy and his toys that come to life", 
  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "www.youtube.com/watch?v=4Itwjtj6mwg")
#print(toy_story.storyline)
# filename.classname()
  #It's outside the python library.


avatar = media.Movie("Avatar", "A marine on","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "www.youtube.com/watch?v=4Itwjtj6mwg" )
#print(avatar.storyline)     
# avatar and toy_story are instances of the class Movie
#avatar.show_trailer()

transporter = avatar = media.Movie("Transporter", "An exciting action movie.","https://cdn2.thedissolve.com/articles/1434/detail.bad589e2.jpg", "www.youtube.com/watch?v=0poXFSvX0_4" )
transporter.show_trailer()
