0x04. AirBnB clone - Web framework
----------------------------------

**0. Hello Flask!** `[0-hello_route.py, __init__.py]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- has route:
	- `/` which displays "Hello HBNB",
- and `strict_slashes=False` option used in the route definition.

**1. HBNB** `[1-hbnb_route.py]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- has routes:
	- `/` which displays "Hello HBNB",
	- and `/hbnb` which displays "HBNB",
- and `strict_slashes=False` option used in the route definition.

**2. C is fun!** `[2-c_route.py]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- has routes:
	- `/` which displays "Hello HBNB",
	- `/hbnb` which displays "HBNB",
	- and `/c/<text>` which displays "C" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character),
- and `strict_slashes=False` option used in the route definition.

**3. Python is cool!** `[3-python_route.py]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- has routes:
	- `/` which displays "Hello HBNB",
	- `/hbnb` which displays "HBNB",
	- `/c/<text>` which displays "C" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character),
	- and `/python/<text>` which displays "Python" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character, and the default value for `text` is "is cool"),
- and `strict_slashes=False` option used in the route definition.

**4. Is it a number?** `[4-number_route.py]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- has routes:
	- `/` which displays "Hello HBNB",
	- `/hbnb` which displays "HBNB",
	- `/c/<text>` which displays "C" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character),
	- `/python/<text>` which displays "Python" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character, and the default value for `text` is "is cool"),
	- and `/number/<n>` which displays "`n` is a number" (only if `n` is an integer),
- and `strict_slashes=False` option used in the route definition.

**5. Number template** `[5-number_template.py, templates/5-number.html]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- has routes:
	- `/` which displays "Hello HBNB",
	- `/hbnb` which displays "HBNB",
	- `/c/<text>` which displays "C" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character),
	- `/python/<text>` which displays "Python" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character, and the default value for `text` is "is cool"),
	- `/number/<n>` which displays "`n` is a number" (only if `n` is an integer),
	- and `/number_template/<n>` which displays a HTML page (only if `n` is an integer, and `H1` tag and "Number: `n`" are inside the tag `BODY`),
- and `strict_slashes=False` option used in the route definition.

