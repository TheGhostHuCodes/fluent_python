import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
memv = memoryview(numbers)
print("memoryview length: %i" % len(memv))
print("value at position 0: %i" % memv[0])
memv_oct = memv.cast('B')
print("memoryview cast to unsigned char: %s" % memv_oct.tolist())
print("set unsigned char at position 5 to value 4")
memv_oct[5] = 4
print(numbers)
