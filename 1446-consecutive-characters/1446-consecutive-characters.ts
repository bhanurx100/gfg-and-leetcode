function maxPower(s: string): number {
    let curr=1;
    let max=0;
    for(let i=1;i<s.length;i+=1){
        if(s[i-1]===s[i]){
            curr+=1;
        }
        else{
            max=Math.max(max,curr);
            curr=1;
        }
    }
    return Math.max(max,curr);
};