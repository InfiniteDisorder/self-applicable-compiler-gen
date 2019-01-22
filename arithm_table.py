arithmetic = {'E': {'left_paren': ['T', 'E1'], 'n': ['T', 'E1']},
'T1': {'star': ['star', 'F', 'T1'], 'plus_sign': [''], '$': [''], 'right_paren': ['']},
'E1': {'plus_sign': ['plus_sign', 'T', 'E1'], '$': [''], 'right_paren': ['']},
'F': {'n': ['n'], 'left_paren': ['left_paren', 'E', 'right_paren']},
'T': {'left_paren': ['F', 'T1'], 'n': ['F', 'T1']},
}
arithmetic_TL = {'n', 'plus_sign', 'star', 'left_paren', 'right_paren'}
arithmetic_NTL = {'E', 'T1', 'E1', 'F', 'T'}
