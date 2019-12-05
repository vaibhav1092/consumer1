from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from adminpage.consume_api import *

allActors = []
def get_all_actors():
    global allActors
    if len(allActors) == 0:
        allActors = get_all_actors_info()


allMovies = []
def get_all_movies():
    global allMovies
    if len(allMovies)==0:
        allMovies=get_all_movies_info()


def movie_actor_assign(req):
    print('invoked')
    if req.method=='POST':
        print(req.POST)
        assign_actors_to_movie(req.POST["movie"],req.POST.getlist("actors"))
    return render(req,"assign.html",
                  {
                      "movies" : get_all_movies_info(),
                    "actors" : get_all_actors_info()
                   })