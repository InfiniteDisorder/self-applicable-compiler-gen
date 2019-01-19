arithmetic = {'T1': {'right_paren': [''], 'star': ['star', 'F', 'T1'], '$': [''], 'plus_sign': ['']},
'F': {'left_paren': ['left_paren', 'E', 'right_paren'], 'n': ['n']},
'T': {'left_paren': ['F', 'T1'], 'n': ['F', 'T1']},
'E1': {'right_paren': [''], 'plus_sign': ['plus_sign', 'T', 'E1'], '$': ['']},
'E': {'left_paren': ['T', 'E1'], 'n': ['T', 'E1']},
}
arithmetic_TL = {'left_paren', 'star', 'right_paren', 'plus_sign', 'n'}
arithmetic_NTL = {'E1', 'F', 'T', 'E', 'T1'}
