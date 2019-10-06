# Contributing

Hey guys! Feel free to contribute to this project, as the principal intent of it
is to be a good place to start you jorney through Open Source Software.

It is important to note, though, that some good standards should be followed to
the well-being of the project.

- You can contribute with anything, from a new feature (new encryptor) to
  documentation.
- If you are creating a new encryptor, make sure to create it following the
  pattern (as explained below). You will need to create the encryptor, as well
  as the routes for the API. The are always in the format
  `/api/{encryptor_name}/{encrypt/decrypt}`.
- Make sure all the tests always pass before creating the PR, as Travis CI will
  check it.
- We use [Gitmoji](https://gitmoji.carloscuesta.me/) in our commit messages,
  so make sure to follow their convention.

## Encryptor Pattern

When creating a new encryptor, try follow this rules:

- Create it in the encryptors folder, with a new class which should have 2
  static methods `encrypt` and `decrypt`.
- You may create some other helper methods, which should be private, this is,
  they should start with an underline, following Python convention.
- You should expose both methods in routes in the
  [routes file](./encryptor/__init__.py)
