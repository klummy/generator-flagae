'use strict';
var yeoman = require('yeoman-generator');
var chalk = require('chalk');
var yosay = require('yosay');
var path = require('path');
var underscored = require("underscore.string");


module.exports = yeoman.Base.extend({
  prompting: function () {
    // Have Yeoman greet the user.
    this.log(yosay(
      'Welcome to the remarkable ' + chalk.red('generator-flagae') + ' generator!'
    ));

    var prompts = [{
      type: 'input',
      name: 'appname',
      message: 'What is your project name?',
      default: 'my_app'
    },{
      type: 'input',
      name: 'app_engine_project_id',
      message: 'What is the AppEngine ID of your project?',
      default: 'my-app'
    },{
      type: 'list',
      name: 'frontend_library',
      message: 'Which frontend library do you want included?',
      choices: [ 'None', 'AngularJS', 'React'],
      filter: function (val) {
        return val.toLowerCase();
      }
    },{
      type: 'confirm',
      name: 'install_pip',
      message: 'Do you want to install pip dependencies after installation?'
    },{
      type: 'confirm',
      name: 'include_mkdocs',
      message: 'Do you want to include MkDocs documentation?',
      default: false
    }];

    return this.prompt(prompts).then(function (props) {
      // To access props later use this.props.someAnswer;
      this.props = props;
    }.bind(this));
  },

  writing: function () {

    // Assign props values to variables to reduce bloat.
    var appname = underscored(this.props.appname).trim().slugify().underscored().value(),
        frontend_library = this.props.frontend_library;


    // Write app.yaml file; use passed app_engine_project_id as project id & run file named with project name as the main script
    this.fs.copyTpl(
      this.templatePath('app.yaml'),
      this.destinationPath(appname+'/app.yaml'),
      { app_engine_project_id: this.props.app_engine_project_id, appname: appname }
    );

    // Copy in appengine_config file.
    this.fs.copy(
      this.templatePath('appengine_config.py'),
      this.destinationPath(appname+'/appengine_config.py')
    );

    // Copy in requirements.txt file - can pass in options later on
    this.fs.copyTpl(
      this.templatePath('requirements.txt'),
      this.destinationPath(appname+'/requirements.txt'),
      {}
    );

    // Copy in run.py file & rename to appname - can pass in options later on
    this.fs.copyTpl(
      this.templatePath('run.py'),
      this.destinationPath(appname+'/'+appname+'.py'),
      {}
    );

    // Copy settings.py file - can pass in options later on
    this.fs.copyTpl(
      this.templatePath('settings.py'),
      this.destinationPath(appname+'/settings.py'),
      { secret_key: (Math.random()*1e64).toString(36), csrf_key : (Math.random()*1e64).toString(36) }
    );

    if(this.props.include_mkdocs) {


      // Copy mkdocs config file
      this.fs.copyTpl(
        this.templatePath('docs/mkdocs.yml'),
        this.destinationPath(appname+'/docs/mkdocs.yml'),
        { appname: appname }
      );

      this.fs.copyTpl(
        this.templatePath('docs/docs'),
        this.destinationPath(appname+'/docs/docs'),
        {}
      );
    };

    this.fs.copy(
      this.templatePath('main'),
      this.destinationPath(appname+'/main')
    );

    if (frontend_library == 'angularjs') {
      this.fs.copy(
        this.templatePath('partials/angularjs/static'),
        this.destinationPath(appname+'/main/static')
      );
      this.fs.copy(
        this.templatePath('partials/angularjs/templates'),
        this.destinationPath(appname+'/main/templates')
      );
    } else if(frontend_library == 'react') {
      this.fs.copy(
        this.templatePath('partials/react/static'),
        this.destinationPath(appname+'/main/static')
      );
      this.fs.copy(
        this.templatePath('partials/react/templates'),
        this.destinationPath(appname+'/main/templates')
      );
    } else {
      this.fs.copy(
        this.templatePath('partials/plain/static'),
        this.destinationPath(appname+'/main/static')
      );
      this.fs.copy(
        this.templatePath('partials/plain/templates'),
        this.destinationPath(appname+'/main/templates')
      );
    };

  },

  install: function () {

    var appname = underscored(this.props.appname).trim().slugify().underscored().value();

    if(this.props.install_pip) {
      this.spawnCommand('pip', ['install', '-r', appname+'/requirements.txt', '-t', appname+'/lib/']);
    }
  },
});
