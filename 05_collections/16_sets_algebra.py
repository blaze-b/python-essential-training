blue_eyes = {'0livia', 'Harry', 'Lily', 'Jack', 'Amelia'}


blond_hair = {'Harry' 'Jack', 'Amelia', 'Mia', 'Joshua'}

smell_hcn = {'Harry', 'Amelia'}

taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}

o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}

b_blood = {'Amelia', 'Jack'}

a_blood = {'Harry'}

ab_blood = {'Joshua', 'Lola'}

print(blue_eyes.union(blond_hair))


print(blue_eyes.intersection(blond_hair))

print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

print(blond_hair.difference(blue_eyes))

print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))

print(blond_hair.symmetric_difference(blue_eyes))


print(blond_hair.symmetric_difference(blue_eyes) ==
      blue_eyes.symmetric_difference(blond_hair))


print(smell_hcn.issubset(blond_hair))

print(taste_ptc.issuperset(smell_hcn))

print(a_blood.isdisjoint(b_blood))
