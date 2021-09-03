/**
 * @param {number} n
 * @return {number[]}
 */
 var grayCode = function(n) {
    const r = [];
    for(let i = 0; i < Math.pow(2, n); i++) {
        r.push(i ^ i >> 1)
    }
    return r
};