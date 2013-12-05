///
///Archivo iptables.js
///

$(document).ready(function(){
    	
});
function save(ant,nue,arch){
	var original=ant.trim();
	var nuevo=nue.trim();
        var flag=0;
      $.ajax({
        type: "POST",
        url: "iptables_save.cgi",
        async: false,
        data:{flag:flag,original:original,nuevo:nuevo,arch:arch},
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

function adicionar(tag,val){
        var ip=prompt("Direccion IP");
        var arch=$("#archivo").val();
        ant=val;
        nue=ant+","+ip;
        
	save(ant,nue,arch);
        apply();
	recarga();
}

function adicionar_url(tag,val){
        var url=prompt("Dirección WEB, Dominio ej: www.facebook.com ej: facebook.com");
        var arch=$("#archivo").val();
        ant=val;
        nue=ant+","+url;
        save(ant,nue,arch);
        apply();
	recarga();
}

function quitar(i,ip){
        var ant=$('#ips-ant').val();
        var rem;
        if (i==0){
            rem=ip+",";
        }
        else{
            rem=","+ip;;
        }
        var nue=ant.replace(rem,"");
        var arch=$("#archivo").val();
        save(ant,nue,arch);
        apply();
	recarga();
}
function quitar_url(i,ip){
        var ant=$('#dom-ant').val();
        var rem;
        if (i==0){
            rem=ip+",";
        }
        else{
            rem=","+ip;;
        }
        var nue=ant.replace(rem,"");
        var arch=$("#archivo").val();
        save(ant,nue,arch);
        apply();
	recarga();
}

function apply(){
      var flag=1;
      $.ajax({
        type: "POST",
        url: "iptables_save.cgi",
        async: false,
        data:{flag:flag},
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

function modificar(tag,i){
        var ant=("="+"\""+i+"\"");
	var arch=$("#archivo").val();
	var nue=("="+"\""+$("#"+tag).val()+"\"");    
        if (tag=="server"){
            ant=("SERVER="+"\""+i+"\"");
            nue=("SERVER="+"\""+$("#"+tag).val()+"\"");    
        }
        if (tag=="glob"){
            if (i=="SI"){
                ant="GLOB_BLOCK=\"SI\"";
                nue="GLOB_BLOCK=\"NO\"";
            }
            else{
                nue="GLOB_BLOCK=\"SI\"";
                ant="GLOB_BLOCK=\"NO\"";
            }
        }
        save(ant,nue,arch);
        apply();
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
