# Vera owns N tops and N pants. The i-th top and i-th pants have colour i, for 1 ≤ i ≤ N, where all N colours are different from each other.

# An outfit consists of one top and one pants. Vera likes outfits where the top and pants are not the same colour.

# How many different outfits does she like?

N = int(input())

print(N*(N-1))