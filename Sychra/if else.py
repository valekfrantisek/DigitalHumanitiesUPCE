is_clovek = False
Good = False
if is_clovek and Good:
    print("Jsi člověk a jsi dobrý")
elif is_clovek and not Good:
    print("Jsi člověk, ale nejsi dobrý")
elif not is_clovek and Good:
    print("Nejsi člověk, ale jsi dobrý")
else:
    print ("Nejsi člověk a nejsi dobrý")

characters = ["Gandalf", "Radagast", "Saruman"]
for a in characters:
    if a == "Saruman":
        break
    print(a)