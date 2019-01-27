productions = [
	{'left': 'S', 'right': []},
	{'left': 'S', 'right': ['I', 'S']},
	{'left': 'P', 'right': ['F']},
	{'left': 'P', 'right': ['F', 'P']},
	{'left': 'F', 'right': ['ST', 'I', 'dot']},
	{'left': 'F', 'right': ['T', 'CI', 'dot']},
	{'left': 'F', 'right': ['I', 'IS', 'S', 'dot']},
	{'left': 'CI', 'right': ['I']},
	{'left': 'CI', 'right': ['CI', 'comma', 'I']},
	{'left': '~S~', 'right': ['P']}
]

table = {
	'0': {
		'ACTION': {
			'ST': 's5',
			'T': 's2',
			'I': 's3'
		},
		'GOTO': {
			'F': '1',
			'T': '2',
			'I': '3',
			'P': '4',
			'ST': '5'
		}
	},
	'1': {
		'ACTION': {
			'$': 'r2',
			'ST': 's5',
			'T': 's2',
			'I': 's3'
		},
		'GOTO': {
			'F': '1',
			'T': '2',
			'I': '3',
			'P': '10',
			'ST': '5'
		}
	},
	'2': {
		'ACTION': {
			'I': 's7'
		},
		'GOTO': {
			'I': '7',
			'CI': '8'
		}
	},
	'3': {
		'ACTION': {
			'IS': 's6'
		},
		'GOTO': {
			'IS': '6'
		}
	},
	'4': {
		'ACTION': {
			'$': 'acc'
		},
		'GOTO': {

		}
	},
	'5': {
		'ACTION': {
			'I': 's9'
		},
		'GOTO': {
			'I': '9'
		}
	},
	'6': {
		'ACTION': {
			'dot': 'r0',
			'I': 's11'
		},
		'GOTO': {
			'I': '11',
			'S': '12'
		}
	},
	'7': {
		'ACTION': {
			'dot': 'r7',
			'comma': 'r7'
		},
		'GOTO': {

		}
	},
	'8': {
		'ACTION': {
			'dot': 's14',
			'comma': 's13'
		},
		'GOTO': {
			'comma': '13',
			'dot': '14'
		}
	},
	'9': {
		'ACTION': {
			'dot': 's15'
		},
		'GOTO': {
			'dot': '15'
		}
	},
	'10': {
		'ACTION': {
			'$': 'r3'
		},
		'GOTO': {

		}
	},
	'11': {
		'ACTION': {
			'dot': 'r0',
			'I': 's11'
		},
		'GOTO': {
			'I': '11',
			'S': '16'
		}
	},
	'12': {
		'ACTION': {
			'dot': 's18'
		},
		'GOTO': {
			'dot': '18'
		}
	},
	'13': {
		'ACTION': {
			'I': 's17'
		},
		'GOTO': {
			'I': '17'
		}
	},
	'14': {
		'ACTION': {
			'$': 'r5',
			'ST': 'r5',
			'T': 'r5',
			'I': 'r5'
		},
		'GOTO': {

		}
	},
	'15': {
		'ACTION': {
			'$': 'r4',
			'ST': 'r4',
			'T': 'r4',
			'I': 'r4'
		},
		'GOTO': {

		}
	},
	'16': {
		'ACTION': {
			'dot': 'r1'
		},
		'GOTO': {

		}
	},
	'17': {
		'ACTION': {
			'dot': 'r8',
			'comma': 'r8'
		},
		'GOTO': {

		}
	},
	'18': {
		'ACTION': {
			'$': 'r6',
			'ST': 'r6',
			'T': 'r6',
			'I': 'r6'
		},
		'GOTO': {

		}
	}
}
