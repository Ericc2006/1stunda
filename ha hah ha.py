import random

def generate_number(max_number):
    """Ģenerē nejaušu skaitli no 1 līdz max_number."""
    return random.randint(1, max_number)

def generate_operator():
    """Ģenerē nejaušu matemātisko operatoru (+, -, *, /)."""
    operators = ['+', '-', '*', '/']
    return random.choice(operators)

def generate_expression(max_number):
    """Ģenerē nejaušu matemātisku izteiksmi ar skaitļiem un operatoriem."""
    num1 = generate_number(max_number)
    num2 = generate_number(max_number)
    operator = generate_operator()
    expression = f"{num1} {operator} {num2}"
    return expression

def evaluate_expression(expression):
    """Novērtē dotās matemātiskās izteiksmes rezultātu."""
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        # Aizsargājamies pret dalīšanu ar 0
        return None
    except:
        # Ja izteiksme ir nepareiza, atgriežam None
        return None

def main():
    max_number = int(input("Ievadies lielāka skaitļa vērtību: ")) # Lietotājam jāievada, kādā apjomā piedāvāt skaitļus
    correct_answers = 0
    total_answers = 0

    while True:
        expression = generate_expression(max_number)
        print("Uzdevums:", expression)
        user_answer = input("Ievadi atbildi (vai 'q' lai beigtu): ")

        if user_answer == 'q':
            break

        total_answers += 1
        correct_result = evaluate_expression(expression)
        if correct_result is not None and int(user_answer) == correct_result:
            print("PAREIZI")
            correct_answers += 1
        else:
            print("NEPAREIZI")

        with open("atbildes.txt", "a", encoding = "utf8") as file:
            file.write(f"Uzdevums: {expression}, Ievadītā atbilde: {user_answer}, Pareizā atbilde: {correct_result}\n")

    print("Pareizo atbilžu skaits:", correct_answers)
    print("Iegūtais vērtējums %:", (correct_answers / total_answers) * 100)

if __name__ == '__main__':
    main()
