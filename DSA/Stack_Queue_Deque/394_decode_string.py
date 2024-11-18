class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            ## Keep adding to Stack until a ']'
            if char != "]":
                stack.append(char)

                print(f"if {stack}")
                
            else: 
                ## Extracting SubString to be Multiplied
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str

                    print(f"while1 {stack}, curr {curr_str}")
                ## Pop to remove '['
                stack.pop()

                ## Extract full number (handles multi-digit, e.g. 10)
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                    print(f"while2 {stack} curr {curr_num}")
                
                ## Updating Stack with multiplied string
                curr_str = int(curr_num) * curr_str
                stack.append(curr_str)
            print(f"for stack: {stack}")

        return "".join(stack)