import json
from pprint import pprint

# movies_movie의 id값에 접근
# 각 id 값으로 요청을 보내 json파일 받아오기 (https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=en-US)
# name, profile_path, character 추출하기, movie 컬럼에 movie_id 넣기

# SELECT id FROM movies_movie;
movie_id_list = [129, 238, 240, 278, 389, 424, 497, 680, 19404, 255709, 283566, 335983, 370172, 372058, 385128, 436969, 438631, 441130, 451048, 459151, 496243, 508943, 512195, 522402, 524434, 532067, 550988, 566525, 568620, 574060, 580489, 585245, 589754, 610253, 618162, 630004, 632632, 634649, 635302, 639721, 644479, 645788, 672582, 675319, 696374, 703771, 714968, 724089, 744275, 761053, 762469, 763164, 768449, 775943, 796499, 843241, 849938, 854442,871964, 885110]

import requests
from tmdb import TMDBHelper

API_KEY = '6756a6f5a02fa599f7f6c9c3afdc2e5d'

tmdb_helper = TMDBHelper(API_KEY)

idx = 1
actors = []
for movie_id in movie_id_list:
    request_url = tmdb_helper.get_request_url(method=f'/movie/{movie_id}/credits', language='ko-KR')
    # base_json = open('movies/data/actors/actors.json', encoding='UTF8')
    data = requests.get(request_url).json()
    
    infos = data['crew']
    for info in infos:
        if info['known_for_department'] == 'Directing':
            item = {}
            item['model'] = "movies.director"
            item['pk'] = idx
            item['fields'] = {}
            item['fields']['movie_id'] = movie_id
            item['fields']['name'] = info['name']
            item['fields']['profile_path'] = info['profile_path']
            actors.append(item)
            idx += 1
            break
file_path = 'movies/fixtures/directors.json'
with open(file_path, 'w') as outfile:
    json.dump(actors, outfile, indent=4)




# movie_json = open('movies/data/popular_movies_1.json', encoding='UTF8')
# # movie_json = open('movies/data/top_rated_movies.json', encoding='UTF8')
# # movie_json = open('movies/data/now_playing_movies.json', encoding='UTF8')
# # movie_json = open('movies/data/popular_movies_2.json', encoding='UTF8')
# movie_dict = json.load(movie_json)
# materials = movie_dict['results']


# fixt = []
# for i in range(len(materials)):
#     fs = materials[i]
#     del fs['backdrop_path']
#     del fs['original_language']
#     del fs['original_title']
#     del fs['popularity']
#     del fs['video']
#     el = {}
#     el['model'] = 'movies.movie'
#     el['pk'] = i+1
#     el['fields'] = fs
#     fixt.append(el)

# file_path = "movies/fixtures/outfile.json"
# with open(file_path, 'w') as outfile2:
#     json.dump(fixt, outfile2, indent=4)