dictionary={"Pawan": 1, "Aditya": 2, "Shah": 3}
dictionary_keys=list(dictionary.keys())
dictionary_keys.sort()
sorted_dictionary={i: dictionary[i] for i in dictionary_keys}
print(f"After sorting the dictionary on the basis of keys: {sorted_dictionary}")