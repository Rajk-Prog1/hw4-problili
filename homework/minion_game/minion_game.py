def minion_game(s: str) -> str:
    vowels = 'AIEOU'
    score_1 = len(sorted(s[i:j] for i, x in enumerate(s) for j in range(i + 1, len(s) + 1) if x in vowels))
    score_2 = len(sorted(s[i:j] for i, x in enumerate(s) for j in range(i + 1, len(s) + 1) if x not in vowels))
    if score_1 > score_2:
        return f'Kevin {score_1}'
    elif score_1 < score_2:
         return f'Stuart {score_2}'
    else:
        return 'DRAW'

print(minion_game('BANANA'))