import os
for filename in os.listdir('../homework2 06.03.23/papka1'):
    if filename.endswith(".json"):
        os.remove('papka1/мусор.json')
    else:
        continue
for filename in os.listdir('../homework2 06.03.23/2'):
    if filename.endswith(".json"):
        os.remove('2/мусор.json')
    else:
        continue
for filename in os.listdir('../homework2 06.03.23/3'):
    if filename.endswith(".json"):
        os.remove('3/мусор.json')
    else:
        continue
for filename in os.listdir('../homework2 06.03.23/4'):
    if filename.endswith(".json"):
        os.remove('4/мусор.json')
    else:
        continue

