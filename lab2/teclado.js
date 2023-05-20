var lista = [0,1,2,3,4,5,6,7,8,9];
lista = lista.sort(function() {return Math.random() - 0.5});
 document.getElementById("uno").value=lista[0];
 document.getElementById("dos").value=lista[1];
 document.getElementById("tres").value=lista[2];
 document.getElementById("cuatro").value=lista[3];
 document.getElementById("cinco").value=lista[4];
 document.getElementById("seis").value=lista[5];
 document.getElementById("siete").value=lista[6];
 document.getElementById("ocho").value=lista[7];
 document.getElementById("nueve").value=lista[8];
 document.getElementById("cero").value=lista[9];
function Ingreso(caracter){
document.getElementById("contra").value+=document.getElementById(caracter).value;
}
function Limpiar(){
  document.getElementById("contra").value='';
}
