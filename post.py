import uuid
from database import Database
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert('posts',
                        self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one('posts', {'id': id})
        return cls(post_data['blog_id'],
                   post_data['title'],
                   post_data['content'],
                   post_data['author'],
                   post_data['created_date'],
                   post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blog_id': id})]
