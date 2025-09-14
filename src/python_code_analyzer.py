import ast

class PythonCodeAnalyzer:
    """Analyze Python code using AST"""

    def parse_code(self, code):
        try:
            tree = ast.parse(code)
            return {"success": True, "tree": tree}
        except SyntaxError as e:
            return {"success": False, "error": str(e)}

    def extract_features(self, tree):
        return {
            "functions": len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]),
            "loops": len([n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))]),
            "conditionals": len([n for n in ast.walk(tree) if isinstance(n, ast.If)]),
            "complexity": self._complexity(tree),
        }

    def _complexity(self, tree):
        c = 1
        for n in ast.walk(tree):
            if isinstance(n, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                c += 1
        return c

if __name__ == "__main__":
    code = """def add_numbers(a,b): return a - b"""
    analyzer = PythonCodeAnalyzer()
    parsed = analyzer.parse_code(code)
    if parsed["success"]:
        print("Analysis:", analyzer.extract_features(parsed["tree"]))
    else:
        print("Error:", parsed)