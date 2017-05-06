# Readme

## Tools
* [yeoman react firebase](https://github.com/prescottprue/generator-react-firebase)
* [emmet.io](https://emmet.io/) - autocomplete for html 
* [emmet cheatsheet](https://docs.emmet.io/cheat-sheet/) - cheatsheet for emmet
* [livereload](https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei/related?hl=en) - live reload changes into browser
* [codepen.io](http://codepen.io/gaearon/pen/ZpvBNJ?editors=0010) - live coding
* [react.io](https://facebook.github.io/react/docs/hello-world.html) - js framework
* [weather api](https://openweathermap.org/current) - weather api
* [gulp](http://gulpjs.com/) - automate tasks


## 1. Install gulp
Install gulp

	npm install gulp-cli -g
	npm install gulp -D

Create gulpfile

	touch gulpfile.js

Install gulp livereload 

	npm install --save-dev gulp-server-livereload


## 2. Flask backend
Needed to obfuscate private api keys.

Install dependencies

	pip install -r requirement.txt

Run the backend

	export FLASK_APP=app/backend/app.py
	flask run --host=0.0.0.0