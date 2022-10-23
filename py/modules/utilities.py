def cinput(message: str, cast_error: str, unsatisfied_error: str, convert=None, satisfied=None):
	string = input(message)
	result = 0

	if convert is not None:
		while True:
			try:
				result = convert(string)
				break
			except ValueError:
				string = input(cast_error)

	if satisfied is not None:
		while not satisfied(result):
			string = input(unsatisfied_error)

			if convert is not None:
				while True:
					try:
						result = convert(string)
						break
					except ValueError:
						string = input(cast_error)

	return result