import mongoengine

# mongodb: // <dbuser > : < dbpassword > @ds241530.mlab.com: 41530/c4e23-blog

host = "ds241530.mlab.com"
port = 41530
db_name = "c4e23-blog"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port,
                        username=user_name, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
