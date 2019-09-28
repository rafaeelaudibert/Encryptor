# Encryptor

Little toy project to showcase Python, Flask, Sentry and Travis CI for INF01127 Software Engineering Course at [INF](https://inf.ufrgs.br)-[UFRGS](https://ufrgs.br)

## Running

* To configure Sentry, you need to create an account at sentry.io and generate a key. You can set it as an environment variable with the name `SENTRY_DSN` or create a `.env` and create an entry `SENTRY_DSN=<your SENTRY_DSN here>`

* To install the required libraries you should run `pip install -r requirements.txt && pip install -e .`

* To run the application, you just need to run the following command, and access the API at port 5000 of your local host: `FLASK_APP=encryptor flask run`

## Trying out

You can try out each encryptor in their respective route based in the following model: `localhost:5000/api/:encryptor/{encrypt|decrypt}/:text/...other_options`, where you can see the required options in each route at the source file. Example to encrypt the text github with an offset of 4, using a Ceasar cypher: `localhost:5000/api/ceasar/encrypt/github/4`.

There is an open route which triggers an error which can be received by sentry at `localhost:5000/api/error`
