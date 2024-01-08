text = (input("Введите текст: ")).split()

# collection = []
# count = 0
#
# for word in text:
#     if word not in collection:
#         collection.append(word)
#         count += 1

collection = set()
for word in text:
    collection.add(word.lower())

print(f"В тексте содержится {len(collection)} различных слов")


