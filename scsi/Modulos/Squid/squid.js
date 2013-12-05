$(document).ready(function(){
    //$("#registrar").click(function(){
    //	alert($("#new1").val());
    //});
	 $("#form1").submit(function(){
		 $.ajax({
		      type: "POST",
		      url: "../../Tools/save.cgi",
		      async: false,
		      data: $(this).serialize(),
		      success: function(msg){
		      	$("#resultado").fadeIn(0);
		        $("#resultado").html(msg).fadeOut(3000);
		      },
		      error: function(){
		      	$("#resultado").fadeIn(0);
		        $("#resultado").html(msg).fadeOut(3000);
		      }
		    }) // ajax
		    return false;
		  });
	 $("#form1m").submit(function(){
             alert("XXXX");
		 $.ajax({
		      type: "POST",
		      url: "../../Tools/savem.cgi",
		      async: false,
		      data: $(this).serialize(),
		      success: function(msg){
		      	$("#resultado").fadeIn(0);
		        $("#resultado").html(msg).fadeOut(3000);
		      },
		      error: function(){
		      	$("#resultado").fadeIn(0);
		        $("#resultado").html(msg).fadeOut(3000);
		      }
		    }) // ajax
		    return false;
		  });
	 //document.getElementById("txt").readOnly=true;
	 $(".slider").slider({
		    min: 0,
		    max: 200,
		    step: 1,
		    slide: function (event, ui) {
		        $(this).parent().find(".inputNumber").val(ui.value);
		    },
		    stop:  function (event, ui) {
		    	var row= $(this).closest("tr")[0].rowIndex;
		    	var delay= $('#tabla_delay tr:eq(' + row + ') td:eq(0)').text();
		    	var clase= $('#tabla_delay tr:eq(' + row + ') td:eq(1)').text();
		    	var kbpsf=ui.value*1024;
		    	var arch=$("#archivo").val();
		    	var ant=$("#original"+delay).val();
		    	var nue;
		    	if (ui.value==0){
		    		nue="delay_parameters "+delay+" -1/-1 -1/-1";
		    		}
		    	else{
		    		nue="delay_parameters "+delay+" "+kbpsf+"/"+kbpsf+" "+kbpsf+"/"+kbpsf;
		    	}
		    	//alert (ant);
		    	//alert (nue);
		    	save(ant,nue,arch);
		    	recarga();
		    },
		    create: function(event, ui){
		        $(this).slider('value',$(this).parent().find(".inputNumber").val());
		    }
		}	 
	 );
	 

	 
});
//////Funciones Extra

function squidguard(id,flag){
	var arch=$("#archivo").val();
	var original=($("#original"+id).val());
	var nuevo="";
	if (flag=="0"){//Para desactivar
		nuevo=$("#original"+id).val().replace($("#original"+id).val(),"#"+$("#original"+id).val());
	}
	else{///para activar
		nuevo=$("#original"+id).val().replace("#","");
	}
	save(original,nuevo,arch);
	recarga();
}


function parser_ip(id){
	var arch=$("#archivo").val();
	var original=($("#original"+id).val());
	var origen  =($("#ant"+id).val());
	var destino =($("#ip"+id).val()+"/"+$("#subnet"+id).val());
	var nuevo=$("#original"+id).val().replace(origen,destino);
	save(original,nuevo,arch);
}

function parser(id,tag){
	var arch=$("#archivo").val();
	var original=($("#original"+id).val());
	var origen  =($("#ant"+id).val());
	var destino =($("#"+tag+id).val());
	var nuevo=$("#original"+id).val().replace(origen,destino);
	save(original,nuevo,arch);
}

function save(ant,nue,arch){
	var original=ant.trim();
	var nuevo=nue.trim();
      $.ajax({
        type: "POST",
        url: "squid_guardar_lista.cgi",
        async: false,
        data:{original:original,nuevo:nuevo,arch:arch},
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

function insRow(i){
	var nlist=prompt("Direccion IP");
        if (ipValida(nlist)==true){
            i++;
            var tbla= "#listas";
            var n = $('tr:last td', $(tbla)).length;
            var args= " url_regex -i";
            var tds = '<tr>';
            /////Valores para insertar.
            tds += '<td>'+i+':</td>';
            tds += '<td><input type="hidden" name=original'+i+' value='+nlist+'>';
            tds += '<input name="new'+i+'" value='+nlist+'></td>';
            //tds += '<td><input class=button type=button value=Modificar onclick=parser_ip('+i+')>';
            //tds += '<input class=button type=button value=Eliminar onclick=borrar('+i+')><td>';
            tds += '</tr>';
            $(tbla).append(tds);
            $("#number").val(i);
            $("#flag").val('5');
            var arch=$("#archivo").val();
            var ant=$("#new"+(i-1)).val();
            save(ant,""+ant+'\n'+nlist+"",arch);
            recarga();
        }
        else{
              var msg="<b>Dirección IP Invalida</b>";
            $("#resultado").fadeIn(0);
            $("#resultado").html(msg).fadeOut(3000);
        }
            
	
}

function insRowL(i){
	var xlist=prompt("Nombre de la lista.");
	var nlist=prompt("Ubicación de la Lista.");
	
        if (xlist!=null && nlist!=null){
        
	i++;
	if ($("#tabla_bloqueo").length){
		var tbla= "#tabla_bloqueo";
		var n = $('tr:last td', $(tbla)).length;
		var args= " url_regex -i";
		}
	else{
		var tbla= "#tabla_lista";
		var n = $('tr:last td', $(tbla)).length;
		var args= " src";
	}

	var tds = '<tr>';
	/////Valores para insertar.
	tds += '<td>'+xlist+'<input type="hidden" name=name'+i+' value="'+xlist+args+'" ></td>';
	tds += '<td></td>';
	tds += '<td><input type="hidden" name=original'+i+' value='+nlist+'>';
	tds += '<input name="new'+i+'" value='+nlist+'></td>';
	tds += '</tr>';
	$(tbla).append(tds);
	$("#number").val(i);
	$("#flag").val('1');
        }
        else{
            var msg="<b>No se permiten valores vacios</b>";
            $("#resultado").fadeIn(0);
            $("#resultado").html(msg).fadeOut(3000);
        }
            
}

function activar(i)
{
	var arch=$("#archivo").val();
	var ant=$("#new"+i).val();
	var nue=ant.replace("#","");
	/*alert (ant);
	alert (nue);
	alert (arch);*/
	save(ant,nue,arch);
	recarga();
} 

function desactivar(i)
{
	var arch=$("#archivo").val();
	var ant=$("#new"+i).val();
	/*alert (ant);
	alert ('#'+ant);
	alert (arch);*/
	save(ant,'#'+ant+"",arch);
	recarga();
} 

function modificar(i)
{
	var arch=$("#archivo").val();
	var ant=$("#original"+i).val();
	var nue=$("#new"+i).val();
	/*alert (ant);
	alert (nue);
	alert (arch);*/
	save(ant,nue,arch);
	recarga();
} 

function denegar_item(item)
{
	var arch=$("#archivo").val();
	var ant=$("#anterior").val();
	var nue=ant.replace(item,"");
	//var nue="";
	/*alert (ant);
	alert (nue);
	alert (arch);*/
	save(ant,nue,arch);
	recarga();
} 
function listas(i,item,flag)
{
	var arch=$("#archivo").val();
	var ant=$("#anterior"+i).val();
	var nue="";
        
        if (flag==0){
            nue="#"+ant;
        }
        else{
            nue=ant.replace("#","")
        }
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

		    