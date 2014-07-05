/*
module.exports = function( collection, count, options ){
    var collections = Array.prototype.slice.call( arguments, 0, -1 );
	options = Array.prototype.slice.call(arguments, arguments.length-1, arguments.length);
    console.log( JSON.stringify(arguments) );
    console.log( "==================" );
    console.log( JSON.stringify(options) );
    console.log( "==================" );
    console.log( JSON.stringify(collections.length) );
    console.log( "==================" );
	var result = '';
	var i = 0;
    for (var i = 0; i < collections.length; i++) {
        console.log( JSON.stringify(collections[i]) );
        console.log( "==================" );
        result += options.fn( collections[i] );
	}
	return result;
};
*/
module.exports = function(options){
    var quizes = [
          this.quiz
        , this.quiz2
    ];
    var result = '';
	for (var i = 0; i < quizes.length; i++) {
        result += options.fn( quizes[i] );
	}
	return result;
};
