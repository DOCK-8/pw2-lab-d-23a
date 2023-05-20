var R;
var i=-1;
function Ingreso(caracter){
	        document.getElementById("pantalla").innerHTML+=caracter;
}
function Borrar(){
	        var a =document.getElementById("pantalla").innerHTML;
	        var b=a.substring(a.length-1,0);
	        document.getElementById("pantalla").innerHTML=b;
}
function igual(){
  i++;
	        document.getElementById("memoria").innerHTML =(document.getElementById("pantalla").innerHTML+"=");
	        var resultado=eval(document.getElementById("pantalla").innerHTML);
  document.getElementById("pantalla").innerHTML=resultado;
  if(i%2==0){
  R=resultado;
  }
}
function memory(){
  document.getElementById("pantalla").innerHTML+=R;
}
