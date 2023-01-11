import os
import time
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from random import choices

import celery_maker

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='pyamqp://guest:guest@localhost//',
    CELERY_RESULT_BACKEND='redis://localhost:6379',
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/pjp.db'
)
app.secret_key = os.urandom(42)

celery = celery_maker.make_celery(app)
db = SQLAlchemy(app)


class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))


@celery.task(name='app.insert')
def insert():
    t = time.time()
    for step in range(500):
        time.sleep(0.025)
        data = ''.join(choices('ABCDE', k=25))
        result = Results(data=data)

        db.session.add(result)

    db.session.commit()    

    return 'insert finished in {}'.format(time.time()-t)

@app.route('/')
def home():

    data = Results.query.order_by(Results.id.desc()).limit(5).all()

    return render_template('index.html', records=data)    

@app.route('/task')
def task():
    insert.delay()
    flash(u'Celery Task úspěšně odstartoval')
    return redirect(url_for('home'))


@app.route('/task_sync')
def task_slow():
    res = insert()
    flash(res)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)    