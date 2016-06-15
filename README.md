# generator-flask-gae-api [![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Dependency Status][daviddm-image]][daviddm-url] [![Coverage percentage][coveralls-image]][coveralls-url]
> This generates an API focused Flask app that is proconfigured for Google AppEngine

_This is currently very basic and would be improved overtime_

## Installation

First, install [Yeoman](http://yeoman.io) and generator-flask-gae-api using [npm](https://www.npmjs.com/) (we assume you have pre-installed [node.js](https://nodejs.org/)).

```bash
npm install -g yo
npm install -g generator-flask-gae-api
```

Then generate your new project:

```bash
yo flask-gae-api
```

## Options
- Appname - [Done] Remember to underscorify it to avoid Python errors
- Pip install - Prompt [Done]
- AppEngine ID - Input
- Include MkDocs documentation - Confirm
- Include example api code - Confirm
- Include authentication - Confirm
- Include base classes - Confirm
- Choose base frontend library/framework - React, AngularJS, Plain HTML


## Credit
The base of the application was scaffolded based on the [appengine-flask-skeleton](https://github.com/GoogleCloudPlatform/appengine-flask-skeleton). The frontend boilerplate is based on [this gulp-frontend-template](https://github.com/dmnsgn/gulp-frontend-boilerplate)

## License

Apache-2.0 © [Yekeen Ajeigbe](yekeen.me)


[npm-image]: https://badge.fury.io/js/generator-flask-gae-api.svg
[npm-url]: https://npmjs.org/package/generator-flask-gae-api
[travis-image]: https://travis-ci.org/klummy/generator-flask-gae-api.svg?branch=master
[travis-url]: https://travis-ci.org/klummy/generator-flask-gae-api
[daviddm-image]: https://david-dm.org/klummy/generator-flask-gae-api.svg?theme=shields.io
[daviddm-url]: https://david-dm.org/klummy/generator-flask-gae-api
[coveralls-image]: https://coveralls.io/repos/klummy/generator-flask-gae-api/badge.svg
[coveralls-url]: https://coveralls.io/r/klummy/generator-flask-gae-api
