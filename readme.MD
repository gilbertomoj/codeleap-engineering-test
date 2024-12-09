[PYTHON_BADGE]: https://img.shields.io/badge/python-fff?style=for-the-badge&logo=python
[DJANGO_BADGE]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django

<h1 align="center" style="font-weight: bold;"> CodeLeap Engineering Test 💻</h1>

![express][PYTHON_BADGE]
![nest][DJANGO_BADGE]

<p align="center">
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> •
 <a href="#contribute">Contribute</a>
</p>

<p align="center">
  <b>Simple description of what your project do or how to use it.</b>
</p>

<h2 id="started">🚀 Getting started</h2>

<h3>Prerequisites</h3>

Here you list all prerequisites necessary for running your project.

- [Python](https://www.python.org)
- [Django](https://www.djangoproject.com)
- [Django Rest Framework](https://www.django-rest-framework.org)
<h3>Cloning the Repository</h3>

Clone this repository to your local machine:

```bash
git clone your-project-url-in-github
```

<h3>Setting Up the Project</h3>

1. Navigate to the project directory
```bash
cd codeleap-test
``````
2. Set up a virtual enviroment
```bash
python -m venv venv
``````
3. Activate the virtual enviroment
```bash
venv\Scripts\activate (Windows)

source venv/Scripts/activate (Linux/macOS)
``````
4. Install project dependencies
```bash
pip install -r requirements.txt
``````
5. Run migrations
```bash
python manage.py migrate
``````
6. Start the development server
```bash
python manage.py runserver
``````
<h2 id="routes">📍 API Endpoints</h2>

Here is a list of the main API routes, along with expected request and response bodies.

| Route          | Description                                        | HTTP Method |
|----------------|----------------------------------------------------|-------------|
| `/list`        | Get a list of all posts                           | GET         |
| `/create`      | Create a new post                                 | POST        |
| `/detail/{id}` | Get details of a specific post                    | GET         |
| `/update/{id}` | Update an existing post                           | PATCH       |
| `/delete/{id}` | Delete a post                                     | DELETE      |


## Posts

### `GET /list`
Fetches all posts.

**Response:**
```json
[
    {
        "id": 1,
        "title": "title post 1",
        "content": "content post 1",
        "username": "user1",
        "created_datetime": "2024-12-09T20:55:46.180280Z"
    },
    {
        "id": 2,
        "title": "title post 2",
        "content": "content post 2",
        "username": "user2",
        "created_datetime": "2024-12-09T20:55:57.235484Z"
    },
    {
        "id": 3,
        "title": "title post 3",
        "content": "content post 3",
        "username": "user3",
        "created_datetime": "2024-12-09T20:56:04.424011Z"
    }
]
```

### `POST /posts`
Creates a new post.

**Request:**
```json
{
    "username": "user1",
    "title": "title post 1",
    "content": "content post 1"
}
```

**Response:**
```json
{
    "id": 1,
    "title": "title post 1",
    "content": "content post 1",
    "username": "user1",
    "created_datetime": "2024-12-09T20:56:04.424011Z"
}
```

### `PATCH /posts/{id}`
Updates an existing post by ID.

**Request:**
```json
{
  "title": "Updated Post",
  "content": "This is the updated content of the post."
}
```

**Response:**
```json
{
    "id": 1,
    "title": "Updated Post",
    "content": "This is the updated content of the post.",
    "username": "user1",
    "created_datetime": "2024-12-09T20:56:04.424011Z"
}
```

### `DELETE /posts/{id}`
Deletes a post by ID.

**Response:**
```json
{}
```
