from django.conf.urls import url
from django.db import connection
from clickhouse_driver import Client
from clickhouse_driver import connect
from psycopg2 import connect as psycopg2connect


def show_user(request, username):

    client = Client('localhost')
    client.execute("SELECT * FROM users WHERE username = '%s'" % username)

    Client('localhost').execute("SELECT * FROM users WHERE username = '%s'" % username)

    conn = connect('clickhouse://localhost')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)

    psycopg2conn = psycopg2connect('clickhouse://localhost')
    psycopg2cursor = psycopg2conn.cursor()
    psycopg2cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)

urlpatterns = [url(r'^users/(?P<username>[^/]+)$', show_user)]
