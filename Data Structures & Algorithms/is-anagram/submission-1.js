class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sMap = new Map();

        // iterate through string s and
        // add it to a hashmap with the character and frequency
        for (const char of s) {
            if (sMap.get(char)) {
                sMap.set(char, sMap.get(char) + 1);
            } else {
                sMap.set(char, 1);
            }
        }

        // iterate through string t and compare with hashmap
        // if char doesnt exist in map, return false
        // if char does exist, decrease frequency
        // if value is 0, delete key
        // if map is empty, return true
        // else return false

        for (const char of t) {
            sMap.set(char, sMap.get(char) - 1);

            if (sMap.get(char) === 0) {
                sMap.delete(char);
            }
        }

        // empty map check
        if (sMap.size == 0) {
            return true;
        }

        console.log(sMap);
        return false;
    }
}
