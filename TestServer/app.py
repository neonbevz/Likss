from flask import Flask, jsonify

app = Flask(__name__)

TEST_DCT = {
        'result': [
            {"name": "Петроцилін",
             "url": "facebook.com",
             "composition": "2,3,4,5,6 Петрична сіль 100мл",
             "county": "Ukraine",
             "release_type": "Апмули"
             },
            {"name": "Петродиклак",
             "url": "twitter.com",
             "composition": "Петропетричний розчин 146%",
             "county": "Ukraine",
             "release_type": "Краплі"
             },
            {"name": "Петро Гель",
             "url": "google.com",
             "composition": "Петроксид Петра",
             "county": "Ukraine",
             "release_type": "Гель"
             }
        ]
    }


@app.route('/search_name_test', methods=['POST'])
def search_name():
    dct = TEST_DCT
    return jsonify(dct)


@app.route('/search_contains_test', methods=['POST'])
def search_contains():
    dct = TEST_DCT
    return jsonify(dct)


if __name__ == '__main__':
    app.run()
