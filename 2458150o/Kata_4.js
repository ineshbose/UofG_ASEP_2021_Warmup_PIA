function elevatorDistance(array) {
  
  let total = 0;
  
  for (let i = 0; i < array.length - 1; i++){
    total += Math.abs(array[i] - array[i + 1]);
    console.log(total)
  }
  
  return total;
}