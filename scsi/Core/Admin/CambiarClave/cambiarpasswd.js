$(document).ready(function(){
	$("#ant").focus();
    $("#cambiar").click(function(){
    	cambiar();
    });
    $(document).keypress(function(e) {
        if(e.which == 13) {
        cambiar();
        }	
    });
});
function cambiar(){    
    if ($("#ant").val().length!=0 && 
    	$("#nueva").val().length!=0 &&
    	$("#cnueva").val().length!=0){
    	if ($("#nueva").val()!=$("#cnueva").val()){
            $("#resultado").html("<b>Las claves no coinciden.</b>").fadeOut(3000);
            $("#nueva").val('');
            $("#cnueva").val('');
            $("#nueva").focus();
        }
        else{
            $("#resultado").html("<b>Procesando... Espere por favor.</b>");
            $.ajax({
            type: "POST",
            url: "cambiarpasswd.cgi",
            data:{ant:$("#ant").val(),nueva:$("#nueva").val(),cnueva:$("#cnueva").val()},
            success: function(msg){
                    $("#resultado").fadeIn(0);
                    $("#resultado").html(msg).fadeOut(3000);
                $('#correo').focus();
            },
            error: function(){
                    $("#resultado").fadeIn(0);
                $("#resultado").html(msg).fadeOut(3000);
                $('#correo').focus();
            }
            }); // ajax
        }
    } // if
    else{
         $("#resultado").fadeIn(0);
         $("#resultado").html("<b>Error, verifique los campos requeridos.</b>").fadeOut(3000);
         if ($("#cnueva").val().length==""){
             $('#cnueva').focus();
         }
        
         if ($("#nueva").val().length==""){
             $('#nueva').focus();
         }
         if ($("#ant").val().length==""){
             $('#ant').focus();
         }
         
        
    }
}

function limpiar_formulario(){
	$("#ant").val('');
	$("#nueva").val('');
	$("#cnueva").val('');
    $("#ant").focus();
}

		    