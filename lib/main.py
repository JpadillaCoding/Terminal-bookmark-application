from peewee import *

postgres_db = PostgresqlDatabase(
    'postgres',
    user='postgres',
    password='',
)

postgres_db.execute_sql('CREATE DATABASE "bookmark"')

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
db.close()

def home_page():
    print("\n" + "-"*50)
    print("Welcome to your Bookmark collector!")
    print("Homepage navigations: \n#1 Create a new Bookmark \n#2 Go to your Bookmark collection \n#3 Exit")
    print("-"*50)

    homepage_response = None

    while homepage_response not in [1, 2,3 ]:
        homepage_response = int(
            input("Type in the page you'd like to navigate to: "))

        if homepage_response == 1: create_bookmark()
        elif homepage_response == 2: bookmarks()
        elif homepage_response == 3: exit()


def create_bookmark():
    print("Create Bookmarks Here")
    title = input("Type your bookmark title: ")
    url = input("Type the bookmark URL: ")
    description = input("Type a brief description of your bookmark: ")

    bookmark = Bookmark(title=title, url=url, description=description)
    bookmark.save()
    print(f"{title} has been saved!")

    create_another = input("Would you like to create another bookmark? (y/n)")
    if create_another == 'y':
        create_bookmark()
    else:
        home_page()


def bookmarks():
    print("Bookmarks page: ")
    print("#1 Show all bookmarks \n#2 Search by name \n#3 Home \n#4 Exit")
    bookmark_response = None

    while bookmark_response not in [1, 2]:
        bookmark_response = int(
            input("Type in the page you'd like to navigate to: "))
        print("="*50)
        print("="*50)

        if bookmark_response == 1:
            bookmarks = Bookmark.select()
            for bookmark in bookmarks:
                print(
                    f"Title: {bookmark.title}: \nURL: {bookmark.url} \nDescription: {bookmark.description}")
                print("\n" + "="*50)
            home_page()
        elif bookmark_response == 2: search_by_title()
        elif bookmark_response == 3: home_page()
        elif bookmark_response == 4: exit()


def search_by_title():

    search_title = input("What is the title of the bookmark? ")
    bookmark = Bookmark.get(Bookmark.title == search_title)
    print(f"Title: {bookmark.title} \nURL: {bookmark.url} \nDescription: {bookmark.description}")

    anotherSearch = input("Would you like to make another Search? (y/n) ")
    if anotherSearch == 'y': search_by_title()
    else: home_page()


home_page()
