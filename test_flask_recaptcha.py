
from flask import Flask
from flask_hcaptcha import hCaptcha

app = Flask(__name__)
app.config.update({
    "debug": True,
    "HCAPTCHA_SITE_KEY": "SITE_KEY",
    "HCAPTCHA_SITE_SECRET": "SECRET",
    "HCAPTCHA_ENABLED": True
})

def test_hcaptcha_enabled():
    hcaptcha = hCaptcha(site_key="SITE_KEY", secret_key="SECRET_KEY")
    assert isinstance(hcaptcha, hCaptcha)
    assert hcaptcha.is_enabled == True
    assert "script" in hcaptcha.get_code()
    assert hcaptcha.verify(response="None", remote_ip="0.0.0.0") == False

def test_hcaptcha_enabled_flask():
    hcaptcha = hCaptcha(app=app)
    assert isinstance(hcaptcha, hCaptcha)
    assert hcaptcha.is_enabled == True
    assert "script" in hcaptcha.get_code()
    assert hcaptcha.verify(response="None", remote_ip="0.0.0.0") == False

def test_hcaptcha_disabled():
    hcaptcha = hCaptcha(site_key="SITE_KEY", secret_key="SECRET_KEY", is_enabled=False)
    assert hcaptcha.is_enabled == False
    assert hcaptcha.get_code() == ""
    assert hcaptcha.verify(response="None", remote_ip="0.0.0.0") == True

def test_hcaptcha_disabled_flask():
    app.config.update({
        "RECAPTCHA_ENABLED": False
    })
    hcaptcha = hCaptcha(app=app)
    assert hcaptcha.is_enabled == False
    assert hcaptcha.get_code() == ""
    assert hcaptcha.verify(response="None", remote_ip="0.0.0.0") == True