let imgzoom,Img
window.onload = function() {
    imgzoom=document.getElementById("zoom"),
    Img=document.getElementById("zImagen");
}
function cerrar(){
    imgzoom.style.display = "none";
}
function Open(archivo){
    Img.src=archivo
    imgzoom.style.display="flex";
}
