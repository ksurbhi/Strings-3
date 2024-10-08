class Solution:
    """
    Time Complexity: The time complexity can be considered O(1), or constant time, as the number
    of operations does not grow with the size of the input. 
    Space Complexity: O(1)
    """
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"
        
        # Arrays to hold the words for numbers less than twenty, tens, and powers of a thousand
        less_than_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
                            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                            "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        # Helper function to convert a number less than 1000 into words
        def helper(n: int) -> str:
            if n == 0:
                return ""  # Base case: return empty string for zero
            elif n < 20:
                # If the number is less than 20, directly map it to its word representation
                return less_than_twenty[n] + " "
            elif n < 100:
                # If the number is less than 100, convert the tens place and recursively convert the remainder
                return tens[n // 10] + " " + helper(n % 10)
            else:
                # If the number is 100 or greater, convert the hundreds place and the remainder recursively
                return less_than_twenty[n // 100] + " Hundred " + helper(n % 100)
        
        res = ""  # Initialize the result string
        
        # Process each group of three digits (thousands, millions, billions)
        for i, word in enumerate(thousands):
            if num % 1000 != 0:
                # If the current group is not zero, convert it to words and add the appropriate power of a thousand
                res = helper(num % 1000) + word + " " + res
            num //= 1000  # Move to the next group of three digits
        
        # Return the final result string with leading/trailing spaces removed
        return res.strip()

        

        
