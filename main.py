from modules.pages import fortnitegame
from modules.account import datarouterresponse, token, externalauths, account, enabled_features, cloudstorage, query_profile, receipts, friends, block, verify, setmtx, AthenaQueryProfile, AthenaQueryLogin, MarkNewQuestNot
from modules.media import apfellogo256x256, lunarlogosmall256x256, seasonxbg, blackhole, blackhole_small
from modules.rest import calendar, versioncheck, statuscheck
from modules.store import catalog
from modules.cloudstorage import system, defaultengine, defaultgame, defaultruntime
from flask import Flask, make_response
from flask_cors import CORS

fn_port = 8383

app = Flask(__name__)
CORS(app)

@app.route("/content/api/pages/fortnite-game", methods=["GET"])
def fortnitegameresponse():
    return fortnitegame()

@app.route("/datarouter/api/v1/public/data", methods=["POST"])
def datarouter():
    return datarouterresponse()

@app.route("/images/lunar-small.png", methods=["GET"])
def lunar_image_small():
    return lunarlogosmall256x256()

@app.route("/images/apfel-small.png", methods=["GET"])
def apfel_image_small():
    return apfellogo256x256()

@app.route("/images/lunar.png", methods=["GET"])
def lunar_image():
    return lunarlogosmall256x256()

@app.route("/images/lunar_big.png", methods=["GET"])
def seasonxbgresponse():
    return seasonxbg()

@app.route("/images/blackhole.png", methods=["GET"])
def blackholemotd():
    return blackhole()

@app.route("/images/blackhole-s.png", methods=["GET"])
def blackholemotds():
    return blackhole_small()

@app.route("/images/apfel_logo.png", methods=["GET"])
def apfel_logor():
    return apfellogo256x256()

@app.route("/account/api/oauth/token", methods=["POST"])
def respondtoken():
    return token()

@app.route("/fortnite/api/calendar/v1/timeline", methods=["GET"])
def respondcalendar():
    return calendar()

@app.route("/fortnite/api/v2/versioncheck/Windows", methods=["GET"])
def respondversion():
    return versioncheck()

@app.route("/fortnite/api/cloudstorage/system", methods=["GET"])
def respondsystem():
    return system()

@app.route("/fortnite/api/cloudstorage/system/DefaultEngine.ini", methods=["GET"])
def responddefaultengine():
    return defaultengine()

@app.route("/fortnite/api/cloudstorage/system/DefaultGame.ini", methods=["GET"])
def responddefaultgame():
    return defaultgame()

@app.route("/fortnite/api/cloudstorage/system/DefaultRuntimeOptions.ini", methods=["GET"])
def responddefaultruntime():
    return defaultruntime()

@app.route("/waitingroom/api/waitingroom", methods=["GET"])
def waitingroom():
    response = make_response("1337", 204)
    return response

@app.route("/account/api/public/account/r54hre45h4r5th48r5hrhr54h56rhr/externalAuths", methods=["GET"])
def repondexternalauths():
    return externalauths()

@app.route("/account/api/oauth/sessions/kill", methods=["DELETE"])
def killsession():
    response = make_response({}, 204)
    return response

@app.route("/account/api/public/account/r54hre45h4r5th48r5hrhr54h56rhr", methods=["GET"])
def respondaccount():
    return account()

@app.route("/account/api/oauth/sessions/kill/eg1~h1e35h4tr5h456r4h75r4h8r4h5r45h4r5", methods=["DELETE"])
def killsessiontwo():
    response = make_response({}, 204)
    return response

@app.route("/fortnite/api/game/v2/tryPlayOnPlatform/account/r54hre45h4r5th48r5hrhr54h56rhr", methods=["POST"])
def platformcheck():
    response = make_response("true", 200)
    return response

@app.route("/lightswitch/api/service/bulk/status", methods=["GET"])
def respondstatus():
    return statuscheck()

@app.route("/fortnite/api/game/v2/enabled_features", methods=["GET"])
def respondfeatures():
    return enabled_features()

@app.route("/fortnite/api/game/v2/grant_access/r54hre45h4r5th48r5hrhr54h56rhr", methods=["POST"])
def respondaccess():
    response = make_response("true", 200)
    return response

@app.route("/fortnite/api/cloudstorage/user/r54hre45h4r5th48r5hrhr54h56rhr", methods=["GET"])
def respondcloudstorage():
    return cloudstorage()

@app.route("/fortnite/api/game/v2/profile/r54hre45h4r5th48r5hrhr54h56rhr/client/QueryProfile", methods=['POST'])
def QueryProfile():
    return query_profile()

@app.route("/fortnite/api/receipts/v1/account/r54hre45h4r5th48r5hrhr54h56rhr/receipts", methods=["GET"])
def respondReceipts():
    return receipts()

@app.route("/fortnite/api/storefront/v2/catalog", methods=["GET"])
def catalogresponse():
    return catalog()

@app.route("/friends/api/public/friends/r54hre45h4r5th48r5hrhr54h56rhr", methods=["GET"])
def friendresponse():
    return friends()

@app.route("/friends/api/public/blocklist/r54hre45h4r5th48r5hrhr54h56rhr", methods=["GET"])
def blockresponse():
    return block()

@app.route("/account/api/oauth/verify", methods=["GET"])
def verifyresponse():
    return verify()

@app.route("/fortnite/api/game/v2/profile/r54hre45h4r5th48r5hrhr54h56rhr/client/SetMtxPlatform", methods=["POST"])
def setmtxplatform():
    return setmtx()

@app.route("/fortnite/api/game/v2/profile/r54hre45h4r5th48r5hrhr54h56rhr/client/QueryProfile", methods=["POST"])
def downloadqueryathena():
    return AthenaQueryProfile()

@app.route("/fortnite/api/game/v2/profile/r54hre45h4r5th48r5hrhr54h56rhr/client/ClientQuestLogin", methods=["POST"])
def downloadqueryloginathena():
    return AthenaQueryLogin()

@app.route("/fortnite/api/game/v2/profile/r54hre45h4r5th48r5hrhr54h56rhr/client/MarkNewQuestNotificationSent", methods=["POST"])
def markNewQuest():
    return MarkNewQuestNot()

@app.route("/fortnite/api/matchmaking/session/findPlayer/r54hre45h4r5th48r5hrhr54h56rhr", methods=["GET"])
def idkman():
    response = make_response("", 204)
    return response

def run_flask():
    print(f'Pynite Running on Port {fn_port}')
    app.run(host='0.0.0.0', port=fn_port)

run_flask()