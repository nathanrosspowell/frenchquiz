//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module.exports = function(options){
    var result = '';
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // List all of the quiz YAML files.
    var quizes = [
        { 
            name: "Basic Quiz",
            context: this.quiz
        },
        { 
            name: "Next Quiz",
            context: this.quiz2
        }
    ];
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // Execute the options function on each object.
	for (var i = 0; i < quizes.length; i++) {
        var context = quizes[i].context;
        context.name = quizes[i].name;
        context.index = i;
        result += options.fn( context );
	}
	return result;
};
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~