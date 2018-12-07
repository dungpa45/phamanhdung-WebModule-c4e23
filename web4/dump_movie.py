import mlab 
from models.movie import Movie
from models.user import User

mlab.connect()
# Movie.drop_collection() de xoa collection

for movie in Movie.objects():
    print(movie.title, movie.user.username,sep=": ")
