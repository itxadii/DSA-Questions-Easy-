L1 = [1, 2, 2, 3, 2, 3, 4, 5]

num_counter = {}

for i in L1:
    if i in num_counter:
        num_counter[i] += 1
    else:
        num_counter[i] = 1
print(num_counter)

temp = 0 
final_result = None
for k, v in num_counter.items():
    if v > temp:
        temp = v 
        final_result = k 

print(final_result)

