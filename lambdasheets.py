from flask import Flask
import pandas as pd
import pygsheets
import config

app = Flask(__name__)

@app.route("/")
def process():
    gc = pygsheets.authorize(service_file=config.auth_file)
    sh = gc.open(config.spreadsheet_name)

    # Read data from first sheet
    data = sh[0].get_as_df()

    # do some processing
    data['length'] = data.end - data.start

    # write back the result
    results = [[d] for d in data['length'].tolist()]
    sh[0].range('C2:C' + str(len(data) + 1), returnas='range')\
        .update_values(results)
    return "OK"

if __name__ == "__main__":
    app.run()
