productions = [
	{'left': 'S', 'right': ['C', 'C']},
	{'left': 'C', 'right': ['d']},
	{'left': 'C', 'right': ['c', 'C']},
	{'left': '~S~', 'right': ['S']}
]

table = {
	'2': {
		'ACTION': {
			'$': 'acc'
		},
		'GOTO': {
			'$': 'acc'
		}
	},
	'5_9': {
		'ACTION': {
			'c': 'r2',
			'$': 'r2',
			'd': 'r2'
		},
		'GOTO': {
			'c': 'r2',
			'$': 'r2',
			'd': 'r2'
		}
	},
	'1_6': {
		'ACTION': {
			'c': 's1_6',
			'd': 's4_8'
		},
		'GOTO': {
			'c': 's1_6',
			'd': 's4_8'
		}
	},
	'7': {
		'ACTION': {
			'$': 'r0'
		},
		'GOTO': {
			'$': 'r0'
		}
	},
	'0': {
		'ACTION': {
			'c': 's1_6',
			'd': 's4_8'
		},
		'GOTO': {
			'c': 's1_6',
			'd': 's4_8'
		}
	},
	'4_8': {
		'ACTION': {
			'd': 'r1',
			'$': 'r1',
			'c': 'r1'
		},
		'GOTO': {
			'd': 'r1',
			'$': 'r1',
			'c': 'r1'
		}
	},
	'3': {
		'ACTION': {
			'c': 's1_6',
			'd': 's4_8'
		},
		'GOTO': {
			'c': 's1_6',
			'd': 's4_8'
		}
	}
}
