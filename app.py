from flask import Flask, jsonify
import xlsx_parser
app = Flask(__name__)
app.json.sort_keys = False

YS001 = xlsx_parser.get_YS001()

index_json = [
    {
        "code": "00",
        "label": {
            "et": "Kinnisvara",
            "en": "Real estate"
        },
        "datasets": [
            {
                "code": YS001["code"],
                "label": YS001["label"],
                "updated": YS001["updated"],
                "status": YS001["status"]
            }
        ]
    },
]

@app.get("/index.json")
def index():
    return index_json

@app.get('/YS001.json')
def get_YS001():  # put application's code here
    return [YS001]


if __name__ == '__main__':
    app.run()
