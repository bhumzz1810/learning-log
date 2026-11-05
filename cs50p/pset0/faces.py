# define the main function
def main():
    # prompt user for input
    user_input = input("Enter input: ")
    # call convert on the input
    result = convert(user_input)
    # print the result
    print(result)

# implement a function called convert
def convert(str_input):
    ans = str_input.replace(":)","🙂").replace(":(","🙁")
    return ans

# call the main function
main()
