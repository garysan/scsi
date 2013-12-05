$(document).ready(function(){
	$("#correo").focus();
    $("#enviar").click(function(){
    	enviar();
    });
    $(document).keypress(function(e) {
        if(e.which == 13) {
        enviar();
        }	
    });
});
function enviar(){    
    if ($("#correo").val().length!=0 && $("#usuario").val().length!=0){
      $.ajax({
        type: "POST",
        url: "recuperar.cgi",
        async: false,
        data:{	usuario:$("#usuario").val(),
        		correo:$("#correo").val()
        		},
        success: function(msg){
        	$("#resultado").fadeIn(0);
        	$("#resultado").html(msg);//.fadeOut(3000);
            $('#correo').focus();
        },
        error: function(){
        	$("#resultado").fadeIn(0);
            //$("#resultado").html(msg);//.fadeOut(3000);
            $('#correo').focus();
        }
      }); // ajax
      
    } // if
    else{
         $("#resultado").fadeIn(0);
         $("#resultado").html("<b>Error, verifique los campos requeridos.</b>").fadeOut(3000);
         
         if ($("#correo").val().length==""){
             $('#correo').focus();
         }
         if ($("#usuario").val().length==""){
             $('#usuario').focus();
         }
    }
}

function limpiar_formulario(){
	$("#correo").val('');
	$("#usuario").val('');
    $("#correo").focus();
}

		    