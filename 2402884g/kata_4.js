function getAbs(difference){
    if(difference<0){
      return -difference;
    }
    return difference;
}
  
function elevatorDistance(array) {
    var sum = 0;
    
    for(var i=0; i<(array.length-1); i++){
      sum = sum + getAbs(array[i]-array[i+1]);
      
    }
    return sum;
}