# Text Summarization Web App

## Overview

This is a web app for text summarization. It was created as part of the pre-entrance test for Cinnamon AI Bootcamp. The app has two parts: a demo front end with the Gradio framework, and a back end with Django. The back end also uses two apps for managing the database: PostgreSQL and pgAdmin4. In production, the app also uses an Nginx proxy.

The core tech of this app is [ViT5-Base Finetuned on vietnews Abstractive Summarization (No prefix needed)](https://huggingface.co/VietAI/vit5-base-vietnews-summarization). I used 2 technologies of optimum with onnx runtime of huggingface to reduce size and improve speed for inferencing. The first is optimization  rebuilds the computation graph and the second is floating-point quantization.In this [notebook](app/bot/model/onnx.ipynb) is a guide on how to make a more productive inferenceable model using the optimum library.

## Features
There are two increments in this simple application, summarize and contribute

1. Summarization

The summarization feature in web app allows you to quickly and easily summarize any text, article, or document. Simply enter the text you want to summarize into the text box and click the "Submit" button. The app will then generate a summary of the text in one second.

![Image demo summarize](docs/images/summarize.jpg)

2. Contribute

The contribute feature in web app allows you to help us collect more quality data for our next training. Simply enter the long text and summary of the text into the text boxes and click the "Contribute" button. The app will then store the data in our database and we will be able to use it to improve our text summarization model.

![Image demo contribute](docs/images/contribute.png)

I created a database management tool called pgAdmin4. This tool allows us to manage all of the data that our clients contribute. I have included the default account credentials for logging into pgAdmin4 in the `.env.dev` file. We have a simple query like this:

![Contributed data](docs/images/database.png)


## Installation
Here are instructions for installing, using and developing more features:
### Development
#### 1. Clone project
```
git clone https://github.com/NgToanRob/django-text-summarization.git
```

Download ONNX model in the [link](https://drive.google.com/file/d/1nCHJJ8ZilX7KNno0r1gIOkXu5U9u9foW/view?usp=sharing)

Extract `onnx.zip` to `app/bot/` directory.

#### 2. Build docker compose and up them in background mode
This process takes a long time to build the images from scratch.
```
docker compose up -d -build
```
#### 3. Makemigrations and migrate on first app launch
This process interferes with running containers, it is quite heavy so it takes a few seconds to work
```
docker compose exec summarizerbot python manage.py makemigrations
docker compose exec summarizerbot python manage.py migrate --noinput
```




#### 5. Let's experience it with the features
- Launch GUI with url [http://localhost:5000](http://localhost:5000)
- Should use docker desktop to see log of containers
![Image ogs](docs/images/logs.png)
- Login pgadmin4 to mamage database with url [http://localhost:8080](http://localhost:8080)
![Image login](docs/images/login-pgadmin.png)

The default account is available in the file `.env.dev` with the names `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`

### Production
I will do when I have money in my account to rent the cloud :))


## Common problems
Exits running app in port 5432
```
sudo lsof -i -P -n | grep 5432
sudo kill <process id>
```









