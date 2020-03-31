from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html');


@app.route('/all-courses')
def all_courses():
    return render_template('all-courses.html');


@app.route('/index-2')
def home2():
    return render_template('index-2.html');


@app.route('/about')
def about():
    return render_template('about.html');


@app.route('/admission')
def admission():
    return render_template('admission.html');


@app.route('/courses')
def courses():
    return render_template('all-courses.html');


@app.route('/course-details')
def course_details():
    return render_template('course-details.html');


@app.route('/awards')
def awards():
    return render_template('awards.html');


@app.route('/seminar')
def seminar():
    return render_template('seminar.html');


@app.route('/events')
def events():
    return render_template('events.html');


@app.route('/event-details')
def event_details():
    return render_template('event-details.html');


@app.route('/event-register')
def event_register():
    return render_template('event-register.html');


@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html');


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html');


@app.route('/eee')
def eee():
    return render_template('eee.html');


@app.route('/ice')
def ice():
    return render_template('ice.html');


@app.route('/textile')
def textile():
    return render_template('textile.html');


@app.route('/civil')
def civil():
    return render_template('civil.html');


@app.route('/cse')
def cse():
    return render_template('cse.html');


@app.route('/db-time-line')
def exam():
    return render_template('db-time-line.html');


@app.route('/ed')
def ed():
    return render_template('ed.html')

@app.route('/cps')
def cps():
    return render_template('cps.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/principal')
def principal():
    return render_template('principal.html')


@app.route('/staff')
def info():
    return render_template('staff.html')


@app.route('/governing-body')
def governing_body():
    return render_template('governing-body.html')


@app.route('/academic-committe')
def academic_committe():
    return  render_template('academic-committe.html')


@app.route('/discipline-committee')
def discipline_committee():
    return  render_template('discipline-committee.html')

@app.route('/transport')
def transport():
    return  render_template('transport.html')


@app.route('/library')
def library():
    return  render_template('library.html')


if __name__ == '__main__':
    app.run(debug=True)