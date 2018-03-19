# Lambdasheets

Process google sheets with Pandas on AWS lambda

##Installaion

### Prerequisite

Install [pipenv](https://github.com/pypa/pipenv)


### Python environment and dependencies

Clone the repository, then from the repository directory:


```sh
pipenv install --dev
pipenv shell
```

### Configuration


Configure zappa with:
```sh
zappa init
```

Choose `lambdasheets.app` for the application.

Create a project in your google developer console.
Add access to 'Google Drive' and 'Google sheets' APIs.
Create a service account: note the service account email.
Download the account key and copy it in the project directory.

Note: You may choose to use OAuth2 instead
Read more on [pygsheet's docs here](https://pygsheets.readthedocs.io/en/latest/authorizing.html).

Create the config file:

```sh
cp config_template.py config.py
```

Edit the `config.py` file and set the the service file name.

### Spreadhseet

Create a new spreadsheet with first columns named `start` and `end`. Share it with the service account email.
Set the spreadsheet name in the `config.py` file.

You can use [this spreadsheet as a template.](https://docs.google.com/spreadsheets/d/1sW8ad82BCprVc89bVE5BA247I5v5X29fXG1n5CclprI/edit?usp=sharing)

You can test that the service account has access to the spreadsheet by launching the flask server locally:

```sh
python lambdasheets.py
```

Head to `http://127.0.0.1:5000/` in your browser. You should see `OK`.

### Deploy function

```sh
zappa deploy
```
Note the deployment url returned by zappa.

### Triggering updates from the Google sheets UI.

We are going to add a menu item to trigger a run of our lambda function.

In `Tools > Script Editor`

Copy the code from script.gs, replace `[deployed_url]` by the one given by zapp, save and reload.
You should see a new `Lambda Sheets` menu that you can use to trigger updates.

You will be asked an authorization when running for the first time.

## Your function

Edit `lambdasheets.py` to do the processing you want.

Check [pygsheets](https://github.com/nithinmurali/pygsheets) for more details on how to interact with the spreadsheet from python.

To redeploy:

```sh
zappa update
```

## Trigger modes

* on menu click: this the one we covered
* Spreadsheet driven: in the google script editor, choose `Edit -> Current project's trigger` and choose the auto execution mode you want
* AWS driven: configure triggers from your AWS console using CLoudFront, S3 ...
