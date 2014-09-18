//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
var fs = require('fs');
var path = require('path');
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
var builtJSON = 'temp/built.json';
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module.exports = function(grunt) {
    grunt.file.defaultEncoding = 'utf8';
    // Project configuration.   
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        uglify: {
            options: {
                compress: {
                    drop_console: false
                }
            },
            frenchQuiz: {
                files: {
                    'build/js/main.js': ['src/js/main.js'],
                    'build/js/scripts.js': ['src/js/scripts.js'],
                }
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        copy: {
            frenchQuiz: {
                files: [{
                    expand: true,
                    cwd: "src/",
                    src: [
                        '**/*', // The full source tree, but...
                        '!**/*.handlebars', // ignore handlebar files,
                        '!**/js/main.js', // ignore this,
                        '!**/js/scripts.js', // ignore this,
                        '!**/yaml/*', // ignore this folder,
                        '!**/partials/*', // ignore this folder,
                        '!**/helpers/*', // and ignore this folder.
                    ],
                    dest: 'build/',
                    filter: "isFile"
                }]
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        yaml: {
            frenchQuiz: {
                options: {
                    space: 4,
                    readEncoding: 'latin1',
                },
                files: [{
                    expand: true,
                    cwd: 'src/yaml/',
                    src: ['**/*.yml'],
                    dest: 'temp/json/'
                }]
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        concat: {
            frenchQuiz: {
                options: {
                    process: function(src, filepath) {
                        var filename = filepath.replace(/^.*[\\\/]/, '')
                        var withoutExt = filename.split('.')[0]
                        return '"' + withoutExt + '": ' + src + ",";
                    },
                },
                files: {
                    'temp/concatfile.json': ['temp/json/*.json']
                },
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        replace: {
            frenchQuiz: {
                options: {
                    patterns: [{
                        match: /\},$/g, // This is the last comma in the file
                        replacement: "}",
                    }]
                },
                files: {
                    'temp/concatfile.json': 'temp/concatfile.json'
                },
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        file_append: {
            frenchQuiz: {
                files: {
                    'temp/built.json': {
                        prepend: "{\n",
                        append: "\n}\n",
                        input: 'temp/concatfile.json'
                    }
                }
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        'compile-handlebars': {
            frenchQuiz: {
                templateData: builtJSON,
                template: [
                    'src/index.handlebars',
                    'src/verbs.handlebars',
                    'src/possession.handlebars',
                    'src/misc.handlebars',
                    'src/about_me.handlebars',
                    'src/basic_1.handlebars'
                ],
                output: [
                    'build/index.html',
                    'build/verbs/index.html',
                    'build/possession/index.html',
                    'build/misc/index.html',
                    'build/about_me/index.html',
                    'build/basic_1/index.html'
                ],
                helpers: [ 
                    'src/helpers/**/*.js', 
                    'node_modules/handlebars-helper/lib/helpers/**/*.js' 
                ],
                partials: ['src/partials/**/*.handlebars']
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        prettify: {
            options: {
                indent: 4
            },
            frenchQuiz: {
                files: [{
                    expand: true,
                    cwd: 'build/',
                    src: ['**/*.html'],
                    dest: 'build/'
                }]
            }
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        jsbeautifier: {
            "frenchQuiz": {
                src: [
                    "Gruntfile.js",
                    "src/main.js",
                    "src/scripts.js",
                ]
            },
        },
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        'gh-pages': {
            frenchQuiz: {
                options: {
                    base: 'build'
                },
                src: ['**']
            }
        }
    });
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // Load tasks.
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-yaml');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-file-append');
    grunt.loadNpmTasks('grunt-gh-pages');
    grunt.loadNpmTasks('grunt-compile-handlebars');
    grunt.loadNpmTasks('grunt-replace');
    grunt.loadNpmTasks('grunt-prettify');
    grunt.loadNpmTasks('grunt-jsbeautifier');
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // Task to turn all text inside of the JSON into markdown output
    grunt.task.registerTask("tomd", "JSON->Markdown", function() {
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        // Function to change all JSON keys names 'markdown'.
        function recurseObject(object) {
            for (var property in object) {
                if (object.hasOwnProperty(property)) {
                    if (typeof object[property] == "object"){
                        recurseObject(object[property]);
                    }else if (typeof object[property] == 'string'){
                        if (property === 'markdown' ){
                            object[property] = 
                                markdown.markdown(object[property]
                                    , options
                                    ,'<%=content%>');
                        }
                    }
                }
            }
        }
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        // Options for grunt-markdown
        var options =  {
            preCompile: function(src, context) {},
            postCompile: function(src, context) {},
            templateContext: {},
            markdownOptions: {
              gfm: true,
              highlight: 'manual',
              codeLines: {
                before: '<span>',
                after: '</span>'
              }
            }
        };
        var markdownLib = './node_modules/grunt-markdown/tasks/lib/markdown';
        var markdown = require(markdownLib).init(grunt);
        //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        // Tell Grunt this task is asynchronous.
        var done = this.async();
        fs.readFile(builtJSON, 'utf8', function (err,data) {
            if (err) {
                return console.log(err);
            }
            var obj = JSON.parse(data);
            recurseObject(obj);
            content = JSON.stringify(obj, null, 2);
            //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            // Write the file out after modifying it.
            fs.writeFile(builtJSON, content, function(err) {
                if(err) {
                    return console.log(err);
                } else {
                    done(true);
                }
            }); 
        });
        
    });
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // Default task: does everything except deployment
    grunt.registerTask('default', [
          'make-yaml'
        , 'handlebars'
        , 'uglify'
        , 'copy'
    ]);
    grunt.registerTask('make-yaml', [
          'yaml'
        , 'concat'
        , 'replace'
        , 'file_append'
        , 'tomd'
    ]);
    grunt.registerTask('handlebars', [
          'compile-handlebars'
        , 'prettify'
    ]);
    // deploy task: runs everything in order.
    grunt.registerTask('deploy', [
          'default'
        , 'gh-pages'
    ]);
};
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
