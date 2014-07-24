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
                        message: '<span class="octicon octicon-keyboard"></span> Please type in your answer'
                    },
                    callback: {
                        message: 'Not quite right...',
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