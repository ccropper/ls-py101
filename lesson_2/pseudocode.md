
## 1. a function that returns the sum of two numbers


	START function

	GET 2 numbers

	return the product of the 2 numbers



## 2. a function that takes a list of strings, and returns a string 
that is all those strings concatenated together

	START

	GET a list of strings

	SET an empty string

	break up the list of strings and add each to the empty string

	return the now-filled string

	END


## 3. a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance:

```python
every_other([1,4,7,2,5]); # => [1,7,5]
```

	START

	GET list of integers

	SET new results list variable

	get the length of the list of integers 

	loop through each index of the list of integers with max as how many elements are in the list

	  IF the index is even, add to results list

	return results list

	END

## 4. a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.

	START

	GET a string and a given character 

	SET a counter to 0

	SET a location to None

	loop through characters in the string

	if the character at the position matches the provided character, increment counter by 1

	if the counter is 3, set location to the position of the character and break loop

	return location

	END

## 5. a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance:

```python
merge([1, 2, 3], [4, 5, 6]); # => [1, 4, 2, 5, 3, 6]
```

You may assume that both list arguments have the same number of elements.


	START 

	GET two lists

	SET an empty result list

	loop through list 1
		append element at index to result list

		loop through list 2
			append element at index to result list

	return result list

	END
