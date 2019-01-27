productions = [
	{'left': 'T', 'right': ['T', 'mul', 'F']},
	{'left': 'T', 'right': ['T', 'div', 'F']},
	{'left': 'T', 'right': ['F']},
	{'left': 'F', 'right': ['n']},
	{'left': 'F', 'right': ['lparen', 'E', 'rparen']},
	{'left': 'E', 'right': ['E', 'plus', 'T']},
	{'left': 'E', 'right': ['E', 'minus', 'T']},
	{'left': 'E', 'right': ['T']},
	{'left': '~S~', 'right': ['E']}
]

table = {
	'0': {
		'ACTION': {
			'n': 's2_7',
			'lparen': 's3_8'
		},
		'GOTO': {
			'E': '1',
			'n': '2_7',
			'lparen': '3_8',
			'T': '4_9',
			'F': '5_10'
		}
	},
	'1': {
		'ACTION': {
			'$': 'acc',
			'plus': 's12_17',
			'minus': 's11_15'
		},
		'GOTO': {
			'minus': '11_15',
			'plus': '12_17'
		}
	},
	'2_7': {
		'ACTION': {
			'mul': 'r3',
			'rparen': 'r3',
			'plus': 'r3',
			'minus': 'r3',
			'div': 'r3',
			'$': 'r3'
		},
		'GOTO': {

		}
	},
	'3_8': {
		'ACTION': {
			'n': 's2_7',
			'lparen': 's3_8'
		},
		'GOTO': {
			'E': '6_18',
			'n': '2_7',
			'lparen': '3_8',
			'T': '4_9',
			'F': '5_10'
		}
	},
	'4_9': {
		'ACTION': {
			'mul': 's13_22',
			'div': 's14_23',
			'$': 'r7',
			'plus': 'r7',
			'minus': 'r7',
			'rparen': 'r7'
		},
		'GOTO': {
			'mul': '13_22',
			'div': '14_23'
		}
	},
	'5_10': {
		'ACTION': {
			'rparen': 'r2',
			'plus': 'r2',
			'div': 'r2',
			'mul': 'r2',
			'$': 'r2',
			'minus': 'r2'
		},
		'GOTO': {

		}
	},
	'6_18': {
		'ACTION': {
			'plus': 's12_17',
			'rparen': 's16_29',
			'minus': 's11_15'
		},
		'GOTO': {
			'minus': '11_15',
			'rparen': '16_29',
			'plus': '12_17'
		}
	},
	'11_15': {
		'ACTION': {
			'n': 's2_7',
			'lparen': 's3_8'
		},
		'GOTO': {
			'n': '2_7',
			'lparen': '3_8',
			'T': '21_26',
			'F': '5_10'
		}
	},
	'12_17': {
		'ACTION': {
			'n': 's2_7',
			'lparen': 's3_8'
		},
		'GOTO': {
			'n': '2_7',
			'lparen': '3_8',
			'T': '20_27',
			'F': '5_10'
		}
	},
	'13_22': {
		'ACTION': {
			'n': 's2_7',
			'lparen': 's3_8'
		},
		'GOTO': {
			'n': '2_7',
			'lparen': '3_8',
			'F': '19_25'
		}
	},
	'14_23': {
		'ACTION': {
			'n': 's2_7',
			'lparen': 's3_8'
		},
		'GOTO': {
			'n': '2_7',
			'lparen': '3_8',
			'F': '24_28'
		}
	},
	'16_29': {
		'ACTION': {
			'minus': 'r4',
			'rparen': 'r4',
			'plus': 'r4',
			'$': 'r4',
			'mul': 'r4',
			'div': 'r4'
		},
		'GOTO': {

		}
	},
	'19_25': {
		'ACTION': {
			'minus': 'r0',
			'rparen': 'r0',
			'$': 'r0',
			'plus': 'r0',
			'mul': 'r0',
			'div': 'r0'
		},
		'GOTO': {

		}
	},
	'20_27': {
		'ACTION': {
			'mul': 's13_22',
			'div': 's14_23',
			'rparen': 'r5',
			'$': 'r5',
			'minus': 'r5',
			'plus': 'r5'
		},
		'GOTO': {
			'mul': '13_22',
			'div': '14_23'
		}
	},
	'21_26': {
		'ACTION': {
			'mul': 's13_22',
			'div': 's14_23',
			'rparen': 'r6',
			'plus': 'r6',
			'$': 'r6',
			'minus': 'r6'
		},
		'GOTO': {
			'mul': '13_22',
			'div': '14_23'
		}
	},
	'24_28': {
		'ACTION': {
			'$': 'r1',
			'rparen': 'r1',
			'plus': 'r1',
			'mul': 'r1',
			'div': 'r1',
			'minus': 'r1'
		},
		'GOTO': {

		}
	}
}