**6. Odd or even?** `[6-number_odd_or_even.py, templates/6-number_odd_or_even.html]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- has routes:
	- `/` which displays "Hello HBNB",
	- `/hbnb` which displays "HBNB",
	- `/c/<text>` which displays "C" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character),
	- `/python/<text>` which displays "Python" followed by the value of the `text` variable (underscore `_` symbols replaced with a space ` ` character, and the default value for `text` is "is cool"),
	- `/number/<n>` which displays "`n` is a number" (only if `n` is an integer),
	- `/number_template/<n>` which displays a HTML page (only if `n` is an integer, and `H1` tag and "Number: `n`" are inside the tag `BODY`),
	- and `/number_odd_or_even/<n>` which displays a HTML page (only if `n` is an integer, and `H1` tag and "Number: `n` is `even|odd`" are inside the tag `BODY`),
- and `strict_slashes=False` option used in the route definition.

**7. Improve engines** `[models/engine/file_storage.py, models/engine/db_storage.py, models/state.py]` >> Updating parts of the engine, namely:
- `FileStorage` (`models/engine/file_storage.py`), where a public method `def close(self):` is added to call `reload()` method for deserializing the JSON file to objects,
- `DBStorage` (`models/engine/db_storage.py`), where a public method `def close(self):` is added to call `remove()` method on the private session attribute (`self.__session`) or `close()` on the class `Session`,
- and `State` (`models/state.py`) if it is not already present, where if the storage engine is not `DBStorage`, a public getter method `cities` is added to return the list of `City` objects from `storage` linked to the current `State`.

**8. List of states** `[web_flask/7-states_list.py, web_flask/templates/7-states_list.html]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- uses `storage` to fetch data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`,
- removes the current SQLAlchemy session after each request, declares a method to handle `@app.teardown_appcontext`, and calls in `storage.close()` method.
- has routes:
	- `/states_list` which displays a HTML page (inside the tag `BODY`):
		- where "States" is in a `H1` tag,
		- a list of all `State` objects present in `DBStorage` sorted by `name` [A - Z] are in an `UL` tag,
			-  and a description of each one `State`: `<state.id>: <B><state.name></B>` in `LI` tag,
- imports [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data,
- and `strict_slashes=False` option used in the route definition.

**9. Cities by states** `[web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- uses `storage` to fetch data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`,
- loads all cities of a `State`, where it uses `cities` relationship if the storage engine is `DBStorage`, otherwise it uses public getter method `cities`.
- removes the current SQLAlchemy session after each request, declares a method to handle `@app.teardown_appcontext`, and calls in `storage.close()` method.
- has routes:
	- `/cities_by_states` which displays a HTML page (inside the tag `BODY`):
		- where "States" is in a `H1` tag,
		- a list of all `State` objects present in `DBStorage` sorted by `name` [A - Z] are in an `UL` tag,
			- a description of each one `State`: `<state.id>: <B><state.name></B>` in `LI` tag plus a list of `City` objects linked to the `State` sorted by `name` [A - Z] are in an `UL` tag,
				- and a description of each one `City`: `<city.id>: <B><city.name></B>` in `LI` tag,
- imports [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data,
- and `strict_slashes=False` option used in the route definition.

**10. States and State** `[web_flask/9-states.py, web_flask/templates/9-states.html]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- uses `storage` to fetch data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`,
- loads all cities of a `State`, where it uses `cities` relationship if the storage engine is `DBStorage`, otherwise it uses public getter method `cities`.
- removes the current SQLAlchemy session after each request, declares a method to handle `@app.teardown_appcontext`, and calls in `storage.close()` method.
- has routes:
	- `/states` which displays a HTML page (inside the tag `BODY`):
		- where "States" is in a `H1` tag,
		- a list of all `State` objects present in `DBStorage` sorted by `name` [A - Z] are in an `UL` tag,
			- a description of each one `State`: `<state.id>: <B><state.name></B>` in `LI` tag,
	- `/states/<id>` which displays a HTML page (inside the tag `BODY`):
		- and if a `State` object is found with this `id` then:
			- where "States" is in a `H1` tag,
			- where "Cities" is in a `H3` tag,
			- a list of `City` objects linked to the `State` sorted by `name` [A - Z] are in an `UL` tag,
				- and a description of each one `City`: `<city.id>: <B><city.name></B>` in `LI` tag,
		- otherwise `H1` is "Not found",
- imports [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data,
- and `strict_slashes=False` option used in the route definition.

**11. HBNB filters** `[web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- uses `storage` to fetch data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`,
- loads all cities of a `State`, where it uses `cities` relationship if the storage engine is `DBStorage`, otherwise it uses public getter method `cities`.
- removes the current SQLAlchemy session after each request, declares a method to handle `@app.teardown_appcontext`, and calls in `storage.close()` method.
- has route:
	- `/hbnb_filters` which displays a HTML page like `6-index.html` from the project [0x01. AirBnB clone - Web static](https://github.com/LeRoy-M/AirBnB_clone). Here:
		- files `3-footer.css`, `3-header.css`, `4-common.css` and `6-filters.css` are copied from `web_static/styles/` to the folder `web_flask/static/styles`,
		- files `icon.png` and `logo.png` are copied from `web_static/images/` to the folder `web_flask/static/images`,
		- there is an update to `.popover` class in `6-filters.css` to allow scrolling in the popover and a max height of 300 pixels,
		- content from `6-index.html` is used as source code for the template `10-hbnb_filters.html`, replacing the content of `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`,
		- `State`, `City` and `Amenity` objects are loaded from `DBStorage` and are sorted by `name` [A - Z],
- imports [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql) to have some data,
- and `strict_slashes=False` option used in the route definition.

**12. HBNB is alive** `[web_flask/100-hbnb.py, web_flask/templates/100-hbnb.html, web_flask/static/]` >> Python script that starts a Flask web application that:
- listens on `0.0.0.0`, on port `5000`,
- uses `storage` to fetch data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`,
- loads all cities of a `State`, where it uses `cities` relationship if the storage engine is `DBStorage`, otherwise it uses public getter method `cities`.
- removes the current SQLAlchemy session after each request, declares a method to handle `@app.teardown_appcontext`, and calls in `storage.close()` method.
- has route:
	- `/hbnb` which displays a HTML page like `8-index.html` from the project [0x01. AirBnB clone - Web static](https://github.com/LeRoy-M/AirBnB_clone). Here:
		- files `3-footer.css`, `3-header.css`, `4-common.css`, `6-filters.css` and `8-places.css` are copied from `web_static/styles/` to the folder `web_flask/static/styles`,
		- all files from `web_static/images/` are copied to the folder `web_flask/static/images`,
		- there is an update to `.popover` class in `6-filters.css` to enable scrolling in the popover and set a max height of 300 pixels,
		- an update in `8-places.css` to always have the price by night on the top right of each place element and the name correctly aligned and visible,
		- content from `8-index.html` is used as source code for the template `100-hbnb.html`, replacing the content of `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`,
		- `State`, `City` and `Amenity` objects are loaded from `DBStorage` and are sorted by `name` [A - Z],
- imports [100-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql) to have some data,
- and `strict_slashes=False` option used in the route definition.
