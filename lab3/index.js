const express=require('express')
const app= express()
const path=require('path')
const fs=require('fs')
function conteo(caracter){
let nombre='./'+caracter;
fs.readdir(nombre,(error,elementos)=>{
	if(error){
		throw error
}
console.log(elementos)
})
}
app.get('/',(req,res)=>{
res.sendFile(path.resolve(__dirname, 'index.html'))
})

app.listen(3000,()=>{
console.log("Escuchando en: http://localhost:3000")
})

app.use(express.static(__dirname))
function prueba(){
let a =document.getElementById('agenda')
	app.sendFile((req,res)=>{
	res.sendFile(path.resolve(__dirname, 'index.html'))
	})
}
