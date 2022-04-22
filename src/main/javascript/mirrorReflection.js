import assert from 'assert/strict';

/**
 * @param {number} p
 * @param {number} q
 * @return {number}
 */
var mirrorReflection = function(p, q) {
    let answer = -1
    let directionUp = true
    let directionRight = true
    let pos = 0
    while(answer === -1) {
        directionRight = !directionRight;
        if (directionUp) {
            pos = pos + q;
        } else {
            pos = pos - q;
        }
        pos = pos % (2*p)
        if (pos < 0) {
            pos = pos + 2 * p;
        }
        if (pos >= p) {
            directionUp = !directionUp;
            pos = p - (pos - p)
        } else if (pos === 0) {
            directionUp = true
        }

        if (pos % p === 0 && !directionUp) {
            return directionRight ? 2 : 1
        } else if (pos % p === 0 && directionUp && !directionRight) {
            return 0;
        }
    }
};
assert.equal(2, mirrorReflection(4,3))
assert.equal(0, mirrorReflection(3,2))

assert.equal(2, mirrorReflection(2,1))

assert.equal(2, mirrorReflection(4,2))
assert.equal(1, mirrorReflection(3,1))
