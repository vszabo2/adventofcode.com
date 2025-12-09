asdf = open("input").readlines()
operator_index = len(asdf) - 1
result = 0
start_problem = True
for i in range(len(asdf[0])):
    if start_problem:
        problem_operator = asdf[operator_index][i]
        operand = int("".join(asdf[j][i] for j in range(operator_index)))
        print(operand)
        problem_intermediate = operand
        start_problem = False
    else:
        try:
            operand = int("".join(asdf[j][i] for j in range(operator_index)))
            print(operand)
            if problem_operator == "*":
                problem_intermediate *= operand
            else:
                assert problem_operator == "+", f"Operator {problem_operator}?"
                problem_intermediate += operand
            assert asdf[operator_index][i] == " ", f"Multiple operators {asdf[operator_index][i]}?"
        except ValueError:
            print(problem_intermediate)
            result += problem_intermediate
            start_problem = True
    # result += problem_intermediate

print(result)
