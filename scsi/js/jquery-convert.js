/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
(function($){
    //Declaracion de numeros
    var numVal = new Array(48,49,50,51,52,53,54,55,56,57);
    //Caracteres literales aceptados
    var letVal = new Array(65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90);
    //carateres especiales aceptados
    var carVal = new Array(8,13,33,34,37,38,39,40,46);
    //44 corresponde al ,
    var cmmVal = 44;
    //45 corresponde al -
    var gioVal = 45;
    //46 corresponde al .
    var pntVal = 46;
    //32 corresponde espacio
    var espVal = 32;
    var i;
    $.fn.convertUpper = function(op,alength) {  
        //var name = $(this).attr("name");
        var expReg;
        var permitir = true;
        var arafVal;
        switch(op){
            case 0: //solo numeros
                expReg = /[^0-9]/g;
                arafVal = numVal; 
                break;
            case 1: //numeros con descimales 
                expReg = /[^0-9.]/g;
                numVal.push(pntVal);
                arafVal = numVal; 
                break;
            case 2: //numeros y espaciado
                expReg = /[^0-9 ]/g;
                numVal.push(espVal);
                arafVal = numVal; 
                break;
            case 3: //letras
                expReg = /[^a-zA-Z]/g;
                arafVal = letVal; 
                break;
            case 4: //letras con espaciado
                expReg = /[^a-zA-Z ]/g;
                letVal.push(espVal);
                arafVal = letVal; 
                break;
            case 5: 
                expReg = /[^a-zA-Z0-9]/g;
                arafVal = numVal.concat(letVal); 
                break;
            case 6: 
                expReg = /[^a-zA-Z0-9 ]/g;
                letVal.push(espVal);
                arafVal = numVal.concat(letVal); 
                break;
            case 7: 
                expReg = /[^a-zA-Z0-9-]/g;
                letVal.push(gioVal);
                arafVal = numVal.concat(letVal); 
                break;
            default: 
                expReg = /[^a-zA-Z0-9,. ]+/g;
                letVal.push(espVal);
                letVal.push(cmmVal);
                letVal.push(pntVal);
                arafVal = numVal.concat(letVal);
                break;
        }
        this.each(function () {
            var $this = $(this);
            if ($this.is('input:text')) {                
                permitir = true;
                $this.bind("cut copy",function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                });
                $this.keyup(function(e) {
                    //e.preventDefault();
                    //e.stopPropagation();
                    if(permitir){
                        $this.val( $this.val().replace(expReg, function(str) {                             
                            mostrarError($this,"Caracter no permitido borrado.");
                            return '';
                        }));
                    }else
                        permitir = true;
                    if(op == 1)
                        formatoDecimal($this,0);
                    
                });
                $this.keypress(function(e) {                    
                    var pressedKey = e.keyCode?e.keyCode:e.which;
                    for (i = 0; i < carVal.length; i++){
                        if(carVal[i]==e.keyCode){
                            permitir = false;
                            return true;
                        }
                    }
                    
                    for (i = 0; i < arafVal.length; i++) {
                        if(arafVal[i]==pressedKey||arafVal[i]==(pressedKey-espVal)){
                            var str = String.fromCharCode(pressedKey);
                            var startpos = this.selectionStart;
                            var endpos = this.selectionEnd;
                            var valor = this.value.substr(0, startpos) + this.value.substr(endpos);
                            var position;
                            if((valor+str).length > alength){
                                mostrarError($this,"Este campo solo permite "+alength+" caracteres");
                                position = startpos;
                                this.value = valor;
                            }else{
                                this.value = this.value.substr(0, startpos) + str.toUpperCase() + this.value.substr(endpos);
                                position = startpos + 1;
                            }
                            this.setSelectionRange(position, position);                            
                            permitir = false;
                            e.preventDefault();
                            e.stopPropagation();
                            return;
                        }
                    }
                    mostrarError($this,"Caracter No Permitido.");                    
                    e.preventDefault();
                    e.stopPropagation();
                    return;
                });
                $this.focusout(function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    if(op == 1)
                        formatoDecimal($this,1);
                    return;
                });
            }
            return;
        });
        function mostrarError(thiss,valor){
            thiss.after("<div id='error"+thiss.attr('name')+"'><span style='color: red;'>"+valor+"</span></div>");
            $("#error"+thiss.attr('name')).fadeOut(2000); 
        }
        function caracteresPermitidos(thiss){
            var longitud = thiss.val().length;
            var resto = alength - longitud;
            if(resto < 0){
                thiss.val(thiss.val().substring(0, alength));
                mostrarError(thiss,"Este campo solo permite "+alength+" caracteres");
                return true;
            }
            return false;
        }
        function formatoDecimal(thiss,operacion){
            if(operacion==1){
                if(thiss.val()==''){
                    return;
                }
                if(thiss.val()==0){
                    //mostrarError(thiss,"No valido");
                    thiss.val("0");
                    return;
                }              
            }
            var nValor = "";
            var campos = thiss.val().split(".");
            if(campos.length>=2){
                if(campos[0].length==0){
                    mostrarError(thiss,"Ejemplo(1254.14)");
                    thiss.val("");
                    return;
                }
                nValor = campos[0];
                if(campos[1].length>0){
                    nValor = campos[0]+"."+campos[1];
                }
                if(campos.length>2){
                    mostrarError(thiss,"Solo un \".\" separador");
                    thiss.val(nValor);
                    return;
                }
                if(operacion==1){
                    if(campos[1].length == 0){
                        nValor = campos[0]+".00";
                        thiss.val(nValor);
                    }
                }
            }else{
                if(operacion==1){
                    if(campos[0] > 0){
                        nValor = campos[0]+".00";
                        thiss.val(nValor);
                    }
                }
            }
        }
    }
    return this;    
})(jQuery);