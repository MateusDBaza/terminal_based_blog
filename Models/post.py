import uuid
from database import Database
import datetime

class Post(object):

    def __init__(self,blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        # uuid module,uuid4 number 4 is random
        # .hex is to give us 32 character hexadecimal string
        # if we pass and id we use that id else uuid will generate one.
        self.created_date = date

    # insert data to our database collection posts.
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'title': self.title,
            'created_date': self.created_date,
            'content': self.content
        }

    @classmethod
    def from_mongo(cls, id):
        #post.from_mongo('123')
        # get posts from mongodb that belongs to a specific id
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])


    @staticmethod
    def from_blog(id):
        #post.from_mongo('123')
        return [post for post in Database.find(collection='posts', query={'id': id})]
        # return list of post id, if we don't use list comprehension we will have cursor
