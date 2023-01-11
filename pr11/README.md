## Flask 

Flask je potřeba nainstalovat, není součástí standardní instalace. Stejně tak celery a další moduly. 
Potřebné závislosti jsou v souboru requirements.txt. 

```
pip install -r requirements.txt
```

### SQL Alchemy

Pro závěrečný příklad musíte vytvořit databázi, to SQL Alchemy automaticky neudělá. Stačí k tomu
použít interaktivní režim interpretu. Více v dokumentaci [http://flask-sqlalchemy.pocoo.org/2.3/quickstart/](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/)

```
>>> from app import db
>>> db.create_all()
```

## Celery 

Pro start worker procesu použijte příkaz `celery -A tasks worker --loglevel=info` pro první příklad (02) a `celery -A app.celery worker --loglevel=info` pro příklad 03 a 04. 

