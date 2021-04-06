#!/usr/bin/node
function FirstReverse(str) { 

  // code goes here  
  let newarray="";
  for(let i = 1; i <= str.length;i++)
  {
    newarray += str[str.length-i]
  }
  return newarray; 
}
   
// keep this function call here 
console.log(FirstReverse(readline()));
