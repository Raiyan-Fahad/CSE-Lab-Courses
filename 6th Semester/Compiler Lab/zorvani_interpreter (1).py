import ast
import math
import operator

# ZORVANI: a small function-call interpreter.
# Enter one ZORVANI function call per line, for example: zavik(10, 20)

def require_int(n, name="value"):
    if isinstance(n, bool) or not isinstance(n, (int, float)) or not float(n).is_integer():
        raise ValueError(f"{name} must be an integer")
    return int(n)

def factorial(n):
    n = require_int(n)
    if n < 0:
        raise ValueError("factorial requires a non-negative integer")
    return math.factorial(n)

def gcd(a, b):
    return math.gcd(require_int(a), require_int(b))

def lcm(a, b):
    a, b = require_int(a), require_int(b)
    return math.lcm(a, b)

def is_prime(n):
    n = require_int(n)
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, math.isqrt(n) + 1))

def fibonacci(n):
    n = require_int(n)
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_digits(n):
    n = require_int(n)
    return sum(int(d) for d in str(abs(n)))

def reverse_number(n):
    n = require_int(n)
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

def percentage(part, whole):
    if whole == 0:
        raise ValueError("whole cannot be zero")
    return (part / whole) * 100

def hypotenuse(a, b):
    return math.hypot(a, b)

FUNCTIONS = {
    "zavik": (lambda a, b: a + b, 2, "Add two numbers"),
    "meroth": (lambda a, b: a - b, 2, "Subtract the second number from the first"),
    "qelvar": (lambda a, b: a * b, 2, "Multiply two numbers"),
    "druvex": (lambda a, b: a / b, 2, "Divide the first number by the second"),
    "nimbak": (lambda a, b: a % b, 2, "Remainder after division"),
    "orvatek": (lambda a, b: a ** b, 2, "Raise a number to a power"),
    "pelquin": (lambda a: a ** 2, 1, "Square a number"),
    "trazumo": (lambda a: a ** 3, 1, "Cube a number"),
    "velnira": (lambda a: math.sqrt(a), 1, "Square root"),
    "kordali": (lambda a: math.copysign(abs(a) ** (1 / 3), a), 1, "Cube root"),
    "xamiro": (lambda a: abs(a), 1, "Absolute value"),
    "bravon": (lambda a, b: max(a, b), 2, "Maximum of two numbers"),
    "seldrik": (lambda a, b: min(a, b), 2, "Minimum of two numbers"),
    "omelix": (lambda a, b: (a + b) / 2, 2, "Average of two numbers"),
    "fruneko": (factorial, 1, "Factorial"),
    "dagrimo": (gcd, 2, "Greatest common divisor"),
    "ulvador": (lcm, 2, "Least common multiple"),
    "prizent": (is_prime, 1, "Prime-number check"),
    "fibrelan": (fibonacci, 1, "Nth Fibonacci number; F(0) = 0"),
    "evnaro": (lambda a: require_int(a) % 2 == 0, 1, "Even-number check"),
    "odriva": (lambda a: require_int(a) % 2 != 0, 1, "Odd-number check"),
    "digisum": (sum_digits, 1, "Sum of digits"),
    "revomik": (reverse_number, 1, "Reverse an integer's digits"),
    "logvanta": (lambda a, b: math.log(a, b), 2, "Logarithm: log(value, base)"),
    "elnovar": (lambda a: math.log(a), 1, "Natural logarithm"),
    "sinquor": (lambda a: math.sin(math.radians(a)), 1, "Sine; angle in degrees"),
    "cosvani": (lambda a: math.cos(math.radians(a)), 1, "Cosine; angle in degrees"),
    "tantrix": (lambda a: math.tan(math.radians(a)), 1, "Tangent; angle in degrees"),
    "perzali": (percentage, 2, "Percentage: part out of whole"),
    "hypnaro": (hypotenuse, 2, "Hypotenuse from two perpendicular sides"),
}

class ZorvaniError(Exception):
    pass

def evaluate(source):
    try:
        tree = ast.parse(source.strip(), mode="eval")
    except SyntaxError as exc:
        raise ZorvaniError("Invalid syntax. Example: zavik(10, 20)") from exc

    node = tree.body
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
        raise ZorvaniError("Enter one function call, such as zavik(10, 20).")
    if node.func.id not in FUNCTIONS:
        raise ZorvaniError(f"Unknown ZORVANI function: {node.func.id}")

    function, expected_args, description = FUNCTIONS[node.func.id]
    if node.keywords:
        raise ZorvaniError("Use positional arguments only.")
    if len(node.args) != expected_args:
        raise ZorvaniError(
            f"{node.func.id} needs {expected_args} argument(s), but received {len(node.args)}."
        )

    values = []
    for arg in node.args:
        if not isinstance(arg, ast.Constant) or isinstance(arg.value, bool) or not isinstance(arg.value, (int, float)):
            raise ZorvaniError("Arguments must be numeric literals, e.g. zavik(10, 20).")
        values.append(arg.value)

    try:
        result = function(*values)
    except ZeroDivisionError:
        raise ZorvaniError("Cannot divide by zero.")
    except ValueError as exc:
        raise ZorvaniError(str(exc))
    except OverflowError:
        raise ZorvaniError("The result is too large to calculate.")

    return result, description

def main():
    print("=" * 48)
    print("              ZORVANI INTERPRETER")
    print("          Type help to see examples")
    print("          Type exit to close the program")
    print("=" * 48)

    while True:
        try:
            line = input("ZORVANI >>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not line:
            continue
        if line.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        if line.lower() == "help":
            print("Examples:")
            print("  zavik(10, 20)       -> 30")
            print("  meroth(20, 5)       -> 15")
            print("  fruneko(5)          -> 120")
            print("  prizent(7)          -> True")
            print("  hypnaro(3, 4)        -> 5.0")
            print("\nAvailable functions:")
            for name, (_, count, description) in FUNCTIONS.items():
                print(f"  {name:<12} ({count} argument(s)) - {description}")
            continue

        try:
            result, description = evaluate(line)
            print(f"Output: {result}")
        except ZorvaniError as exc:
            print(f"ZORVANI Error: {exc}")

if __name__ == "__main__":
    main()
