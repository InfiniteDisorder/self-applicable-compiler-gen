productions = [
	{'left': 'E', 'right': ['E', 'plus', 'T']},
	{'left': 'E', 'right': ['E', 'minus', 'T']},
	{'left': 'E', 'right': ['T']},
	{'left': 'T', 'right': ['T', 'mul', 'F']},
	{'left': 'T', 'right': ['T', 'div', 'F']},
	{'left': 'T', 'right': ['F']},
	{'left': 'F', 'right': ['n']},
	{'left': 'F', 'right': ['lparen', 'E', 'rparen']},
	{'left': '~S~', 'right': ['E']}
]

table = {
	'0': {
		'ACTION': {
			'n': 's1_19',
			'lparen': 's5_22'
		},
		'GOTO': {
			'n': '1_19',
			'F': '2_20',
			'E': '3',
			'T': '4',
			'lparen': '5_22'
		}
	},
	'1_19': {
		'ACTION': {
			'rparen': 'r6',
			'$': 'r6',
			'mul': 'r6',
			'div': 'r6',
			'minus': 'r6',
			'plus': 'r6'
		},
		'GOTO': {

		}
	},
	'2_20': {
		'ACTION': {
			'minus': 'r5',
			'mul': 'r5',
			'div': 'r5',
			'plus': 'r5',
			'$': 'r5',
			'rparen': 'r5'
		},
		'GOTO': {

		}
	},
	'3': {
		'ACTION': {
			'$': 'acc'
		},
		'GOTO': {
			'plus': '6_13',
			'minus': '7_14'
		}
	},
	'4': {
		'ACTION': {
			'$': 'r2',
			'plus': 'r2',
			'minus': 'r2',
			'mul': 's11_25',
			'div': 's10_24'
		},
		'GOTO': {
			'div': '10_24',
			'mul': '11_25'
		}
	},
	'5_22': {
		'ACTION': {

		},
		'GOTO': {
			'E': '8_26',
			'T': '9'
		}
	},
	'6_13': {
		'ACTION': {
			'n': 's1_19',
			'lparen': 's5_22'
		},
		'GOTO': {
			'n': '1_19',
			'F': '2_20',
			'T': '15_21',
			'lparen': '5_22'
		}
	},
	'7_14': {
		'ACTION': {
			'n': 's1_19',
			'lparen': 's5_22'
		},
		'GOTO': {
			'n': '1_19',
			'F': '2_20',
			'T': '17_23',
			'lparen': '5_22'
		}
	},
	'8_26': {
		'ACTION': {
			'rparen': 's12_27',
			'minus': 's7_14',
			'plus': 's6_13'
		},
		'GOTO': {
			'rparen': '12_27',
			'plus': '6_13',
			'minus': '7_14'
		}
	},
	'9': {
		'ACTION': {
			'rparen': 'r2'
		},
		'GOTO': {

		}
	},
	'10_24': {
		'ACTION': {
			'n': 's1_19',
			'lparen': 's5_22'
		},
		'GOTO': {
			'n': '1_19',
			'F': '18_29',
			'lparen': '5_22'
		}
	},
	'11_25': {
		'ACTION': {
			'n': 's1_19',
			'lparen': 's5_22'
		},
		'GOTO': {
			'n': '1_19',
			'F': '16_28',
			'lparen': '5_22'
		}
	},
	'12_27': {
		'ACTION': {
			'div': 'r7',
			'plus': 'r7',
			'mul': 'r7',
			'rparen': 'r7',
			'$': 'r7',
			'minus': 'r7'
		},
		'GOTO': {

		}
	},
	'15_21': {
		'ACTION': {
			'div': 's10_24',
			'mul': 's11_25',
			'$': 'r0',
			'minus': 'r0',
			'plus': 'r0',
			'rparen': 'r0'
		},
		'GOTO': {
			'div': '10_24',
			'mul': '11_25'
		}
	},
	'16_28': {
		'ACTION': {
			'div': 'r3',
			'minus': 'r3',
			'mul': 'r3',
			'$': 'r3',
			'rparen': 'r3',
			'plus': 'r3'
		},
		'GOTO': {

		}
	},
	'17_23': {
		'ACTION': {
			'minus': 'r1',
			'mul': 's11_25',
			'rparen': 'r1',
			'$': 'r1',
			'div': 's10_24',
			'plus': 'r1'
		},
		'GOTO': {
			'div': '10_24',
			'mul': '11_25'
		}
	},
	'18_29': {
		'ACTION': {
			'plus': 'r4',
			'div': 'r4',
			'mul': 'r4',
			'$': 'r4',
			'rparen': 'r4',
			'minus': 'r4'
		},
		'GOTO': {

		}
	}
}
