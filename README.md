# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Setting up Trello API Integration

This app uses the Trello API for sharing the tool itels. You'll need to setup 
* A Trello account with a Trello Board and generate 
* An API key Token

once you have done this you'll need to update the '.env' file to include your Trello details

## Running the App Locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Test Suite
To run the tests for the codebase run the following command:
```
poetry run pytest
```
(Please make sure you have run `poetry install` beforehand to install `pytest`)

If instead you'd like to run your test via Docker please run the following
```bash
docker build --tag todo-app:test --target test .
docker run todo-app:test
```

## Building and running the App via Docker
To build the container for local development, please run
```bash
docker build --tag todo-app:dev --target deveopment .

```
To run the container for local development, please run
```bash
docker run --env-file .env --publish 5001:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```

For the production container the build and run commands are:
```bash
docker build --tag todo-app:prod --target production .
docker run --publish 5001:5000 -it --env-file .env todo-app:prod
```

## Diagrams
Architecture diagrams can be found in the `diagrams1 subfolder. They were built using [app.diagrams.net] (app.diagrams.net)(you can use the `.draw.io` file to edit these diagrams).

## Azure Hosting
The container image that us deployed to Azure is hosted on Docker hub at https://hub.docker.com/repository/docker/abhilashjagityla1/abhilash16-todo-app/general

The website itself is hosted at https://abhilashjagitylaappservice.azurewebsites.net/ 

To update the website you will need to run the following commands to build and push the updated container image:

``bash
docker build --tag abhilashjagityla1/abhilash16-todo-app --target production .
docker push abhilashjagityla1/abhilash16-todo-app
```

Next you will need to make a POST request to the webhook link provided on the app Service (under the Deployment Centre tab). This will trigger Azure to pull the updated image from Docker Hub.