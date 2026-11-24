class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(string)
        j = len(string) - 1
        for i in range(len(s)):
            if i == j or i > j:
                break
            if string[i] != string[j]:
                return False
            j -= 1
        return True
