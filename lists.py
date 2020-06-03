han_description = ['stuck-up', 'half-witted', 'scruffy-looking', 'nerf herder']

# lukes_real_hands = ["left"]
# people_who_like_jar_jar = []

# print(han_description[1])
# print(people_who_like_jar_jar[100])

# index = 0
# print("Why are You:")
# while index < len(han_description):
#     print("%d. %s" % (index + 1, han_description[index]))
#     index += 1
counter = 1
for descriptor in han_description:
    # print(f"{counter}. {descriptor}")
    print("%d. %s" % (counter, descriptor))
    length = len(han_description)
    if counter < length:
        print("The next one up is %s" % han_description[counter])
    counter += 1
