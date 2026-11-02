import requests     #It is python library for the APIs
api_url = "https://jsonplaceholder.typicode.com/posts"
response=requests.get(api_url)
print(response)   #<Response [200]> this print status code:- 200 that successfully 
posts=response.json()
# print(posts)   #this print the response in JSONformat

# for post in posts:
#     print(posts)

print(f"Total posts: {len(posts)}") 
print(f"First Post : {posts[0]['title']}")