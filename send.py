import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTM0ODY0NjMyLCJqdGkiOiJmNzUxZjA4MzM5NWY0YTRlODk3MDlmZjFkYWQwZWJkNiIsInVzZXJfaWQiOjF9.f3MqUVxQvQev1AB2sbZTnhyyeis1awmsUyNUCGJppkE'


r = requests.get('http://localhost:8000/paradigms', headers = headers)

print(r.text)