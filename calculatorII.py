class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def calculate(self, s: str) -> int:
        calc = 0  # This will hold the cumulative result
        num = 0  # This will hold the current number being processed
        prev_operator = '+'  # The last operator seen, starting with '+'
        tail = 0  # This is used for correctly handling '*' and '/' operations
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit():  # If the character is a digit, build the number
                num = num * 10 + int(char)
            
            # Process the operation if we hit a non-digit, non-space, or the end of the string
            if not char.isdigit() and char != ' ' or i == len(s) - 1:
                if prev_operator == "+":
                    calc += num
                    tail = num
                elif prev_operator == "-":
                    calc -= num
                    tail = -num
                elif prev_operator == "*":
                    calc = calc - tail + tail * num
                    tail = tail * num
                elif prev_operator == "/":
                    calc = calc - tail + int(tail / num)
                    tail = int(tail / num)
                
                prev_operator = char  # Update the operator for the next loop
                num = 0  # Reset the number for the next digit sequence
        
        return calc

       


################### Using Stack #####################
class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    def calculate(self, s: str) -> int:
        stack = []
        num= 0

        
        prev_operator = '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() and char !=' ' or i == len(s)-1:
                if prev_operator =='+':
                    stack.append(+num)
                elif prev_operator =='-':
                    stack.append(-num)
                elif prev_operator =='*':
                    stack.append(stack.pop() * num)
                elif prev_operator =='/':
                    stack.append(int(stack.pop()/num))
                num =0
                prev_operator = char
        return sum(stack)
