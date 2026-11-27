"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    
    status = "OK"
    result = 0
    error_code = ""
    valid = True

    if operation != "+" and operation != "-" and operation != "*" and operation != "/":
        error_code = "UNKNOWN_OPERATION"
        status = "ERROR"
        result = ""
        valid = False
    elif a_text == "" or b_text =="":
        error_code = "INVALID_NUMBER"
        status = "ERROR"
        result = ""
        valid = False

    if valid == True:
        if operation == "+":
            result = add(a_text, b_text)
        elif operation == "-":
            result = subtract(a_text, b_text)
        elif operation == "*":
            result = multiply(a_text, b_text)
        if operation == "/":
            if b_text == 0:
                error_code = "DIVISION_BY_ZERO"
                status = "ERROR"
                result = ""
            else:
                result = divide(a_text, b_text)

    return (status, result, error_code)

    """Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """
    raise NotImplementedError("Complete process_calculation for the coursework")

def main():
	while True:
		a = float(input("First number: "))
		op = input("Operator (+ - * /): ")
		b = float(input("Second number: "))
		print(process_calculation(op, a, b))

if __name__ == "__main__":
	main()
