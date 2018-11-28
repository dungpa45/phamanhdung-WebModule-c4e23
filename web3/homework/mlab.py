import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds251747.mlab.com:51747/movies

host = "ds251747.mlab.com"
port = 51747
db_name = "movies"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
