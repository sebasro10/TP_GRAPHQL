import json

def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie

def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile)
    return newmovie

def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def actor_with_id(_,info,_id):
    with open('{}/data/actors.json'.format("."), "r") as file:
        actors = json.load(file)
        for actor in actors['actors']:
            if actor['id'] == _id:
                return actor

def get_list_movies(_,info):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        return movies['movies']

def movie_with_title(_,info,_title):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['title'] == _title:
                return movie

def create_movie(_,info,_movie):
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _movie["id"]:
                return {"message":"movie ID already exists"}
    movies['movies'].append(_movie)
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(movies, wfile)
    return {"message":"movie added"}

def delete_movie(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movies['movies'].remove(movie)
                with open('{}/data/movies.json'.format("."), "w") as wfile:
                    json.dump(movies, wfile)
                return movie

def movies_by_director(_,info,_director):
    res = []
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['director'] == _director:
                res.append(movie)
    return res
