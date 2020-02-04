import numpy as np
if __name__ == '__main__':
    digits = []
    for i in range(12):
        digits.append(np.random.randint(0,9))
   
    result = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    np_digits = np.array(digits)
    
    turns = 5
    while turns > 0:
        guess_num = int(input())
        if (guess_num in np_digits):
            revealed_digits = np.where(np_digits == guess_num)
            revealed_digits = revealed_digits[0]
            for numbers in revealed_digits:
                result[numbers] = guess_num
        print(result)    
        turns -= 1
    np_result = np.array(result)
    unguessed = np.where(np_result == '_')
    unguessed = unguessed[0]
   
    points = 12 - len(unguessed)
    print(points)

            