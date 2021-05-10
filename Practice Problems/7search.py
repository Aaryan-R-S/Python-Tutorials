# ------------- 1 ----------------
import re

docs = ['How pretty the baby was!', 'I hope you accept this by the time the baby is born.', 'The baby was asleep in her cradle, and he must not make a noise and waken her.', 'Mom, when will the baby be born?', 'The baby smiled but did not wake up.', 'Where is baby howse?', 'How could anyone love the baby the way she could?', 'We are going to have a baby, not a sin.', 'Someone else carries this baby for you.', 'When you want a baby so bad, the first morning of sickness is a blessing.']

print("\nSearch here!")
inp = input()

if re.findall(r"^(\s)+$", inp) or inp == '':
    print(f"0 Search results found !\n")
    exit()
inps = inp.split(" ")

# ------------- 3 ----------------
scoreList = []

for d in docs:
    score = 0
    for i in inps:
        reg = re.findall(i.lower(), d.lower())
        for r in reg:
            score+=1
    scoreList.append(score)
    
sortedScorewithDocs = [s for s in sorted(zip(scoreList, docs), reverse=True)]
# print(sortedScorewithDocs)

# ------------- 3 ----------------
srchList = []

for score, doc in sortedScorewithDocs:
    if score != 0 :
        srchList.append(doc)

print(f"\n {len(srchList)} Search results found :")

for d in srchList:
    print(d)

print(" ")
