function getCount(str) {
    var vowelsCount = 0;
    
    for(i=0;i<str.length;i++){
        if( str[i]=='a' || str[i]=='e' || str[i]=='i'|| str[i]=='o' || str[i]=='u'){
            vowelsCount = vowelsCount+1;
        }
    }
    
    return vowelsCount;
}