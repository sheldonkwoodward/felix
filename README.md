# Felix v1.1


## Description

Felix is a Django web server for my personal use. As of v1.1 it provides an API to read and write data to the media database. This includes information about different movies and TV shows such as title, release year, date added, and other things.


## Installation Guide
After cloning the repo, install the requirements:
```
$ pip3 install -r requirements.txt
```
Now run the Django migrations:
```
$ python3 manage.py migrate
```
This will create the default.db database. After the migrations have been run and the database has been created, a superuser needs to be made so an API token is generated:
```
$ python3 manage.py createsuperuser
```
After the migrations and users have been created the server is ready to run:
```
$ python3 manage.py runserver
```


## Usage
As of v1.1, this app can handle GET requests for movie or season info. It can also handle POST requests to add either of these to the database. All GET and POST requests require a Bearer token to be provided in the header of the request. This token is automatically generated for every Django user and can be foud in <b>default.db</b> under the <b>authtoken_token</b> table. 

### Media GET Requests
Media GET Requests return JSON objects in the following format:
```
{
    "time_stamp": "YYYY-MM-DD HH:MM:SS.xxxxxx",
    "movie_num": NUMBER MATCHED MOVIES,
    "season_num": NUMBER MATCHED SEASONS,
    "episode_num": NUMBER MATCHED EPISODES,
    "movies": [
        {
            "id": ID,
            "title": "TITLE",
            "release_year": YYYY,
            "cut": "CUT",
            "resolution": "RESOLUTION",
            "date_added": "YYYY-MM-DD HH:MM:SS.xxxxxx",
            "length_minutes": MINUTES,
            "path": "PATH"
        },
        ...
    ],
    "seasons": [
        {
            "id": ID,
            "title": "TITLE",
            "season": SEASON,
            "cut": "CUT",
            "resolution": "RESOLUTION",
            "date_added": "YYYY-MM-DD",
            "path": "PATH"
        },
        ...
    ],
     "episodes": [
        {
            "id": ID,
            "title": "TITLE",
            "season": SEASON,
            "episode": EPISODE,
            "cut": "CUT",
            "resolution": "RESOLUTION",
            "date_added": "YYYY-MM-DD",
            "path": "PATH"
        },
        ...
    ]
}
```

#### Query Parameters
All media GET requests can include query parameters in the URL. The query parameters are <b>id</b>, <b>title</b>, <b>release_year</b>, <b>season</b>, <b>episode</b>, <b>cut</b>, <b>resolution</b>, and <b>length_minutes</b>. These parameters are exclusively searched and will not match partially.

#### GET /media/
Returns all movies and seasons in the database.

#### GET /media/\<year>
Returns all movies and seasons in the database that were added in \<year\>.

#### GET /media/\<year>/\<month>
Returns all movies and seasons in the database that were added in \<month> \<year\>.

#### GET /media/\<year>/\<month>/\<day>
Returns all movies and seasons in the database that were added on \<day> \<month> \<year\>.

#### GET /media/minutes/\<minutes>
Returns all movies and seasons in the database that were added within the past \<minutes> minutes.

#### GET /media/hours/\<hours>
Returns all movies and seasons in the database that were added within the past \<hours> hours.

#### GET /media/days/\<days>
Returns all movies and seasons in the database that were added within the past \<days> days.

#### GET /media/weeks/\<weeks>
Returns all movies and seasons in the database that were added within the past \<weeks> weeks.

#### GET /media/months/\<months>
Returns all movies and seasons in the database that were added within the past \<months> months.

#### GET /media/years/\<years>
Returns all movies and seasons in the database that were added within the past \<years> years.


### Media POST Requests
Media POST Requests return JSON objects in the following format:
```
{
    "status": SUCCESS OR FAILURE
}
```

#### POST /media/add/movie
Contains headers with data for the following keys: <b>title</b>, <b>release_year</b>, <b>cut</b>, <b>resolution</b>, <b>length_minutes</b>, and <b>path</b>. This data will be added to the <b>media_movie</b> table in <b>default.db</b> as a new media_movie row.

#### POST /media/add/season
Contains headers with data for the following keys: <b>title</b>, <b>season</b>, <b>cut</b>, <b>resolution</b>, and <b>path</b>. This data will be added to the <b>media_season</b> table in <b>default.db</b> as a new media_season row.

#### POST /media/add/season
Contains headers with data for the following keys: <b>title</b>, <b>season</b>, <b>episode</b>, <b>cut</b>, <b>resolution</b>, and <b>path</b>. This data will be added to the <b>media_episode</b> table in <b>default.db</b> as a new media_episode row.
