# ToDo application

A ToDo application with the ability to log in and register a user, create and manage tasks.

## Installation

To get started with the application you need to complete following steps:

- Install dependencies:

```shell
$ pip install -r requirements.txt
```

- Provide details for your PostgreSQL database in `assignment/settings.py` file to `DATABASES` variable.

- Run application:

```shell
$ python3 manage.py runserver 8000
```

## Usage

The application consists of two modules:

- Auth - authorization module, which responsible for user authentication.
- ToDo - ToDo module, which reponsible for managing current user's tasks.

First things first you have to be logged in to use this application, that's why the authorization module will welcome you. After successful authorization you can access to your ToDo list and start adding your tasks one by one. You could also cross them out by clicking on each task. Tasks will be grouped by their status, those that finished will be in one group and those that not in another.

## Example of usage

This project might be useful for people who love to manage their day, because by listing all your tasks you won't forget anything. This also helps to better manage your time.