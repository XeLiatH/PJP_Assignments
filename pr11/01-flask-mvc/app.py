# -*- coding: utf-8 -*-
import flask
from modules import auth


app = flask.Flask(__name__)
app.secret_key = 'prisnetajnyretezec'


@app.route('/')
@app.route('/pokus/')
def home():
    return flask.render_template('index.html')


@app.route('/login/')
def login():
    return flask.render_template('login.html')


@app.route('/login/', methods=('POST',))
def login_handler():
    stav = auth.check_auth(flask.request.form)
    if stav:
        flask.flash(u'úspešné přihlášení...')
        flask.session['authorized'] = True
        return flask.redirect(flask.url_for('admin'))
    else:
        error_msg = u'špatné uživatelské jméno nebo heslo'
        return flask.render_template('login.html', error=error_msg)

@app.route('/logout/')
def logout():

    flask.flash(u'úspešné odhlášení...')
    flask.session['authorized'] = False
    return flask.render_template('index.html')        


@app.route('/admin/')
@auth.required('home')
def admin():
    return flask.render_template('admin.html')



@app.errorhandler(404)
def not_found(error):
    return flask.render_template('error_404.html')




if __name__ == '__main__':
    app.run(debug=True)       
