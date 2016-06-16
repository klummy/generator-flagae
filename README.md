# generator-flagae [![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Dependency Status][daviddm-image]][daviddm-url] [![Coverage percentage][coveralls-image]][coveralls-url]
> This generates an API focused Flask app that is proconfigured for Google AppEngine

_This is currently very basic and would be improved overtime_

## Installation

First, install [Yeoman](http://yeoman.io) and generator-flagae using [npm](https://www.npmjs.com/) (we assume you have pre-installed [node.js](https://nodejs.org/)).

```bash
npm install -g yo
npm install -g generator-flagae
```

Then generate your new project:

```bash
yo flask-gae-api
```

## Options
- Appname - [Done] Remember to underscorify it to avoid Python errors
- Pip install - Prompt [Done]
- AppEngine ID - Input [Done]
- Include MkDocs documentation - Confirm [Done]
- Choose base frontend library/framework - React, AngularJS, Plain HTML [Halfway] Include & configure boilerplates for each code.
- Include example api code - Confirm
- Include authentication - Confirm
- Include base classes - Confirm


## Credit
The base of the application was scaffolded based on the [appengine-flask-skeleton](https://github.com/GoogleCloudPlatform/appengine-flask-skeleton). The frontend boilerplate is based on [this gulp-frontend-template](https://github.com/dmnsgn/gulp-frontend-boilerplate)

## License

Apache-2.0 © [Yekeen Ajeigbe](yekeen.me)


[npm-image]: https://badge.fury.io/js/generator-flagae.svg
[npm-url]: https://npmjs.org/package/generator-flagae
[travis-image]: https://travis-ci.org/klummy/generator-flagae.svg?branch=master
[travis-url]: https://travis-ci.org/klummy/generator-flagae
[daviddm-image]: https://david-dm.org/klummy/generator-flagae.svg?theme=shields.io
[daviddm-url]: https://david-dm.org/klummy/generator-flagae
[coveralls-image]: https://coveralls.io/repos/klummy/generator-flagae/badge.svg
[coveralls-url]: https://coveralls.io/r/klummy/generator-flagae
