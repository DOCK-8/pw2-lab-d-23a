let imgzoom,Img,Img_D,Img_N,Img_P
window.onload = function() {
    imgzoom=document.getElementById("zoom"),
    Img=document.getElementById("zImagen");
    Img_D = document.getElementById("descripcion")
    Img_N = document.getElementById("nombre")
    Img_P = document.getElementById("precio")
}
function cerrar(){
    imgzoom.style.display = "none";
}
function Open(ubi,nombre,des,precio){
    Img.src = ubi
    Img_N.textContent = nombre
    Img_D.textContent = des
    Img_P.textContent = 'S/.' + precio
    imgzoom.style.display="flex";
}
