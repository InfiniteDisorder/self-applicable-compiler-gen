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
			'n': 's5_12',
			'lparen': 's4_11'
		},
		'GOTO': {
			'T': '1_8',
			'E': '2',
			'F': '3_10',
			'lparen': '4_11',
			'n': '5_12'
		}
	},
	'1_8': {
		'ACTION': {
			'div': 's6_15',
			'mul': 's7_16',
			'minus': 'r2',
			'rparen': 'r2',
			'plus': 'r2',
			'$': 'r2'
		},
		'GOTO': {
			'div': '6_15',
			'mul': '7_16'
		}
	},
	'2': {
		'ACTION': {
			'$': 'acc',
			'plus': 's14_23',
			'minus': 's13_22'
		},
		'GOTO': {
			'minus': '13_22',
			'plus': '14_23'
		}
	},
	'3_10': {
		'ACTION': {
			'rparen': 'r5',
			'mul': 'r5',
			'plus': 'r5',
			'div': 'r5',
			'minus': 'r5',
			'$': 'r5'
		},
		'GOTO': {

		}
	},
	'4_11': {
		'ACTION': {
			'n': 's5_12',
			'lparen': 's4_11'
		},
		'GOTO': {
			'T': '1_8',
			'E': '9_19',
			'F': '3_10',
			'lparen': '4_11',
			'n': '5_12'
		}
	},
	'5_12': {
		'ACTION': {
			'minus': 'r6',
			'mul': 'r6',
			'div': 'r6',
			'$': 'r6',
			'rparen': 'r6',
			'plus': 'r6'
		},
		'GOTO': {

		}
	},
	'6_15': {
		'ACTION': {
			'n': 's5_12',
			'lparen': 's4_11'
		},
		'GOTO': {
			'F': '21_29',
			'lparen': '4_11',
			'n': '5_12'
		}
	},
	'7_16': {
		'ACTION': {
			'n': 's5_12',
			'lparen': 's4_11'
		},
		'GOTO': {
			'F': '18_25',
			'lparen': '4_11',
			'n': '5_12'
		}
	},
	'9_19': {
		'ACTION': {
			'rparen': 's24_27',
			'plus': 's14_23',
			'minus': 's13_22'
		},
		'GOTO': {
			'minus': '13_22',
			'plus': '14_23',
			'rparen': '24_27'
		}
	},
	'13_22': {
		'ACTION': {
			'n': 's5_12',
			'lparen': 's4_11'
		},
		'GOTO': {
			'T': '20_28',
			'F': '3_10',
			'lparen': '4_11',
			'n': '5_12'
		}
	},
	'14_23': {
		'ACTION': {
			'n': 's5_12',
			'lparen': 's4_11'
		},
		'GOTO': {
			'T': '17_26',
			'F': '3_10',
			'lparen': '4_11',
			'n': '5_12'
		}
	},
	'17_26': {
		'ACTION': {
			'div': 's6_15',
			'$': 'r0',
			'mul': 's7_16',
			'plus': 'r0',
			'minus': 'r0',
			'rparen': 'r0'
		},
		'GOTO': {
			'div': '6_15',
			'mul': '7_16'
		}
	},
	'18_25': {
		'ACTION': {
			'minus': 'r3',
			'plus': 'r3',
			'div': 'r3',
			'mul': 'r3',
			'rparen': 'r3',
			'$': 'r3'
		},
		'GOTO': {

		}
	},
	'20_28': {
		'ACTION': {
			'minus': 'r1',
			'mul': 's7_16',
			'$': 'r1',
			'rparen': 'r1',
			'div': 's6_15',
			'plus': 'r1'
		},
		'GOTO': {
			'div': '6_15',
			'mul': '7_16'
		}
	},
	'21_29': {
		'ACTION': {
			'plus': 'r4',
			'$': 'r4',
			'mul': 'r4',
			'rparen': 'r4',
			'minus': 'r4',
			'div': 'r4'
		},
		'GOTO': {

		}
	},
	'24_27': {
		'ACTION': {
			'minus': 'r7',
			'plus': 'r7',
			'$': 'r7',
			'mul': 'r7',
			'div': 'r7',
			'rparen': 'r7'
		},
		'GOTO': {

		}
	}
}
