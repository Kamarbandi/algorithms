arr = [3,5,6,1,2,7,4]

def mergerSort(arr):
	if len(arr) <= 1:
		return arr
	middle = len(arr) // 2
	left = mergerSort(arr[:middle])
	right = mergerSort(arr[middle:])
	return merge(left, right)

def mem_decorator(func):
	cache = {}
	def wrapper(*args, **kwargs):
		key = args + tuple(sorted(kwargs.items()))
		if key not in cache:
			cache[key] = func(*args, **kwargs)
		return cache[key]
	return wrapper

@mem_decorator
def fib(n):
	if n in(0, 1):
		return 1
	return fib(n-1) + fib(n-2)


def merge(left, right):
	result = []
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left[0])
			left = left[1:]
		else:
			result.append(right[0])
			right = right[1:]
	if len(left) > 0:
		result += left
	if len(right) > 0:
		result += right
	return result


#print(mergerSort(arr))

print(fib(128))