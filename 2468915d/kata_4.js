function elevatorDistance(array) {
    var distance = 0;
    var last_floor = array[0];

    for (let i=1; i<array.length; i++) {
        distance += Math.abs(last_floor - array[i]);
        last_floor = array[i]
    }
    return distance;
  }
