# Python Bookmark Directory 

## Intro
This application replicates a Bookmark directory that displays the title, description, and the URL. PeeWee and PostgreSQL are used to manage the data. 

## Installation 
* This guide assumes the user already has PostgreSQL and Pipenv set up.

1. clone this repository.
``` 
git clone [LINK]
```
2. Launch the Pipenv shell:
```
pipenv shell
```
3. On a seperate terminal, launch PostgresSQL shell.
```
psql
```
4. Create the PostgreSQL database.
```
CREATE DATABASE bookmark;
```
5. Check to make sure the database is made, then navigate to it. 
```
\l
\c boookmark
```
6. On your Pipenv terminal, launch the program! Program instructions are shown once launched. 
```
python [FilePath]
```

## Features 

* Creating bookmarks
* Searching bookmarks
* Searching by bookmark name

## Future Features

* delete a bookmark
* update a bookmark