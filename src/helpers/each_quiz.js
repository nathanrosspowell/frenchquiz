//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module.exports = function(options){
    var result = '';
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // List all of the quiz YAML files.
    var quizes = [
        { 
            name: "Verbs",
            id: "verbs",
            context: this.verbs
        },
        { 
            name: "Next Quiz",
            id: "next_quiz",
            context: this.quiz2
        }
    ];
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // Execute the options function on each object.
	for (var i = 0; i < quizes.length; i++) {
        var context = quizes[i].context;
        context.name = quizes[i].name;
        context.id = quizes[i].id;
        context.index = i;
        result += options.fn( context );
	}
	return result;
};
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~