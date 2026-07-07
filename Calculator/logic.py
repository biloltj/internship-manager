# logic.py
import math
import re

class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        self.memory = 0.0
        self.history = []

    def append_to_expression(self, value: str):
        """Appends characters or operators to the current expression."""
        # Map visual operators to Python evaluation operators safely
        if value == "×":
            self.expression += "*"
        elif value == "÷":
            self.expression += "/"
        else:
            self.expression += str(value)

    def clear(self):
        self.expression = ""

    def backspace(self):
        self.expression = self.expression[:-1]

    def memory_clear(self):
        self.memory = 0.0

    def memory_recall(self) -> float:
        return self.memory

    def memory_add(self, current_display_val: str):
        try:
            self.memory += float(current_display_val)
        except ValueError:
            pass

    def memory_subtract(self, current_display_val: str):
        try:
            self.memory -= float(current_display_val)
        except ValueError:
            pass

    def evaluate(self) -> str:
        """Parses and safely evaluates the math expression."""
        if not self.expression:
            return ""

        try:
            # Replace visual functions with math module functions securely
            eval_expr = self.expression
            eval_expr = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', eval_expr)
            eval_expr = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', eval_expr)
            eval_expr = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', eval_expr)
            eval_expr = re.sub(r'log\((.*?)\)', r'math.log10(\1)', eval_expr)
            eval_expr = re.sub(r'√\((.*?)\)', r'math.sqrt(\1)', eval_expr)
            eval_expr = eval_expr.replace('^', '**')

            # Handle percentage conversion safely (e.g., 50% -> 50*0.01)
            eval_expr = eval_expr.replace('%', '*0.01')

            # Strict sandbox evaluation context using math
            allowed_globals = {"__builtins__": None, "math": math}
            
            result = eval(eval_expr, allowed_globals, {})
            
            # Format numbers cleanly (integers stay flat, floats truncated elegantly)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            elif isinstance(result, float):
                result = round(result, 8)

            readable_expr = self.expression.replace('*', '×').replace('/', '÷')
            self.history.append(f"{readable_expr} = {result}")
            
            self.expression = str(result)
            return self.expression

        except ZeroDivisionError:
            self.expression = ""
            return "Error: Division by 0"
        except (ValueError, SyntaxError, TypeError):
            self.expression = ""
            return "Error: Invalid Input"