$(document).ready(function(){
	$("#usuario").focus();
        $("#nombre").convertUpper(6,50);

    $("#registrar").click(function(){
        registrar();
    });
    $(document).keypress(function(e) {
        if(e.which === 13) {
        registrar();
        }	
    });
});
function registrar(){
    var usuario=$("#usuario").val();
    var nombre =$("#nombre").val();
    var email  =$("#email").val();
    var rol    =$("#rol").val();
    
    if (usuario.length!==0 && nombre.length!==0 && email.length!==0){
       $("#resultado").html("<b>Procesando... Espere por favor.</b>");
       $.ajax({ 
        type: "POST",
        url : "registrar.cgi",
        data: {usuario:usuario,nombre:nombre,email:email,rol:rol},
        success: function(msg){
            $("#resultado").html(msg).fadeIn(0);
            /////Recargar
        },
        error: function(){
            $("#resultado").fadeIn(0);
            $("#resultado").html("<b>Error, verifique los campos requeridos.</b>").fadeOut(3000);
            $('#usuario').focus();
        }
        });  
       
    } // if
    else{
         $("#resultado").fadeIn(0);
         $("#resultado").html("<b>Error, verifique los campos requeridos.</b>").fadeOut(3000);   
    }
}

function limpiar_registro(){
    $("#usuario").val('');
    $("#nombre").val('');
    $("#email").val('');
    $("#rol").val('');
    $("#usuario").focus();
}

		    