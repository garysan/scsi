$(document).ready(function(){
    $('#addModulo').hide();
    $('#addItem').hide();
    $("#botones").hide();
    flag=0;
    
    cargar_select(flag);
    
    $('#modulo').change(function() {
    var selectVal = $('#modulo :selected').attr('id');
    $('#item').empty();
    $("#showruta").val("Menu principal sin ruta");
    if (selectVal === "adnmod"){
        $('#valor').focus();
        $("#addModulo").submit(function( event ) {
        if ($("#addModulo").find('input[name="valor"]').val()!=""){
             procesar(2,$("#addModulo").find('input[name="valor"]').val());
             $(this).dialog("close");
        }
        else{
            $("#resultado").text("Hey! no introdujo un valor.");
            $("#valor").val('');
            $("#valor").focus();
        }
        event.preventDefault();
        });
        $("#addModulo").dialog({
            modal:true,
            open: function() {
                $( this ).find( "[type=submit]" ).hide();
            }
        });    
    }
    else{       
        cargarLista(selectVal);
    }
    });
	
    $('#item').change(function() {
    var nmod = $('#modulo :selected').attr('id');
    var item = $('#item :selected').attr('id');
    var dialog, form;
    if (item === "adnite"){
        dialog = $("#addItem").dialog({
            modal: true,
            autoOpen: false,
            buttons: {
                "Registrar": function(){
                    var desc = $("#desc");
                    var ruta = $("#ruta");
                    procesar_item(3,desc.val(),ruta.val());  
                    $(this).dialog("close");
                },
                "Cancelar": function() {
                    $(this).dialog("close");
                }
            }
        });  
        
        dialog.dialog( "open" );
        
        form = dialog.find("#addItem").on( "submit", function( event ) {
        event.preventDefault();
    });
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