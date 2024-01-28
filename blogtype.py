from enum import Enum

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


def required_function():
    return {'message':'Learing FastAPI is important'}

