from Models.blog import Blog
from database import Database


class Menu(object):

    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    # find one blogs that has the user name, and return True or False
    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    # ask user to create a blog
    def _prompt_user_for_account(self):
        title = input("Enter the blog title: ")
        description = input("Enter the blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo() # assign blog to user_blog
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blogs()
            pass
        elif read_or_write == 'W':
             self.user_blog.new_post()
        else:
            print("Thank you, for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={}) # return a cursor first element of list

        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        # blog_to_see will be id of blog, will get it from_mongo
        blog_to_see = input("Enter the ID of the blog you'd like to see: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))
