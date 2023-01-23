import requests

def popular_count():
    pass 
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : 'b4ddf663645312b787e1c5de3538d0f7',
        'language' : 'ko-KR',
        'region' : 'KR'
    }
    res = requests.get(URL+path,params=params).json()
    response = len(res.get('results'))
    return response

if __name__ == '__main__':
    print(popular_count())