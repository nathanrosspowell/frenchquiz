function sanitise(a){return a.toLowerCase().latinise()}function validateFormWithAnswer(a,b){$(a).bootstrapValidator({message:"Not the right answer",feedbackIcons:{valid:"glyphicon glyphicon-ok",invalid:"glyphicon glyphicon-remove",validating:"glyphicon glyphicon-refresh"},submitHandler:function(){},fields:{question:{validators:{notEmpty:{message:"The first name is required"},callback:{message:"Wrong answer",callback:function(a){return sanitise(a)==sanitise(b)}}}}}})}