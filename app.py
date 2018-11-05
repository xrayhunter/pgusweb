from flask import Flask, render_template, request, session, send_from_directory
from flask_session import Session
from flask_wtf import CSRFProtect
from flaskext.markdown import Extension, Markdown
from datetime import datetime
from membership import MembershipForm
import json

# Flask Initialization
app = Flask(__name__, static_folder='./media')
# Flask-App Configuration
app.config.from_object(__name__)
app.secret_key = 'S21AD#$1aSFa!@#$sAGAG221tAg'
app.config["SESSION_TYPE"] = 'filesystem'

# Server-Side Session Handler
sess = Session(app)

# Markdown Handler
md = Markdown(app)

# Cross-Site Request Forgery Handler
csrf = CSRFProtect(app)

# SQL Handler
sql = SQLAlchemy(app)
@app.route("/")
def index():
    if session.get("user") is None:
        session['user'] = []

    return render_template("index.html", user=session['user'], news=[{"title":"", "summary":""}])
    
@app.route("/news")
def news():
    if session.get("user") is None:
        session['user'] = []
    return render_template("news.html", user=session['user'])
    
@app.route("/membership/", methods=["POST", "GET"])
def membership():
    completed_registration = False
    if request.method == "POST":
        fullname = request.form.get('fullname')
        country = request.form.get('country')
        states = request.form.get('states')
        email = request.form.get('email')
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3')
        q4 = request.form.get('q4')
        q5 = request.form.get('q5')
        q6 = request.form.get('q6')
        json_questions = json.dumps([q1, q2, q3, q4, q5, q6])
        # Insert Membership
        completed_registration = True

    if session.get("user") is None:
        session['user'] = []
    if session.get("membership") is None:
        session['membership'] = None
        #sql.get('membership', ('email = ' + session['user'].email))
    return render_template("membership/index.html", user=session['user'], member=session['membership'], form=MembershipForm(), registration_complete=completed_registration)

@app.route("/associatedprojects")
def associatedProjects():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/associatedprojects.html", user=session['user'])
    
@app.route("/becomeamember/")
def becomeAMember():
    if session.get("user") is None:
        session['user'] = []
    if session.get("membership") is None:
        session['membership'] = []
    return render_template("pages/becomeamember.html", user=session['user'], member=membership)

@app.route("/conferences")
def conferences():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/conferences.html", user=session['user'])

@app.route("/contactus")
def contactus():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/contactus.html", user=session['user'])

@app.route("/corporate")
def corporate():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/corporate.html", user=session['user'])

@app.route("/diversity")
def diversity():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/diversity.html", user=session['user'])

@app.route("/donate")
def donate():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/donate.html", user=session['user'])

@app.route("/events")
def events():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/events.html", user=session['user'])

@app.route("/financialsupport")
def financialsupport():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/financialsupport.html", user=session['user'])

@app.route("/policies")
def policies():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/policies.html", user=session['user'])

@app.route("/singleevent")
def singleevent():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/singleevent.html", user=session['user'])

@app.route("/team/")
def team():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/team.html", user=session['user'])

@app.route("/aboutus")
def aboutus():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pages/aboutus.html", user=session['user'])
    
@app.route("/team/info")
def team_info():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pieces/team_info.html", user=session['user'])

@app.route("/team/event_description")
def team_event_description():
    if session.get("user") is None:
        session['user'] = []
    return render_template("pieces/event_description.html", user=session['user'])

@app.route("/<path:filename>")
def send_static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.errorhandler(404)
def error_404(e):
    if session.get("user") is None:
        session['user'] = []
    return render_template("errs/404.html", user=session['user'], page=request.path)

@app.template_filter('timeuntil')
def timeuntil(s):
    return s


@app.template_filter('date')
def date(dateformat):
    return datetime.strftime(dateformat)