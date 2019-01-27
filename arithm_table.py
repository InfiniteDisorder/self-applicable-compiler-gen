productions = [
	{'left': 'T', 'right': ['T', 'mul', 'F']},
	{'left': 'T', 'right': ['T', 'div', 'F']},
	{'left': 'T', 'right': ['F']},
	{'left': 'E', 'right': ['E', 'plus', 'T']},
	{'left': 'E', 'right': ['E', 'minus', 'T']},
	{'left': 'E', 'right': ['T']},
	{'left': 'F', 'right': ['n']},
	{'left': 'F', 'right': ['lparen', 'E', 'rparen']},
	{'left': '~S~', 'right': ['E']}
]

table = {
	'0': {
		'ACTION': {
			'n': 's5_14',
			'lparen': 's4_13'
		},
		'GOTO': {
			'T': '1_10',
			'E': '2',
			'F': '3_12',
			'lparen': '4_13',
			'n': '5_14'
		}
	},
	'1_10': {
		'ACTION': {
			'div': 's7_20',
			'mul': 's6_19',
			'$': 'r5',
			'plus': 'r5',
			'minus': 'r5',
			'rparen': 'r5'
		},
		'GOTO': {
			'mul': '6_19',
			'div': '7_20'
		}
	},
	'2': {
		'ACTION': {
			'$': 'acc',
			'plus': 's9_16',
			'minus': 's8_15'
		},
		'GOTO': {
			'minus': '8_15',
			'plus': '9_16'
		}
	},
	'3_12': {
		'ACTION': {
			'mul': 'r2',
			'$': 'r2',
			'rparen': 'r2',
			'minus': 'r2',
			'plus': 'r2',
			'div': 'r2'
		},
		'GOTO': {

		}
	},
	'4_13': {
		'ACTION': {
			'n': 's5_14',
			'lparen': 's4_13'
		},
		'GOTO': {
			'T': '1_10',
			'E': '11_22',
			'F': '3_12',
			'lparen': '4_13',
			'n': '5_14'
		}
	},
	'5_14': {
		'ACTION': {
			'plus': 'r6',
			'minus': 'r6',
			'rparen': 'r6',
			'div': 'r6',
			'mul': 'r6',
			'$': 'r6'
		},
		'GOTO': {

		}
	},
	'6_19': {
		'ACTION': {
			'n': 's5_14',
			'lparen': 's4_13'
		},
		'GOTO': {
			'F': '24_25',
			'lparen': '4_13',
			'n': '5_14'
		}
	},
	'7_20': {
		'ACTION': {
			'n': 's5_14',
			'lparen': 's4_13'
		},
		'GOTO': {
			'F': '18_29',
			'lparen': '4_13',
			'n': '5_14'
		}
	},
	'8_15': {
		'ACTION': {
			'n': 's5_14',
			'lparen': 's4_13'
		},
		'GOTO': {
			'T': '23_26',
			'F': '3_12',
			'lparen': '4_13',
			'n': '5_14'
		}
	},
	'9_16': {
		'ACTION': {
			'n': 's5_14',
			'lparen': 's4_13'
		},
		'GOTO': {
			'T': '21_27',
			'F': '3_12',
			'lparen': '4_13',
			'n': '5_14'
		}
	},
	'11_22': {
		'ACTION': {
			'rparen': 's17_28',
			'plus': 's9_16',
			'minus': 's8_15'
		},
		'GOTO': {
			'minus': '8_15',
			'plus': '9_16',
			'rparen': '17_28'
		}
	},
	'17_28': {
		'ACTION': {
			'minus': 'r7',
			'plus': 'r7',
			'rparen': 'r7',
			'$': 'r7',
			'mul': 'r7',
			'div': 'r7'
		},
		'GOTO': {

		}
	},
	'18_29': {
		'ACTION': {
			'minus': 'r1',
			'div': 'r1',
			'rparen': 'r1',
			'mul': 'r1',
			'plus': 'r1',
			'$': 'r1'
		},
		'GOTO': {

		}
	},
	'21_27': {
		'ACTION': {
			'div': 's7_20',
			'mul': 's6_19',
			'$': 'r3',
			'plus': 'r3',
			'rparen': 'r3',
			'minus': 'r3'
		},
		'GOTO': {
			'mul': '6_19',
			'div': '7_20'
		}
	},
	'23_26': {
		'ACTION': {
			'div': 's7_20',
			'plus': 'r4',
			'minus': 'r4',
			'mul': 's6_19',
			'$': 'r4',
			'rparen': 'r4'
		},
		'GOTO': {
			'mul': '6_19',
			'div': '7_20'
		}
	},
	'24_25': {
		'ACTION': {
			'minus': 'r0',
			'div': 'r0',
			'$': 'r0',
			'rparen': 'r0',
			'plus': 'r0',
			'mul': 'r0'
		},
		'GOTO': {

		}
	}
}
