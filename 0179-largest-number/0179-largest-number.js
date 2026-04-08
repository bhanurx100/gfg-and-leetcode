/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    const arr = nums.map(String);
    arr.sort((a,b)=>{
        const ab=a+b;
        const ba= b+a;
        if (ab>ba) return -1;
        if (ba>ab) return 1;
        return 0;

    });
    if (arr[0]==="0") return "0";
    return arr.join("");
};