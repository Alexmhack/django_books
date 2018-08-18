# django_books
books library made in django which uses heroku postgres, api for books, review system and much more

# Creating postgres database
1. Navigate to https://www.heroku.com/, and create an account if you don’t already have one.
2. On Heroku’s Dashboard, click “New” and choose “Create new app.”
3. Give your app a name, and click “Create app.”
4. On your app’s “Overview” page, click the “Configure Add-ons” button.
5. In the “Add-ons” section of the page, type in and select “Heroku Postgres.”
6. Choose the “Hobby Dev - Free” plan, which will give you access to a free PostgreSQL database that will support up to 10,000 rows of data. Click “Provision.”
7. Now, click the “Heroku Postgres :: Database” link.
8. You should now be on your database’s overview page. Click on “Settings”, and then “View Credentials.” This is the information you’ll need to log into your database. You can access the database via Adminer, filling in the server (the “Host” in the credentials list), your username (the “User”), your password, and the name of the database, all of which you can find on the Heroku credentials page.
9. Alternatively, if you install PostgreSQL on your own computer, you should be able to run psql URI on the command line, where the URI is the link provided in the Heroku credentials list.

```
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'all-credentials-from-heroku',
'USER': 'user',
'PASSWORD': 'password',
'HOST': 'host',
'PORT': 'port',
```

Don't upload your credentials anywhere, use them from environ variables or read them from any file.
