from collections import defaultdict

class SketchRules:
    def __init__(self):
        self.rules = defaultdict(list)

    def add_rule(self, category, rule_str):
        self.rules[category].append(rule_str)

    @property
    def categories(self):
        return list(self.rules.keys())

    @staticmethod
    def load(fpath):
        fin = open(fpath, "r", encoding="UTF-8")
        rules_pat = r"\d:"
        rule_cat = "(none)"
        sr = SketchRules()
        for ln in fin.readlines():
            if ln.startswith("="):
                rule_cat = ln.strip().replace("=", "")
            elif ln.startswith("      "):
                if ln.strip():
                    sr.add_rule(rule_cat, ln.strip())
        fin.close()

        return sr