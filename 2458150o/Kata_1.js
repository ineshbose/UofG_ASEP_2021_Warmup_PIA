function getCount(str) {
  var vowelsCount = 0;
  
  //loop through string 
  for (let i = 0; i < str.length; i++) { 
    //if letter in list of vowels then increment vowelsCount
    if (["a", "e", "o", "u", "i"].includes(str[i])){
      vowelsCount += 1;
    }
  }
  
  return vowelsCount;
}