import requests

fake_blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
blog_response = requests.get(fake_blog_url)
blog_response.raise_for_status()
all_posts = blog_response.json()

for post in all_posts:
    print(post['title'])
    print(post['subtitle'])

print(all_posts)
