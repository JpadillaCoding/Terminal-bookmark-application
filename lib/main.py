from peewee import *

def home_page():
    print("Welcome to your Bookmark collector!")
    print("Homepage navigations: \n#1 Create a new Bookmark \n#2 Go to your Bookmark collection")
    homepage_response = int(input("Type the number of which page you'd like to navigate"))

    def home_page_switch(response):
        if response == 1:
            create_bookmark()
        elif response == 2:
            bookmarks()
        else:
            
        
    
def bookmarks():
    print("bookmarks page")

def create_bookmark():
    print("create page")

home_page()

