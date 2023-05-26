const fs= require('fs')
const express= require('express')
const path=require('path')
const app=express()
const ubi=__dirname;

app.get('/',(req,res)=>{
	let html='<!DOCTYPE html><html><head></head><body><h1>Agenda</h1><a href="/ver">ver lista de proyectos</a></br><a href="/agregar"> Agregar</a></body></html>';
	res.send(html)
})
app.get('/ver',(req,res)=>{
	var content=fs.ri0
})
app.listen(3000,()=>{
console.log('Escucchando al Servidor')
})
