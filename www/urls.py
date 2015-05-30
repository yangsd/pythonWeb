__author__ = 'sdyang'

from www.base.tables import User
from www.base.web import get, post, ctx, view, interceptor, seeother, notfound
import os, re, time, base64, hashlib, logging
import markdown2
from apis import api, Page, APIError, APIValueError, APIPermissionError, APIResourceNotFoundError
from config import configs

@view('test_users.html')
@get('/')
def test_users():
    users = User.find_all()
    return dict(users=users)

@view('register.html')
@get('/register')
def register():
    return dict()

@view('signin.html')
@get('/signin')
def signin():
    return dict()