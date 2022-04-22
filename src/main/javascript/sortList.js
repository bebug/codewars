import assert from 'assert/strict';

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    return mergeSort(head)
};

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var mergeSort = function(head) {
    if (!head || !head.next) {
        return head;
    }
    let middle = split(head);

    let sortedL = mergeSort(head);
    let sortedR = mergeSort(middle);
    let result = null;
    let current = null

    while (sortedL || sortedR) {
        let next = null
        if (!sortedL) {
            next = sortedR;
            sortedR = sortedR.next;
        }
        else if (!sortedR) {
            next = sortedL;
            sortedL = sortedL.next;
        }
        else if (sortedL && sortedR) {
            if (sortedL.val > sortedR.val) {
                next = sortedR;
                sortedR = sortedR.next;
            } else {
                next = sortedL;
                sortedL = sortedL.next;
            }
        }

        if (current) {
            current.next = next;
        }
        current = next;
        current.next = null;
        if (!result) {
            result = current;
        }
    }

    return result;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var split = function(head) {
    console.log(`splitting ${JSON.stringify(head)}`)
    let length = 0;
    let current = head;
    while (current) {
        current = current.next
        length++;
    }
    length = length/2;
    current = head;
    while (length > 1) {
        current = current.next
        length--;
    }
    let next = current.next
    current.next = null;
    console.log(`first ${JSON.stringify(head)}`)
    console.log(`second ${JSON.stringify(next)}`)

    return next;

}

/**
 * @param {ListNode} head
 * @return {Array}
 */
var toArray = function(head) {
    let current = head;
    let myArray = []
    while (current) {
        myArray.push(current.val);
        current = current.next;
    }
    return myArray;
}

/**
 * @param {Array} array
 * @return {ListNode}
 */
var toNodes = function(array) {
    let current = null
    for (let i = 0; i < array.length; i++) {
        current = new ListNode(array[array.length - 1 - i], current);
    }
    return current;
}

assert.deepEqual([1,2,3,4], toArray(sortList(toNodes([4,2,1,3]))))
assert.deepEqual([-1,0,3,4,5], toArray(sortList(toNodes([-1,5,3,4,0]))))
assert.deepEqual([1,2,3], toArray(toNodes([1,2,3])))

let k = function(mul) {

    return (number) => {
        return number * mul;
    }
}

console.log(k(10)(4))

