const fs= require('fs')
const express= require('express')
const app= express()
	var cont=fs.readdirSync("./eventos")
	console.log(cont)
app.get('/lista',(req,res)=>{
	cont.forEach(contenido=>console.log(contenido));
})
app.listen (3000,()=>{
console.log('Escuchando a Maria')
}
)
