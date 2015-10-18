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
    var carVal = new Array(8,9,13,33,35,37,38,39,40);
    //44 corresponde al ,
    var cmmVal = 44;
    //45 corresponde al -
    var gioVal = 45;
    //46 corresponde al .
    var pntVal = 46;
    //32 corresponde espacio
    var espVal = 32;
    //34 corresponde "
    var cmlVal = 34;
    //10 salto de linea
    var sltVal = 10;
    //47 barra / para fecha
    var braVal = 47;    
    var i;
    $.fn.convertUpperTextArea = function() { 
        this.convertUpper(10,0);
    }
    $.fn.convertUpper = function(op,alength) {
        var permitir = true;
        var arrayFormatoValor;
        var arrayFormatoAdcnl = numVal.slice(0, numVal.length);
        switch(op){
            case 0: //solo numeros
                arrayFormatoValor = arrayFormatoAdcnl;
                break;
            case 1: //numeros con descimales                
                arrayFormatoAdcnl.push(pntVal);
                arrayFormatoValor = arrayFormatoAdcnl;
                break;
            case 2: //numeros y espaciado
                arrayFormatoAdcnl.push(espVal);
                arrayFormatoValor = arrayFormatoAdcnl; 
                break;
            case 3: //letras
                arrayFormatoValor = letVal.slice(0, letVal.length); 
                break;
            case 4: //letras con espaciado
                arrayFormatoAdcnl = letVal.slice(0, letVal.length); 
                arrayFormatoAdcnl.push(espVal);
                arrayFormatoValor = arrayFormatoAdcnl; 
                break;
            case 5: //letras y numeros
                arrayFormatoValor = arrayFormatoAdcnl.concat(letVal); 
                break;
            case 6: //letras numero y espaciado
                arrayFormatoAdcnl = arrayFormatoAdcnl.concat(letVal);
                arrayFormatoAdcnl.push(espVal);
                arrayFormatoValor = arrayFormatoAdcnl; 
                break;
            case 7: 
                arrayFormatoAdcnl = arrayFormatoAdcnl.concat(letVal);
                arrayFormatoAdcnl.push(gioVal);
                arrayFormatoValor = arrayFormatoAdcnl; 
                break;                
            case 8:
                arrayFormatoAdcnl = arrayFormatoAdcnl.concat(letVal); 
                arrayFormatoAdcnl.push(espVal);
                arrayFormatoAdcnl.push(gioVal);
                arrayFormatoAdcnl.push(cmlVal);
                arrayFormatoValor = arrayFormatoAdcnl;
                break;
            case 10:
                arrayFormatoAdcnl = arrayFormatoAdcnl.concat(letVal);
                arrayFormatoAdcnl.push(gioVal);
                arrayFormatoAdcnl.push(espVal);
                arrayFormatoAdcnl.push(cmmVal);
                arrayFormatoAdcnl.push(sltVal);
                arrayFormatoAdcnl.push(pntVal);
                arrayFormatoAdcnl.push(braVal);
                arrayFormatoAdcnl.push(cmlVal);
                arrayFormatoValor = arrayFormatoAdcnl; 
                break;
            default: 
                arrayFormatoAdcnl = arrayFormatoAdcnl.concat(letVal);
                arrayFormatoAdcnl.push(espVal);
                arrayFormatoAdcnl.push(cmmVal);
                arrayFormatoAdcnl.push(pntVal);
                arrayFormatoValor = arrayFormatoAdcnl;
                break;
        }        
        this.each(function () {            
            var $this = $(this);
            if ($this.is('input:text')) {                
                permitir = true;
                $this.keyup(function(e) {
                    keyPresionadoUP($this);
                    if(op == 1)
                        formatoDecimal($this,0);
                    
                });
                $this.keypress(function(e) {
                    keyPresionado(e, $this, this, true);
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
            if ($this.is('textarea')) {
                $this.keypress(function(e) {
                    keyPresionado(e, $this, this, false);
                });
                $this.keyup(function(e) {
                    this.style.height = "1px";
                    this.style.height = this.scrollHeight+"px";
                    keyPresionadoUP($this);                    
                });
            }
            return;
        });
        function keyPresionadoUP(jlthis){
            var text1 = jlthis.val().toUpperCase();
            var textt = "";
            if(permitir){ 
                for (var i = 0; i < text1.length; i++) {
                    if(normalizarText(text1.charCodeAt(i),jlthis)){
                        textt += ''+text1.charAt(i);
                    }
                }
                jlthis.val(textt);
            }else{
                permitir = true;
            }            
        }
        function normalizarText(chart,jlthis) {
            for(var i = 0; i < arrayFormatoValor.length; i++ ){
                if(chart==arrayFormatoValor[i])
                    return true;
            }
            mostrarError(jlthis,"Caracter "+String.fromCharCode(chart)+" borrado");
            return false;
        }
        function keyPresionado(event, jlthis, thiss, controlLengt){
            var pressedKey = event.keyCode;
            //alert(event.keyCode+" - "+event.which+" = "+getBrowser());
            if(getBrowser()=='Firefox' || getBrowser()=='Opera'){
                pressedKey = event.which;                               
            }
            if(pressedKey=='0'){
                permitir = false;
                return;
            } 
            var forbiddenKeys = new Array("c", "x", "v");            
            for (i = 0; i < carVal.length; i++){
                if(carVal[i]==event.keyCode){
                    permitir = false;
                    return;
                }
            }
            if (event.ctrlKey) {
                permitir = false;
                for (i = 0; i < forbiddenKeys.length; i++) {
                    if (forbiddenKeys[i] == String.fromCharCode(pressedKey).toLowerCase()) {
                        permitir = true;
                        break;
                    }
                } 
                return;
            }
            event.preventDefault();
            event.stopPropagation();            
            for (i = 0; i < arrayFormatoValor.length; i++) {
                if(arrayFormatoValor[i]==pressedKey||arrayFormatoValor[i]==(pressedKey-espVal)){
                    var varCharCode = String.fromCharCode(pressedKey);
                    var startpos = thiss.selectionStart;
                    var endpos = thiss.selectionEnd;
                    var valor = thiss.value.substr(0, startpos) + thiss.value.substr(endpos);
                    var varPosicion;
                    if((valor+varCharCode).length > alength && controlLengt){
                        mostrarError(jlthis,"Solo se permite "+alength+" caracter(es)");
                        varPosicion = startpos;
                        thiss.value = valor;
                    }else{                        
                        thiss.value = thiss.value.substr(0, startpos) + varCharCode.toUpperCase() + thiss.value.substr(endpos);
                        varPosicion = startpos + 1;
                    }                    
                    thiss.setSelectionRange(varPosicion, varPosicion);
                    permitir = false;                    
                    return;
                }
            }
            mostrarError(jlthis,"Caracter No Permitido.");
            return;
        }
        function mostrarError(thiss,valor){
            var nameComponent = 'mgeError-'+thiss.attr('name');
            thiss.after("<div id='"+nameComponent+"'>\n\
                            <span id='S"+nameComponent+"' style='color: red;'>"+valor+"\
                            </span>\n\
                        </div>");
            $("#"+nameComponent).fadeOut(2000,function(){
                $("#S"+nameComponent).remove();
                $("#"+nameComponent).remove();
            }); 
        }
        function caracteresPermitidos(thiss){
            var longitud = thiss.val().length;
            var resto = alength - longitud;
            if(resto < 0){
                thiss.val(thiss.val().substring(0, alength));
                mostrarError(thiss,"Este campo permite "+alength+" caracter(es)");
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
        function getBrowser(){
            var nAgt = navigator.userAgent;
            var browserName  = navigator.appName;
            if (nAgt.indexOf("Opera")!=-1) {
                browserName = "Opera";
            }
            else if (nAgt.indexOf("MSIE")!=-1) {
                browserName = "Internet Explorer";
            }
            else if (nAgt.indexOf("Chrome")!=-1) {
                browserName = "Chrome";
            }
            else if (nAgt.indexOf("Safari")!=-1) {
                browserName = "Safari";
            }
            else if (nAgt.indexOf("Firefox")!=-1) {
                browserName = "Firefox";
            }
            return browserName;
        }
    }
    return this;    
})(jQuery);