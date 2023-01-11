import os
from flask import Flask, render_template, url_for, redirect, flash
import celery_maker


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='pyamqp://guest:guest@localhost//',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

app.secret_key = os.urandom(42)

celery = celery_maker.make_celery(app)

@celery.task(name='app.add_together')
def add_together(a, b):
    return a + b


@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/task')
def task():
    add_together.delay(10, 20)
    flash(u'Task úspěšně odstartoval')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)    