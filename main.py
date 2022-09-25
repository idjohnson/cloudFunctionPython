import os
import apprise

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    apobj = apprise.Apprise()
    apobj.add('sendgrid://SENDGRIDTOKENHERE:isaac@freshbrewed.science/isaac.johnson@gmail.com')
    apobj.add('msteams://MSTEAMSTOKENHERE')
    apobj.notify(
        body='Notified by Cloud Run Function',
        title='From Python Cloud Run',
    )
    return "Hello hello {}!".format(name)

@app.route("/teams")
def hello_world2():
    name = os.environ.get("NAME", "World")
    apobj = apprise.Apprise()
    apobj.add('sendgrid://SENDGRIDTOKENHERE:isaac@freshbrewed.science/isaac.johnson@gmail.com')
    apobj.notify(
        body='Notified by Cloud Run Function',
        title='From Python Cloud Run',
    )
    return "Hello hello {}!".format(name)

@app.route("/email")
def hello_world3():
    name = os.environ.get("NAME", "World")
    apobj = apprise.Apprise()
    apobj.add('sendgrid://SENDGRIDTOKENHERE:isaac@freshbrewed.science/isaac.johnson@gmail.com')
    apobj.notify(
        body='Notified by Cloud Run Function',
        title='From Python Cloud Run',
    )
    return "Hello hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
