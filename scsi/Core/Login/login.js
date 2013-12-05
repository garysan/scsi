$(document).ready(function(){
	$("#usuario").focus();
    $("#ingresar").click(function(){
    	ingresar();
    });
    $(document).keypress(function(e) {
        if(e.which == 13) {
        ingresar();
        }	
    });
});
function ingresar(){
	//$("#resultado").html("test");
    if (usuario.length!=0 && password.length!=0){
      $.ajax({
        type: "POST",
        url: "login.cgi",
        async: false,
        data:{usuario:$("#usuario").val(),password:$("#password").val()},
        success: function(msg){
            $("#resultado").fadeIn(0);
            $("#resultado").html(msg).fadeOut(4000);
            $('#usuario').focus();
        },
        error: function(){
            $("#resultado").fadeIn(0);
            $("#resultado").html(msg).fadeOut(4000);
            $('#usuario').focus();
        }
      }); // ajax
      
    } // if
    else{
         $("#resultado").fadeIn(0);
         $("#resultado").html("<b>Error, verifique los campos requeridos.</b>");
         $("#resultado").fadeOut(4000);
         if (usrn.length==""){
             $('#usuario').focus();
         }
         if (clave.length==""){
             $('#clave').focus();
         }		        	    
    }
}

function go_link(pagina)
{
	document.location = pagina;
}

function limpiar_login(){
    $("#usuario").val('');
    $("#password").val('');
    $("#usuario").focus();
}

		    