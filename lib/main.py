from peewee import *

db = PostgresqlDatabase(
    'bookmark',
    user='postgres',
    password='',
    host='localhost',
    port='5432'
)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Bookmark(BaseModel):
    title = CharField()
    url = CharField()
    description = CharField()


db.create_tables([Bookmark])

def home_page():
    print("\n" + "-"*50)
    print("Welcome to your Bookmark collector!")
    print("Homepage navigations: \n#1 Create a new Bookmark \n#2 Go to your Bookmark collection")
    print("-"*50)

    homepage_response = None

    while homepage_response not in [1, 2]:
        homepage_response = int(input("Type in the page you'd like to navigate to: "))

        if homepage_response == 1:
            create_bookmark()
        elif homepage_response == 2:
            bookmarks()


def create_bookmark():
    print("Create Bookmarks Here")
    title = input("Type your bookmark title: ")
    url = input("Type the bookmark URL: ")
    description = input("Type a brief description of your bookmark: ")

    bookmark = Bookmark( title=title, url=url, description=description )
    bookmark.save()


def bookmarks():
    print("bookmarks page")


home_page()
