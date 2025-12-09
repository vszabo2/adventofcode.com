asdf = [line.split() for line in open("input")]
num_problems = len(asdf[0])
operator_index = len(asdf) - 1
result = 0
for i in range(num_problems):
    problem_operator = asdf[operator_index][i]
    if problem_operator == "*":
        prod = 1
        for j in range(operator_index):
            prod *= int(asdf[j][i])
        result += prod
    elif problem_operator == "+":
        result += sum(int(asdf[j][i]) for j in range(operator_index))
    else:
        raise AssertionError(f"Operator {problem_operator}?")
print(result)
