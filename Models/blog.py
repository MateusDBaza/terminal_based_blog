import uuid
from models.post import Post
import datetime
from database import Database

class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave for today(in format DDMMYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        # Would be the id of the blog_id after creation of the post.
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,  # Author the blog is also author of the post
                    date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)  # will get the current post id and return it

    def save_to_mongo(self):  # insert data in the blogs collection
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self): # return data in json format
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])
