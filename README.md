# FastAPI Mongo ⚡
A fastAPI mongoDB integrated cookiecutter 🍪 template

---

## ➡️ Installation

    $ pip install cookiecutter
        ...
##
    $ cookiecutter gh:minihut/fastapi-mongo
        project_name [fastapi-mongo]:
        project_slug [fastapi]: 
        project_version [0.1.0]:
        project_short_description [A fastapi-based API for MongoDB]: 
        workers [2]: 
        base [http://127.0.0.1]: 
        port [8080]:
        mongo_url [mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000]: 
        docs_endpoint [/docs]: 
        playground_endpoint [/play]: 
        global_rate_limit_per_second [5]:

- `project_name`: The name of the project.
- `project_slug`: Basically folder name
- `project_version`: The version of the project.
- `project_short_description`: A short description of the project.
- `workers`: The number of workers to use in uvicorn.
- `base`: The base url of the project.
- `port`: The port to be used
- `mongo_url`: The url of the mongoDB server.
- `docs_endpoint`: The endpoint for the docs.
- `playground_endpoint`: The endpoint for the playground.
- `global_rate_limit_per_second`: The global rate limit per second (applies to all endpoints).

## 💻 Support
Create a issue or join the community on [Discord](https://discord.gg/gQ9rcuNK75)

## 📒 CHANGELOG
[See here](CHANGELOG.md)