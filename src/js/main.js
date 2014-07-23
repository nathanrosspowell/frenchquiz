//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
function sanitise( text ) {
    return text.toLowerCase().latinise();
}
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
function validateFormWithAnswer( formId, answer ) {
    console.log( formId + " With " + answer );
    $(formId).bootstrapValidator({
        message: 'Not the right answer',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        submitHandler: function(validator, form, submitButton) {
            // Do nothing
        },
        fields: {
            question: {
                validators: {
                    notEmpty: {
                        message: 'Type in your answer...'
                    },
                    callback: {
                        message: 'Wrong answer :(',
                        callback: function(value, validator) {
                            return sanitise(value)== sanitise(answer);
                        }
                    }
                }
            }
        }
    });
}
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~