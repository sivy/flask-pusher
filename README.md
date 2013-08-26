flask-pusher
============

Pusher extension for the Flask microframework.

Built on top of <https://pypi.python.org/pypi/pusher/>

Installation
-----------

```shell
pip install flask-pusher
```

Configuration
-------------

In your flask configuration file/object:

```python
PUSHERAPP_ID = '<your app id>'
PUSHERAPP_KEY = '<your pusher key>'
PUSHERAPP_SECRET = '<your pusher secret>'
```

```python
from flask import Flask
from flask_pusher import Pusher

app = Flask(__name__)
pusher = Pusher(app)
```

or in `extensions.py`

```python
from flask_pusher import Pusher

pusher = Pusher()
```

```python
from flask import Flask
from extensions import pusher

def create_app():
	app = Flask(__name__)
	pusher.init_app(app)
	return app
```

Usage
-----


```python
from extensions import pusher

pusher[channel_name].trigger('event', {
	'message': msg,
})
```

Documentation for communicating with the Pusher service with the python client are on the Pusher website:

<http://pusher.com/docs/server_api_guide#/lang=python>
