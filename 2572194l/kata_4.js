function elevatorDistance(array) {
  var sum = 0
  for(let i = array.length-1; i > 0; i--){
      sum += Math.abs(array[i] - array[i-1])
    }
  return sum
}