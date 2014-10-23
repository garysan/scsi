$(document).ready(function(){
    $('#ip').focus();
    $(document).keypress(function(e) {
    if(e.which == 13) {
          consultar($('#ip').val());    
    }
});
    
 $('#ip').keyup(function(){
      this.value = this.value.replace(/[^0-9\.]/g,'');
    });
    $('#ip').focusout(function(){
      if ($(this).val().match(/(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/)){
      }else{
        mensaje("IP Invalida!");
        $('#ip').focus();}
        
  });   
    
});
function consultar(ip){    
      $.ajax({
        type: "POST",
        url: "byip.cgi",
        data:{ip:ip},
        success: function(msg){
        	$("#resultado").html(msg);
        },
        error: function(){
            $("#resultado").html(msg);
        }
      }); // ajax
    }
function mensaje(valor){
     $("#mensaje").fadeIn(0);
     $("#mensaje").html('<b>'+valor+'</b>');//.fadeOut(3000);
     $(this).focus();
}
		    
                    