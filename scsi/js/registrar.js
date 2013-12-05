$(document).ready(function(){
	  $("form#loginForm").submit(function() { // loginForm is submitted
		    var usuario = $('#usuario').attr('value'); // get usuario
		    var password = $('#password').attr('value'); // get password

		    if (usuario && password) { // values are not empty
		      $.ajax({
		        type: "GET",
		        url: "login.pl", // URL of the Perl script
		        contentType: "application/json; charset=utf-8",
		        dataType: "json",
		        // send usuario and password as parameters to the Perl script
		        data: "usuario=" + usuario + "&password=" + password,
		        // script call was *not* successful
		        error: function(XMLHttpRequest, textStatus, errorThrown) { 
		          $('div#loginResult').text("responseText: " + XMLHttpRequest.responseText 
		            + ", textStatus: " + textStatus 
		            + ", errorThrown: " + errorThrown);
		          $('div#loginResult').addClass("error");
		        }, // error 
		        // script call was successful 
		        // data contains the JSON values returned by the Perl script 
		        success: function(data){
		          if (data.error) { // script returned error
		            $('div#loginResult').text("data.error: " + data.error);
		            $('div#loginResult').addClass("error");
		          } // if
		          else { // login was successful
		            $('form#loginForm').hide();
		            $('div#loginResult').text("data.success: " + data.success 
		              + ", data.userid: " + data.userid);
		            $('div#loginResult').addClass("success");
		          } //else
		        } // success
		      }); // ajax
		    } // if
		    else {
		      $('div#loginResult').text("Faltan Datos!");
		      $('div#loginResult').addClass("Error");
		    } // else
		    $('div#loginResult').fadeIn();
		    return false;
		  });
		});