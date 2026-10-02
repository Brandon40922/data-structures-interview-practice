# Timed Challenge - Problem 13: Balanced Symbols
#
# Check if the brackets in a string are balanced.
#
# Input: "{[()]}"
# Output: True
#
# Input: "{[(])}"
# Output: False 

def is_balanced(symbols):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for symbol in symbols:
        if symbol in "([{":
            stack.append(symbol)

        elif symbol in ")]}":
            if len(stack) == 0:
                return False

            top = stack.pop()

            if top != pairs[symbol]:
                return False

    return len(stack) == 0 

# Test cases
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
print(is_balanced("()"))
print(is_balanced(""))
print(is_balanced("((("))
print(is_balanced("hello")) 

# Reflection
#
# For this timed challenge, I chose to use a stack to solve the Balanced
# Symbols problem. I chose a stack because it follows the Last-In, First-Out
# (LIFO) principle. When an opening bracket is found, it is added to the
# stack. When a closing bracket is found, the program removes the most recent
# opening bracket and checks whether the two symbols match. This made a stack
# a good choice because brackets that open most recently need to be closed
# first. The solution only needs to go through the input once, so the time
# complexity is O(n), where n is the number of characters in the input.
#
# The 30-minute time limit influenced me to choose a solution that was simple
# to understand and implement. Instead of trying multiple approaches, I
# focused on the stack because the LIFO behavior directly matched the
# requirements of the problem. I also used a dictionary to connect each
# closing bracket with its matching opening bracket. This helped keep the
# comparisons organized and made the code easier to read.
#
# One trade-off with this solution is that the stack can require O(n)
# additional space in a case where the input contains many opening brackets.
# Under the time limit, I prioritized creating a correct and readable solution
# instead of trying to reduce the extra memory. I also spent part of the time
# testing edge cases, including an empty string, unmatched brackets, and a
# string without brackets. Overall, the challenge showed me how choosing the
# right data structure can make a problem easier to solve efficiently.