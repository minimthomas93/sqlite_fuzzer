from fuzzingbook.GrammarFuzzer import EvenFasterGrammarFuzzer
import grammar
import random
import re

class Fuzzer:
    def __init__(self):
        # This function must not be changed.
        self.grammar = grammar.grammar
        self.setup_fuzzer()
    
    def setup_fuzzer(self):
        # This function may be changed.
        self.fuzzer = EvenFasterGrammarFuzzer(self.grammar)

    def fuzz_one_input(self) -> str:
        return self.fuzzer.fuzz()
