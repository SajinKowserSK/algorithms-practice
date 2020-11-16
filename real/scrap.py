import pandas as pd

f = open("recs.txt", "r")

master = []
for line in f:
    curr = []
    split = line.split()

    for x in range(0, len(split)):
        word = split[x]
        if "@" in word:
            indice = x


    email = split[indice]
    company_name = split[0:indice]
    separator = ' '
    left = separator.join(company_name)
    recruiter = split[indice+1:]
    seperator = ' '
    right = seperator.join(recruiter)

    curr.append(left)
    curr.append(email)
    curr.append(right)

    master.append(curr)

final  = pd.DataFrame(master, columns=['Company Name', 'Email', 'Recruiter Name'])
final.to_csv (r'',
              index = False, header=True)

print('done')
