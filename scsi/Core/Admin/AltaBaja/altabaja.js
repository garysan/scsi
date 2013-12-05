$(document).ready(function(){
	
    cargar1(0);
    cargar9(2);

    $('#activar').click(function(){
        var usuario = $('#usuario9 :selected').attr('id');
        procesar(1,usuario);
    });
    $('#desactivar').click(function(){
        var usuario = $('#usuario1 :selected').attr('id');
        procesar(9,usuario);
    });

});

function procesar(flag,user){
    $.ajax({ 
        type: "POST",
        url: "altabaja.cgi",
        data: {flag:flag,user:user},
        success: function(msg){
           $("#resultado").html(msg).fadeOut(4000, function(){location.reload();});
             
        },
        error: function(){
           $("#resultado").text("Error al procesar solicitud");
           $("#resultado").fadeIn(0);
           $("#resultado").html(msg);
        }
     });  
}  


function cargar1(flag){
	 $.ajax({
	        type: "POST",
	        url: "altabaja.cgi",
	        data:{flag:flag},
	        success: function(msg){
	        	$("#usuario1").append(msg);
	        },
	        error: function(){
	        	$("#resultado").html(msg).fadeIn(0);
	        }
	      }); // ajax
}
function cargar9(flag){
	 $.ajax({
	        type: "POST",
	        url: "altabaja.cgi",
	        data:{flag:flag},
	        success: function(msg){
	        	$("#usuario9").append(msg);
	        },
	        error: function(){
	        	$("#resultado").html(msg).fadeIn(0);
	        }
	      }); // ajax
}

function clean(){
	$("#nmod").val('');
    $("#arch").val('');
    $("#desc").val('');
    $("#nmod").focus();
}
