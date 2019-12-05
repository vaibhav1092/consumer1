import requests
from adminpage.pyobjects import *
BASE_URI = "http://localhost:8000/v1/producer/"



def create_movie(mvinfo):
    respnose = requests.post(BASE_URI+'movies/',json=mvinfo.__dict__)
    print(respnose.status_code)
    print(respnose.json())

#create_movie(m1)

TOKEN='Token 2c6806b6dc784df81ee5404a4a4ab2ef44273827'
TOKEN_VAL = {"Authorization":TOKEN}

def create_actor(actorinfo):
    respnose = requests.post(BASE_URI + 'actors/', json=actorinfo.__dict__,headers=TOKEN_VAL)
    print(respnose.status_code)
    print(respnose.json())


def update_movie(movieinfo):
    respnose = requests.put(BASE_URI + 'movies/'+str(movieinfo.id)+"/", json=movieinfo.__dict__,headers=TOKEN_VAL)
    print(respnose.status_code)
    print(respnose.json())


def update_actor(actorinfo):
    respnose = requests.put(BASE_URI + 'actors/' + str(actorinfo.id)+"/", json=actorinfo.__dict__,headers=TOKEN_VAL)
    #print(respnose.status_code)
    #print(respnose.json())


def delete_movie(mid):
    respnose = requests.delete(BASE_URI + 'movies/'+str(mid)+'/',headers=TOKEN_VAL)
    #print(respnose.status_code)
    #print(respnose.json())


def delete_actor(actid):
    respnose = requests.delete(BASE_URI + 'actors/' + str(actid) + '/',headers=TOKEN_VAL)
    #print(respnose.status_code)
    #print(respnose.json())


def get_single_movie(mid):
    respnose = requests.get(BASE_URI + 'movies/'+str(mid))
    #print(respnose.status_code)
    #print(respnose.json())


def get_single_actor(actid):
    respnose = requests.get(BASE_URI + 'actors/'+str(actid))
    #print(respnose.status_code)
    #print(respnose.json())


def get_all_movies_info():
    respnose = requests.get(BASE_URI + 'movies/')
    #print(respnose.status_code)
    #print(respnose.json())
    return respnose.json()

def get_all_actors_info():
    respnose = requests.get(BASE_URI + 'actors/')
    #print(respnose.status_code)
    #print(respnose.json())
    return respnose.json()
def assign_actors_to_movie(mid,actorids):
    print(mid,"--MVID")
    print(actorids,'--ACTORIDs')
    values = {
        "movieid":mid,
        "actorids":actorids
    }
    response = requests.post(BASE_URI+'/custom/assign/',json=values)
    #print(response.status_code)
    #print(response.text)

def get_actor_movies(actorid):
    #ideally shud be get
    response = requests.post(BASE_URI+'/custom/actormvs/',json={"id":actorid})
    #print(response.json())

def get_allactors_of_movie(mvid):
    response = requests.post(BASE_URI + '/custom/mvactors/', json={"id": mvid})
    #print(response.json())


if __name__ == '__main__':
    pass
    m1 = Movie(id=7, nm='war', rw='4Str', ct='A')
    # create_movie(m1)
    update_movie(m1)
    #delete_movie(2)
    #get_single_movie(1)
    # ac1 = Actor(id=2,nm='akshay',exp=4)
    # create_actor(ac1)
    #update_actor(ac1)
    # delete_actor(7)
    #get_single_actor(1)
    # assign_actors_to_movie(1,[4,5,7])
    #get_actor_movies(4)
    # get_allactors_of_movie(1)