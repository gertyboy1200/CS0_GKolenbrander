user_input = input()
def solution(input):

    if 'ss' in input:
        print("hiss")
        return("hiss")
    else:
        print("no hiss")
        return("no hiss")


solution(user_input)

assert(solution("hiss") == "hiss")

assert(solution('ss') == 'hiss')

assert(solution('sos') == 'no hiss')