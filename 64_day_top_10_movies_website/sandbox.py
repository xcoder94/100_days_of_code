import requests

url = "https://api.themoviedb.org/3/discover/movie"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjY2NlNGNhMDQ1MDFmMGE3NjczNzlhNmNkNDZhNjg5NSIsInN1YiI6IjY1ZGYwZWU1YjM5ZTM1MDE2MzJmOWVlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pcKqyzqB2JuqXfIQEtpKJAPHT8eBPnoH44PitqSEF1Y"
}
params = {
    'include_adult': False,
    'include_video': False,
    'language': 'en-US',
    'page': 1,
    'sort_by': 'popularity.desc'

}
response = requests.get(url, headers=headers, params=params)
response.raise_for_status()
data = response.json()['results']

# print(len(data['results']))
print(data)
