# Some symbol calcs

# Arcane Symbols
def arcane_symbol_stat(level):
    if level == 0:
        return 0
    else:
        return 200 + level * 100


# Grandis Authentic/Sacred Symbols
def grandis_symbol_stat(level):
    if level == 0:
        return 0
    else:
        return 300 + level * 200


# Calculate total final stat from Arcane Symbols
def total_arcane_symbol_stat(arcane_symbols):
    total = 0
    for symbol in arcane_symbols:
        total += arcane_symbol_stat(arcane_symbols[symbol])

    return total


# Calculate total final stat from Grandis Symbols
def total_grandis_symbol_stat(grandis_symbols):
    total = 0
    for symbol in grandis_symbols:
        total += grandis_symbol_stat(grandis_symbols[symbol])

    return total
