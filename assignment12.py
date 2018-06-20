'''#Q1
An access token is an object that describes the security context of a process or thread

sign in to developer accoun
creat a new api
under that go to keys and access token
generate access token



#Q2
google ip address=172.217.15.68
facebook ip address=31.13.69.230'''

#Q3
import tweepy
from keys import Consumer_Key,Consumer_Secret,Access_Secret,Access_Token

oauth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
print(api.search("#akshay kumar"))



'''#Q4
API is a part of library which defines how an application communicates with external code.
API can be written in any language.
      
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along
with a large collection of high-level mathematical functions to operate on these arrays.'''


#Q5
import tweepy
from keys import Consumer_Key,Consumer_Secret,Access_Secret,Access_Token

oauth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
user=api.get_user("sonalis97649695")
print (user.screen_name)
print (user.friends_count)


