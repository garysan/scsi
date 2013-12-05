$(document).ready(function(){
	$("#botones").hide();
	flag=0;
	cargar_select(flag);
	$('#modulo').change(function() {
        var selectVal = $('#modulo :selected').attr('id');
        $('#item').empty();
        $("#showruta").val("Menu principal sin ruta");
        if (selectVal == "adnmod"){
            registrar_menu();  
        }
        else{       
            cargarLista(selectVal);
        }
    });
	
	$('#item').change(function() {
        var nmod = $('#modulo :selected').attr('id');
        var item = $('#item :selected').attr('id');

        if (item == "adnite"){
           registrar_item();
        }
        else{
            cargarRuta(nmod,item);
        }
    });
    $('#update').click(function(){
        var nmod = $('#modulo :selected').attr('id');
        var item = $('#item :selected').attr('id');
        var ruta = $("#showruta").val();
        update(8,nmod,item,ruta);
    });
    $('#quitar').click(function(){
        var nmod = $('#modulo :selected').attr('id');
        var item = $('#item :selected').attr('id');
        baja(9,nmod,item);
    });

});

function update(flag,nmod,item,ruta){

    $.ajax({ 
        type: "POST",
        url: "menu.cgi",
        data: {flag:flag,nmod:nmod,item:item,ruta:ruta},
        success: function(msg){
            $("#resultado").html(msg).fadeIn(0); 
            $("#resultado").html(msg).fadeOut(4000);
             
        },
        error: function(){
           $("#resultado").text("Error al actualizar");
           $("#resultado").fadeIn(0);
           $("#resultado").html(msg);
        }
     });  
}  
function baja(flag,nmod,item){

    $.ajax({ 
        type: "POST",
        url: "menu.cgi",
        data: {flag:flag,nmod:nmod,item:item},
        success: function(msg){
            $("#resultado").html(msg).fadeIn(0); 
            $("#resultado").html(msg).fadeOut(4000);
             
        },
        error: function(){
           $("#resultado").text("Error al dar de baja");
           $("#resultado").fadeIn(0);
        }
     });  
}  

var flag;
function registrar_menu(){
    flag=2;
    $( "#dialog-form" ).dialog( "open" );
}

function registrar_item(){
    flag=3;
    $( "#dialog-form-sub" ).dialog( "open" );
}

//////Funciones Extra

function procesar(flag,desc){
	
	var arch=$("#arch").val();
      $.ajax({
        type: "POST",
        url: "menu.cgi",
        data:{flag:flag,desc:desc,arch:arch},
        success: function(msg){
        	$("#resultado").fadeIn(0);
            $("#resultado").html(msg).fadeOut(4000, function(){location.reload();});
            $('#nmod').focus();
        },
        error: function(){
            $("#resultado").html(msg).fadeIn(0);
        }
      }); // ajax

};

function procesar_item(flag,desc,ruta){
 var nmod = $('#modulo :selected').attr('id');
    $.ajax({ 
      type: "POST",
      url: "menu.cgi",
      data: {flag:flag,desc:desc,ruta:ruta,nmod:nmod},
       success: function(msg){
          $("#resultado").fadeIn(0);
          $("#resultado").html(msg).fadeOut(4000);
      },
      error: function(){
          $("#resultado").fadeIn(0);
          $("#resultado").html(msg).fadeOut(4000);
      }
   });

};

function cargar_select(flag){
	 $.ajax({
	        type: "POST",
	        url: "menu.cgi",
	        data:{flag:flag},
	        success: function(msg){
	        	$("#modulo").append(msg);
	        	$("#modulo").append("<option id='adnmod'>Adicionar Nuevo Modulo</option>");
	        },
	        error: function(){
	        	$("#resultado").html(msg).fadeIn(0);
	        }
	      }); // ajax
}
function cargarLista(nmod){
	 flag=1
	 $.ajax({
	        type: "POST",
	        url: "menu.cgi",
	        data:{flag:flag,nmod:nmod},
	        success: function(msg){
	        	$('#item').append("<option></option>");
	        	$("#item").append(msg);
	        	$("#item").append("<option id='adnite'>Adicionar Item a Menu</option>");
	        },
	        error: function(){
	        	$("#resultado").html(msg).fadeIn(0);
	        }
	      }); // ajax
}
function cargarRuta(nmod,item){
    var flag=4;

    $.ajax({ 
        type: "POST",
        url: "menu.cgi",
        data: {flag:flag,nmod:nmod,item:item},
        success: function(msg){
           $("#showruta").val("");
           $("#showruta").val(msg);
           $("#botones").show();
             
        },
        error: function(){
           $("#resultado").text("Error al obtener la ruta");
           $("#resultado").fadeIn(0);
           $("#resultado").html(msg);
        }
     });  
};

function clean(){
	$("#nmod").val('');
    $("#arch").val('');
    $("#desc").val('');
    $("#nmod").focus();
}

		    
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
           if ($("#fin").val()!=""){
                        procesar(flag,valor.val());
            	}
            	else{
            		alert("No puede quedar vacio");
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
////////////////////ITEM de MEnu
$(function() {
      var desc = $( "#desc" ),
          ruta = $( "#ruta" ),
      allFields = $( [] ).add( desc ).add( ruta ),
      tips = $( ".validateTips" );
      $( "#dialog-form-sub" ).dialog({
      autoOpen: false,
      height: 300,
      width: 350,
      draggable:false,
      resizable:false,
      modal: true,
      closeOnEscape:false,
      buttons: {
        "Aceptar": function() {
           if ($("#fin").val()!=""){
                        procesar_item(flag,desc.val(),ruta.val());
            	}
            	else{
            		alert("No puede quedar vacio");
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