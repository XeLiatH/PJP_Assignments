import flask
from functools import wraps


def check_auth(form):
    uname = 'admin'
    passwd = 'admin'

    return form['uname'] == uname and form['passwd'] == passwd


def required(endpoint):
    """
    auth reqired decorator with parameter 
    @param string app endpoint for redirect
    """
        
    def required_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                status = flask.session['authorized']
            except KeyError:
                return flask.redirect(flask.url_for(endpoint))

            if status:
                return func(*args, **kwargs)

            return flask.redirect(flask.url_for(endpoint))

        return wrapper

    return required_decorator    