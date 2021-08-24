import requests
from selenium.webdriver.chrome import webdriver


class Oauth(object):
    client_id = "879827948583137280"
    client_secret = "uMNg2SXUnCUzwbLn8nnIY0EDQnSUmEdp"
    scope = "identify%20guilds"
    redirect_uri = "https://clarity.dexcom.com"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id={}&redirect_uri={}&response_type=code&scope={}".format(client_id,redirect_uri,scope)
    discord_tken_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discordapp.com/api"

    @staticmethod
    def get_access_token(code):
        payload = {
            'client_id':Oauth.client_id,
            'client_secret':Oauth.client_secret,
            'grant_type':"authorization_code",
            'code':code,
            'redirect_uri':Oauth.redirect_uri,
            'scope':Oauth.scope
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = requests.post(url = Oauth.discord_tken_url,data=payload,headers=headers)
        json = access_token.json()
        return json.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = Oauth.discord_api_url+"/users/@me"

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        user_object = requests.get(url =url,headers = headers)
        user_json = user_object.json()
        return user_json





