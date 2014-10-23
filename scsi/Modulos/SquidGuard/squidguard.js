///
///Archivo squidguard.js
///

$(document).ready(function(){
    	
});

//////////Principal de guardado
function save(ant,nue,arch){
    var original=ant.trim();
    var nuevo=nue.trim();
    $("#resultado").html("<b>Procesando... Espere por favor.</b>");
    $.ajax({
        type: "POST",
        url: "squidguard_save.cgi",
        data:{
        	  original:original,
        	  nuevo:nuevo,
        	  arch:arch
        	},
        success: function(msg){
        	$("#resultado").fadeIn(0);
            $("#resultado").html(msg).fadeOut(3000);
        },
        error: function(){
        	$("#resultado").fadeIn(0);
            $("#resultado").html(msg).fadeOut(3000);
            
        }
      }); // ajax
}

//////Funciones Extra
$(function() {
    var valor = $( "#valor" ),
      allFields = $( [] ).add( valor ),
      tips = $( ".validateTips" );
    
    $( "#dialog-form" ).dialog({
      autoOpen: false,
      height: 300,
      width: 350,
      draggable:false,
      resizable:false,
      modal: true,
      closeOnEscape:false,
      buttons: {
        "Aceptar": function() {
            if ($("#fin").val()=="0"){
        		if (webValida(valor.val())==true){
        			proceso2(valor.val());		
            	}
            	else{
            		alert("WEB Invalida!");
            	}        	}
        	else{
        		if (ipValida(valor.val())==true){
        			proceso(valor.val());		
            	}
            	else{
            		alert("IP Invalida!");
            	}
        		
        	}	
        	$( this ).dialog( "close" );
        },
        "Cancelar": function() {
          $( this ).dialog( "close" );
        }
      },
      close: function() {
        allFields.val( "" ).removeClass( "ui-state-error" );
      }
    });
  });

function nuevo(){
	$( "#dialog-form" ).dialog( "open" );
}
function modificar(){
	$( "#dialog-form" ).dialog( "open" );
}
function quitar(ip){
	var arch=$("#archivo").val();
	var nue="";
	var ant="ip "+ip
	save(ant,nue,arch);
	recarga();
}
function proceso(i){
	var fin=$("#fin").val();
	var ant=("ip "+$("#new"+fin).val());
	var arch=$("#archivo").val();
	var nue=(ant+"\nip "+i);
	save(ant,nue,arch);
	recarga();
}
function proceso2(i){
	var ant =($("#original"+$("#id").val()).val());
	var arch=$("#archivo").val();
	var nue = "redirect "+i;
	save(ant,nue,arch);
	recarga();
} 

function recarga()
{
	//parent.frames['top'].location.recarga(true);
	var frameDocument = $('frame[name="main"]', top.document)[0].contentDocument;
	$(frameDocument).find('body').prepend('<script language="JavaScript">location.reload();</script>');
	
	//parent.frames[frameDocument].location.recarga(true);
	
} 

function ipValida(str) {
    //if (str.match(/^\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b$/)) {
	//if (str.match(/^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$/)){
	if (str.match(/^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/)){
        return true; 
    } else { 
        return false;
    }
}
function webValida(str){
	if (str.match(/(http):\/\/([_a-z\d\-]+(\.[_a-z\d\-]+)+)(([_a-z\d\-\\\.\/]+[_a-z\d\-\\\/])+)*/)){
		return true;
	}
	else { 
        return false;
    }
}
