# :lock: :key: Encryptor

Several encryptors (cryptographic secure or not) available in a REST API
fashion, using Flask

## :computer: Running

- To configure Sentry, you need to create an account at sentry.io and generate a
  key. You can set it as an environment variable with the name `SENTRY_DSN` or
  create a `.env` and create an entry `SENTRY_DSN=<your SENTRY_DSN here>`

- To install the required libraries you should run
  `pip install -r requirements.txt && pip install -e .`

- To run the application, you just need to run the following command, and access
  the API at port 5000 of your local host: `FLASK_APP=encryptor flask run`

## :vertical_traffic_light: Trying out

You can try out each encryptor in their respective route based in the following
model:
`localhost:5000/api/:encryptor/{encrypt|decrypt}/:text?option_1=x&option_2=y`,
where you can see the required options in each route at the source file. Example
to encrypt the text github with an offset of 4, using a `Ceasar` cypher:
`localhost:5000/api/ceasar/encrypt/github?offset=4`.

## :white_check_mark: Tests

You can test this application running the `pytest` command


## Encryptor Logo 
![Encryptor Logo](/assets/logo.png)
![Encryptor Logo Grey](/assets/logo_grey.png)
![Encryptor Logo BW](/assets/logo_bw.png)



## :muscle: Contributing

You may check [CONTRIBUTING.md](./CONTRIBUTING.md) if you want to contribute to
the project! I would highly reccommend you to do so, as we are trying to build
something really nice and beginner friendly.

## :busts_in_silhouette: Contributors

- [RafaAudibert](https://github.com/rafaeelaudibert) - Author
