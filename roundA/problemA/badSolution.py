data = [42,11,1,2018]

def stripInput(filename):

    data = []

    with open(filename, 'r') as f:
        for line in f:
            data.append(int(line))

    del data[0]
    return data

def allEven(n):
    digits = []

    while n != 0:
        digits.append(n%10)
        n //= 10

    return all(map(lambda x: x%2 ==0, digits))


def calculateUgly(data):
    output = []
    for number in data:

        if not(allEven(number)):
            up = number
            down = number

            while not allEven(up):
                up += 1

            while not allEven(down):
                down -= 1

            output.append(min(up-number, number-down))
        else:
            output.append(0)    

    return output


    
result = calculateUgly(stripInput("A-small-practice.in"))

with open("result.out", 'w') as f:
    for pos, n in enumerate(result):
        f.write("Case #{}: {}\n".format(pos+1, n))
    
    

