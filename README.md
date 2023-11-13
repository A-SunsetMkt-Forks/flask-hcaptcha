# Flask-hCaptcha
[![Latest version released on PyPi](https://img.shields.io/pypi/v/Flask-hCaptcha.svg?style=flat&label=latest%20version)](https://pypi.org/project/Flask-hCaptcha/)
[![Python package](https://github.com/KnugiHK/flask-hcaptcha/workflows/Python%20package/badge.svg)](https://github.com/KnugiHK/flask-hcaptcha/actions)

A hCaptcha extension for Flask based on flask-recaptcha.

**Flask-hCaptcha 0.6.0 will be the last version that support Python 2, 3.5 and 3.6.**

---

## Install

    pip install flask-hcaptcha

# Usage

### Implementation view.py

    from flask import Flask
    from flask_hcaptcha import hCaptcha

    app = Flask(__name__)
    hcaptcha = hCaptcha(app)
    
    #or 
    
    hcaptcha = hCaptcha()
    hcaptcha.init_app(app)
    

### In your template: **{{ hcaptcha }}**

Inside of the form you want to protect, include the tag: **{{ hcaptcha }}**

It will insert the code automatically


    <form method="post" action="/submit">
        ... your field
        ... your field

        {{ hcaptcha }}

        [submit button]
    </form>


### Verify the captcha

In the view that's going to validate the captcha

    from flask import Flask
    from flask_hcaptcha import hCaptcha

    app = Flask(__name__)
    hcaptcha = hCaptcha(app)

    @route("/submit", methods=["POST"])
    def submit():

        if hcaptcha.verify():
            # SUCCESS
            pass
        else:
            # FAILED
            pass


## API

**hCaptcha.__init__(app, site_key, secret_key, is_enabled=True)**

**hCaptcha.get_code(dark_theme=False)**

Returns the HTML code to implement. But you can use
**{{ hcaptcha }}** directly in your template. A [dark
theme](https://docs.hcaptcha.com/configuration#themes)
can also be specified with `dark_theme=True`.

**hCaptcha.verify()**

Returns bool

## In Template

Just include **{{ hcaptcha }}** wherever you want to show the hcaptcha


## Config

Flask-hCaptcha is configured through the standard Flask config API.
These are the available options:

**HCAPTCHA_ENABLED**: Bool - True by default, when False it will bypass validation

**HCAPTCHA_SITE_KEY** : Public key

**HCAPTCHA_SECRET_KEY**: Private key

    HCAPTCHA_ENABLED = True
    HCAPTCHA_SITE_KEY = ""
    HCAPTCHA_SECRET_KEY = ""

## Todo
1. Support [Invisible Captcha](https://docs.hcaptcha.com/invisible)
2. Support the use of [Language Codes](https://docs.hcaptcha.com/languages)

---

© 2021 Knugi 
© 2015 Mardix 

