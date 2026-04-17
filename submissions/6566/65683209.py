dict = {}
for line in [*open(0)]:
    data = line.rstrip()
    s_data = "".join(sorted(data))
    if s_data not in dict:
        dict[s_data] = [data]
    else:
        dict[s_data].append(data)
key_list = sorted(dict.keys(), key=lambda x: (-len(dict[x]), dict[x]))
for i in range(5):
    new_list = sorted(set(dict[key_list[i]]))
    joined = " ".join(new_list)
    print(f"Group of size {len(dict[key_list[i]])}: {joined} .")