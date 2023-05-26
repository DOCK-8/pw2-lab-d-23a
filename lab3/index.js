const express=require('express')
const app= express()
const path=require('path')
 
app.get('/',(req,res)=>{
res.sendFile(path.resolve(__dirname, 'index.html'))
})

app.listen(3000,()=>{
console.log("Escuchando en: http://localhost:3000")
})

app.use(express.static(__dirname))

