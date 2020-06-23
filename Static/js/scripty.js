
$(document).ready(function(){
    console.log("loaded");
    $('body').bootstrapMaterialDesign();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log("form submitted");
    });
});
