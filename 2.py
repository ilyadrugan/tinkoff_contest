N = int(input())
allTeams = []
rating = {}
for i in range(N):
    names = list(map(str, input().split()))
    names.sort()
    allTeams.append(names)
    teamName = names[0] + names[1] + names[2]
    if teamName in rating:
        rating[teamName] += 1
    else:
        rating[teamName] = 1

print(rating)
print(rating[max(rating, key=rating.get)])
#MISHA IVAN GOSHA MISHA GOSHA IVAN VLAD IVAN VASYA KOLYA DIMA IVAN