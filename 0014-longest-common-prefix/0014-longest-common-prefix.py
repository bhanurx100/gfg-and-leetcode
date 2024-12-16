class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            while not s.startswith(prefix):  # Check if the string starts with the current     prefix
                prefix = prefix[:-1]  # Reduce the prefix by removing the last character
                if prefix == "":  # If prefix becomes empty, return ""
                    return ""

        return prefix
