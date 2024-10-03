from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Biconditional(AKnight, BKnight)),  # Si A es caballero, A y B son del mismo tipo.
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),  # Si A es knave, la afirmación es falsa.
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),  # Si B es caballero, A y B son de diferentes tipos.
    Implication(BKnave, Biconditional(AKnight, BKnight))  # Si B es knave, la afirmación de B es falsa.
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Biconditional(AKnight, Or(AKnight, AKnave)),  # A dice que es caballero o knave.
    Biconditional(AKnave, Not(Or(AKnight, AKnave))), # Si A es knave, entonces no dijo la verdad.
    # B dice que A dijo "Soy un knave"
    Implication(BKnight, AKnave),  # Si B es caballero, entonces A es knave.
    Implication(BKnave, AKnight),  # Si B es knave, A no dijo "Soy un knave", por lo tanto, A es caballero.
    # B dice que C es un knave
    Implication(BKnight, CKnave),  # Si B es caballero, entonces C es knave.
    Implication(BKnave, CKnight),  # Si B es knave, entonces C no es knave, por lo tanto, C es caballero.
    # C dice que A es un caballero
    Implication(CKnight, AKnight),  # Si C es caballero, entonces A es caballero.
    Implication(CKnave, AKnave),  # Si C es knave, entonces A es knave.
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
