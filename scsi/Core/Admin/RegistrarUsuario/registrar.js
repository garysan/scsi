$(document).ready(function(){
	$("#usuario").focus();
    $("#registrar").click(function(){
    	registrar();
    });
    $(document).keypress(function(e) {
        if(e.which == 13) {
        registrar();
        }	
    });
});
function registrar(){
    if (usuario.length!=0 && password.length!=0){
      $.ajax({
        type: "POST",
        url: "registrar.cgi",
        async: false,
        data:{	usuario:$("#usuario").val(),
        		nombre:$("#nombre").val(),
        		email:$("#email").val(),
        		rol:$("#rol").val(),
        		password:$("#password").val()
        		},
        success: function(msg){
        	$("#resultado").fadeIn(0);
            $("#resultado").html(msg);
            $('#usuario').focus();
        },
        error: function(){
        	$("#resultado").fadeIn(0);
            $("#resultado").html(msg);
            $('#usuario').focus();
        }
      }); // ajax
      
    } // if
    else{
         $("#resultado").fadeIn(0);
         $("#resultado").html("<b>Error, verifique los campos requeridos.</b>");
         $("#resultado").fadeOut(3000);
         if (usrn.length==""){
             $('#usuario').focus();
         }
         if (clave.length==""){
             $('#clave').focus();
         }		        	    
    }
}

function limpiar_registro(){
    $("#usuario").val('');
    $("#nombre").val('');
    $("#email").val('');
    $("#rol").val('');
    $("#password").val('');
    $("#usuario").focus();
}

		    