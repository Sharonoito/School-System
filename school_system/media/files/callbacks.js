// console.log("plant kunde");
// console.log("water kunde");
// console.log("Add kunde");

console.log("plant kunde");
 setTimeout(function(){
    console.log("water kunde");
 },3000)
 console.log("add fertilizer");

 function greeting(name){
     console.log(`Hello${name}, welcome to JS class`);


 }
let promise=new promidse(function(resolve,reject){
    setTimeout(()=>resolve("done",1000)})

