function getCount(str) {
    var vowelsCount = 0;
    
    // enter your majic here

    let vowels = "aeiou";
    var count = 0;

    for (let ch of string) {
        for (let v of vowels) {
            if (ch == v) {
                vowelsCount ++;
            }
        }
    }
    return vowelsCount;
  }

