# Deploy to Heroku

1. Create an account on https://www.heroku.com
1. [Install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
   ```sh
   brew tap heroku/brew
   brew install heroku
   ```
1. Copy this folder to somewhere outside the `python-curriculum` repository
1. Navigate to that folder, create a local Git repository, and connect it to Heroku
   ```sh
   cd <new folder location>
   git init
   heroku create
   ```
1. Commit and push the code to Heroku
   ```sh
   git add .
   git commit -m 'Initial commit'
   git push heroku main
   ```
1. Start the application
   ```sh
   heroku ps:scale worker=1
   ```

## Stop the application

```sh
heroku ps:stop worker
```
