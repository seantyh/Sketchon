from dataclasses import dataclass
from types import List, Tuple

TokenTuple = Tuple[str, str, str]

@dataclass
class Token:
    word: str
    pos: str
    dep: str
    
    def __repr__(self):
        text = self.word
        if self.pos:
            text = self.text + "/" + self.pos
        else:
            text = text + "/"

        if self.dep:
            text = self.text + "/" + self.dep

        return text
        
class TokenStream:
    def __init__(self, tokens: Token):
        self.tokens = tokens

    def __iter__(self):
        return iter(self.tokens)
    
    def __repr__(self):
        text = "\u3000".join(f"{tok.word/tok.pos}" for tok in self.tokens)
        return "<TokenStream: {}>".format(text)

    def from_tuples(self, text_tups: List[TokenTuple]):
        pass

    def from_text(self, text: str):
        pass

    
        