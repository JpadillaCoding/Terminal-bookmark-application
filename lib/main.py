from peewee import *


def home_page():

    print("Welcome to your Bookmark collector!")
    print("Homepage navigations: \n#1 Create a new Bookmark \n#2 Go to your Bookmark collection")

    homepage_response = None

    while homepage_response not in [1, 2]:
        homepage_response = int(
            input("Type in the page you'd like to navigate to"))

        if homepage_response == 1:
            create_bookmark()
        elif homepage_response == 2:
            bookmarks()


def bookmarks():
    print("bookmarks page")


def create_bookmark():
    print("create page")


home_page()
