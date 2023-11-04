class myAddition():
    def __init__(self):
        pass
    
    
    def add_two_numbers(self, num_1, num_2):
        try:
            numb_1 = float(num_1)
            numb_2 = float(num_2)
            result_add = numb_1 + numb_2
            return result_add
        except:
            return 'Data types not correct'
    
    
# Main code
add_result = myAddition()
number_1 = input('Enter the first number: ')
number_2 = input('Enter the second number: ')

result = add_result.add_two_numbers(number_1, number_2)
print(f'The result is: {result}')
    