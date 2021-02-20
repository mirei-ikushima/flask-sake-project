import requests

sakenote_key = None

sakenote_sakes_base_url = None


def request_essentials(app):
    global sakenote_key, sakenote_sakes_base_url
    sakenote_key = app.config["SECRET_KEY"]
    sakenote_sakes_base_url = app.config["SAKENOTE_SAKES_BASE_URL"]


