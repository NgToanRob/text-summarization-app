# Chatbot using webhook in Django

## Folder structure

This repository contains a Django project packaged in Docker Compose with PostgreSQL, PgAdmin4, and Nginx. The project structure is as follows:

```linux
├── app
│   ├── chatbot
│   ├── db.sqlite3
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   ├── .dockerignore
│   ├── entrypoint.prod.sh
│   ├── entrypoint.sh
│   ├── facebook
│   ├── manage.py
│   ├── requirements.txt
│   └── static
├── data
├── docker-compose.prod.yml
├── docker-compose.yml
├── .env.dev
├── .env.prod
├── .env.prod.db
├── .gitignore
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
└── README.md
```

The `app` folder contains the Django project, with the `chatbot` app as the main application. The `Dockerfile` and `Dockerfile.prod` files are used to build the Docker images for development and production environments respectively. The `entrypoint.sh` and `entrypoint.prod.sh` scripts are used as entry points for the containers. The `requirements.txt` file contains the Python dependencies required for the project.

The `data` folder is used to persist the PostgreSQL database data.

The `docker-compose.yml` file is used to set up the development environment, and the `docker-compose.prod.yml `file is used for the production environment. The .`env.dev` and `.env.prod` files contain environment variables for the development and production environments respectively. The `.env.prod.db `file contains the PostgreSQL environment variables for the production environment.

The `nginx` folder contains the Nginx configuration and `Dockerfile` for serving the static files and proxying requests to the Django application.

## Running the Project

To run the project, first make sure that Docker and Docker Compose are installed on your system.

For the development environment, build/re-build and run in the background following command:

```
docker-compose up -d --build
```

For the production environment, build/re-build and run in the background following command:

```
docker-compose -f docker-compose.prod.yml up -d --build
```

The application will be available at [http://localhost:8000](http://localhost:8000) (development) or [http://localhost:<NGINX_PORT>](http://localhost:1337) (production).

PgAdmin4 is available at[http://localhost:<PGADMIN_PORT>](http://localhost:8080). The default email and password are `admin@chatbot.com` and `12345` respectively.

## Contributing

If you want to contribute to this project, please create a pull request with your changes.

## Development Process

1. Run ngrok to generate URL:
   Run ngrok container and access to [localhost:4040](localhost:4040) to get ULR which has ssl (https://)
2. Add `DJANGO_ALLOWED_HOSTS` in `env.dev` file
3. Update Messenger Profile Properties with Postman

```json
curl -X POST -H "Content-Type: application/json" -d '{
    "whitelisted_domains": [
            "<New generated URL in Step 1>"
        ],

}' "https://graph.facebook.com/v16.0/me/messenger_profile?access_token=<PAGE_ACCESS_TOKEN>"
```




