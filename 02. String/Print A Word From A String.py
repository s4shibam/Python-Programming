str = "Earth is round in shape"
print (str[0:5])    # This prints letters under 0 to 4th index
print (str[:5])     # Automatically detects starting index and prints letters till 4th index
print (str[0:])     # Automatically detects ending index and prints letters till end
print (str[0:23])   # This prints letters under 0 to 22nd index if available else till the last index.
print ("1 Gap 1 Letter Print = ", end = "")
print (str[0:23:2])