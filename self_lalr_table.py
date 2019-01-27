productions = [
	{'left': 'RD', 'right': ['I', 'IS', 'S']},
	{'left': 'CI', 'right': ['comma', 'I', 'CI']},
	{'left': 'CI', 'right': []},
	{'left': 'P', 'right': ['ST', 'I', 'dot', 'P']},
	{'left': 'P', 'right': ['TD', 'dot', 'P']},
	{'left': 'P', 'right': ['RD', 'dot', 'P']},
	{'left': 'P', 'right': []},
	{'left': 'S', 'right': ['I', 'S']},
	{'left': 'S', 'right': []},
	{'left': 'TD', 'right': ['T', 'I', 'CI']},
	{'left': '~S~', 'right': ['P']}
]

table = {
	'0': {
		'ACTION': {
			'ST': 's3',
			'$': 'r6',
			'T': 's4',
			'I': 's1'
		},
		'GOTO': {
			'I': '1',
			'RD': '2',
			'ST': '3',
			'T': '4',
			'P': '5',
			'TD': '6'
		}
	},
	'1': {
		'ACTION': {
			'IS': 's8'
		},
		'GOTO': {
			'IS': '8'
		}
	},
	'2': {
		'ACTION': {
			'dot': 's10'
		},
		'GOTO': {
			'dot': '10'
		}
	},
	'3': {
		'ACTION': {
			'I': 's11'
		},
		'GOTO': {
			'I': '11'
		}
	},
	'4': {
		'ACTION': {
			'I': 's7'
		},
		'GOTO': {
			'I': '7'
		}
	},
	'5': {
		'ACTION': {
			'$': 'acc'
		},
		'GOTO': {

		}
	},
	'6': {
		'ACTION': {
			'dot': 's9'
		},
		'GOTO': {
			'dot': '9'
		}
	},
	'7': {
		'ACTION': {
			'comma': 's12',
			'dot': 'r2'
		},
		'GOTO': {
			'comma': '12',
			'CI': '13'
		}
	},
	'8': {
		'ACTION': {
			'I': 's16',
			'dot': 'r8'
		},
		'GOTO': {
			'I': '16',
			'S': '17'
		}
	},
	'9': {
		'ACTION': {
			'ST': 's3',
			'$': 'r6',
			'T': 's4',
			'I': 's1'
		},
		'GOTO': {
			'I': '1',
			'RD': '2',
			'ST': '3',
			'T': '4',
			'P': '14',
			'TD': '6'
		}
	},
	'10': {
		'ACTION': {
			'ST': 's3',
			'$': 'r6',
			'T': 's4',
			'I': 's1'
		},
		'GOTO': {
			'I': '1',
			'RD': '2',
			'ST': '3',
			'T': '4',
			'P': '18',
			'TD': '6'
		}
	},
	'11': {
		'ACTION': {
			'dot': 's15'
		},
		'GOTO': {
			'dot': '15'
		}
	},
	'12': {
		'ACTION': {
			'I': 's21'
		},
		'GOTO': {
			'I': '21'
		}
	},
	'13': {
		'ACTION': {
			'dot': 'r9'
		},
		'GOTO': {

		}
	},
	'14': {
		'ACTION': {
			'$': 'r4'
		},
		'GOTO': {

		}
	},
	'15': {
		'ACTION': {
			'ST': 's3',
			'$': 'r6',
			'T': 's4',
			'I': 's1'
		},
		'GOTO': {
			'I': '1',
			'RD': '2',
			'ST': '3',
			'T': '4',
			'P': '19',
			'TD': '6'
		}
	},
	'16': {
		'ACTION': {
			'I': 's16',
			'dot': 'r8'
		},
		'GOTO': {
			'I': '16',
			'S': '20'
		}
	},
	'17': {
		'ACTION': {
			'dot': 'r0'
		},
		'GOTO': {

		}
	},
	'18': {
		'ACTION': {
			'$': 'r5'
		},
		'GOTO': {

		}
	},
	'19': {
		'ACTION': {
			'$': 'r3'
		},
		'GOTO': {

		}
	},
	'20': {
		'ACTION': {
			'dot': 'r7'
		},
		'GOTO': {

		}
	},
	'21': {
		'ACTION': {
			'comma': 's12',
			'dot': 'r2'
		},
		'GOTO': {
			'comma': '12',
			'CI': '22'
		}
	},
	'22': {
		'ACTION': {
			'dot': 'r1'
		},
		'GOTO': {

		}
	}
}
