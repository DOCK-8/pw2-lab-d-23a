
function Ingreso(caracter){
	        document.getElementById("pantalla").innerHTML+=caracter;
}
function Borrar(){
	        var a =document.getElementById("pantalla").innerHTML;
	        var b=a.substring(a.length-1,0);
	        document.getElementById("pantalla").innerHTML=b;
}
function igual(){
	        document.getElementById("memoria").innerHTML +=(document.getElementById("pantalla").innerHTML+"=");
	        var resultado=eval(document.getElementById("pantalla").innerHTML);
	          document.getElementById("pantalla").innerHTML=resultado;
	          document.getElementById("memoria").innerHTML +=(document.getElementById("pantalla").innerHTML+"\n");
}
