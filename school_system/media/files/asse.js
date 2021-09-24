function range(){ 
    var range=(1,100)
    for(num in range){
        if (num%3==0){ 
        console.log("Fizz")
        }
        else if(num%5==0){ 
        console.log("Buzz")
        }
        else if(num%3==0 && num%5==0){
            console.log("FizzBuzz")
        }
    }}
    range()

 var num=[10,3,50,32,7]
 for(var n of num) {
     if(n<=50){
         console.log("largest number")
     }}

    var grade=100 
     if(grade <=100){
         console.log("A")
         }
       else if (grade <=90){
           console.log("B")
       }
    else if(grade<=80){ 
    console.log("C")
         }
     else if(grade<=70) {
         console.log("D")
     }  
     else if(grade<=60){
         console.log("F")

     } 


     var range=(0,100)
     for (var no of range){
         for (let i = 0; i < range.length; i++) {
             console.log = range[i];  
         }
         if(no%2==0)
         console.log(`${no} is even `)
         else{
             console.log(`${no} is odd`)
         }
     }
     
     
 