def solution(number):
    output = 0
    for previous_number in range(number):
        print(previous_number)
        if(
            previous_number % 3 == 0
            or previous_number % 5 == 0
          ):
            output += previous_number
        
    return output    