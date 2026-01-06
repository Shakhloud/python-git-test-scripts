from services.numsService import mathService


def calc():
    input_num1 = int(input("Введите первое число: "))
    input_num2 = int(input("Введите второе число: "))
    operation = input("Введите требуемую операцию (+, -, *, /): ")

    result = None

    if operation == "+":
        result = mathService.plus_of_nums(input_num1, input_num2)
    elif operation == "-":
        result = mathService.min_of_nums(input_num1, input_num2)
    elif operation == "*":
        result = mathService.mult_of_nums(input_num1, input_num2)
    elif operation == "/":
        result = mathService.div_of_nums(input_num1, input_num2)

    print("Результат: ", result, end="\n")


if __name__ == "__main__":
    calc()
