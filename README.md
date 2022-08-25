# Dreamlancer backend API
Built by MMO & Co.,
The 3 CTOs with a dream.

## About Dreamlancer
<!-- Please pick one -->

This repo contains the backend for project Dreamlancer. Dreamlancer aims to combine the organization of sites like Trello with the usability of sites like Fiverr. Clients will be able to post project listings, that developers can view and bid on. Once an agreement is reached and the client has selected their developer (or developer team), clients will be able to view a roadmap with predefined checkpoints maintained by the developers.


<!-- The goal of Dreamlancer is to provide a one stop shop where clients can request and fulfill their projects with the help of freelance developer(s). Clients will be able to take small peeks as their project is built by their selected development team, a form of transparancy and accountability that is needed in the freelancing world! Developers will be able to update and provide a roadmap as development of a project continues, assuring that no misunderstandings happen along the development process. -->

## About the Dreamlancer API

Dreamlancer is built using a boilerplate `dreamlancer` that provides user authentication, and the app *change this name later*`api`. This API will serve it's React based client: `https://github.com/Zene09/client-dreamlancer`.

### Structure
The `dreamlancer` includes `settings.py` with settings to allow this project to run both locally and on production.

The `api` app provides contains files for models and views in `api/models` and `api/views` that are utilized by `api/urls.py`.

The `.env` contains the `SECRET` and database name used to run the API service locally or for development.

<!-- change all instances of dreamlancer and api to our own naming conventions -->

### Installation and commands

To make use of this API for yourself, please install `gunicorn` and `whitenoise` using the command: `pipenv install gunicorn whitenoise`

To run Django locally please use the cmd:
`pip3 install pipenv pylint pylint-django`

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |

*Note: Windows Users will need to enable USER_PW and password for the database during development.*

### Connecting to Client

This API is standalone and should be able to talk to any client. Dreamlancer uses React for it's front end, but you can use any client you would like.

### Port

The django template uses port `8000` by default, this server location is `http://127.0.0.1:8000/`

### URL syntax

Django defaults to trailing forward slashes on request: `http://127.0.0.1:8000/users/`

### Token syntax

For authentication purposes, a bearer token is required with this syntax and pattern:
```
Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Request Data Into String

Use `axios` to request API and then string using

```
const create = function (data) {
  return axios({
    url: config.apiUrl + '/projects/',
    method: 'POST',
    headers: {
      Authorization: 'Token ' + store.user.token
    },
    data: JSON.stringify(data)
  })
}
```

### Loading JSON data

Example of loading JSON:

```
class Projects(APIView):
    def post(self, request):
        data = json.loads(request.body)
        serializer = MySerializer(data=data['resource'])

```
### Authentication

Depending on the user type || Client or Developer || different options will be available (such as posting/requesting a project or working/developing a project).
This will be handled by the authentication and conditional views.

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up`             | `users#signup`    |
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-password/`  | `users#changepw`  |
| DELETE | `/sign-out/`         | `users#signout`   |
| GET    | `/user/<username>/`        | `users#profile`   |

### Route Tables


| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET   | `/projects/`             | `projects#index`    |
| GET   | `/projects/<int:project_id>/`             | `projects#show`    |
| POST   | `/projects/create`             | `projects#create`    |
| PATCH  | `/projects/<int:pk>/update/` | `projects#update`  |
| DELETE | `/projects/<int:pk>/delete/`        | `projects#delete`   |

<!-- | Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET   | `/client/`             | `client#index`    |
| GET   | `/client/<int:client_id>/`             | `client#show`    |
| POST   | `/client/create`             | `client#create`    |
| PATCH  | `/client/<int:pk>/update/` | `client#update`  |
| DELETE | `/client/<int:pk>/delete/`        | `client#delete`   |

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET   | `/dev/`             | `dev#index`    |
| GET   | `/dev/<int:dev_id>/`             | `dev#show`    |
| POST   | `/dev/create`             | `dev#create`    |
| PATCH  | `/dev/<int:pk>/update/` | `dev#update`  |
| DELETE | `/dev/<int:pk>/delete/`        | `dev#delete`   | -->
## Collaborator Roles
- Kyle Moreno: Back End Dev
- Lyndonna Munro: Front End Dev
- Zene Orr: Team Manager
- Efrain Davila: Front End Dev
