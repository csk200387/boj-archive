import collections

def find_largest_groups(words):
  groups = collections.defaultdict(list)
  for word in words:
    groups[tuple(sorted(word))].append(word)
  return sorted(groups.items(), key=lambda x: (-len(x[1]), x[1]))[:5]
if __name__ == "__main__":
  words = list(map(str.strip, [*open(0)]))
  result = find_largest_groups(words)
  for group in result[:5]:
    print(f"Group of size {len(group[1])}: {' '.join(sorted(group[1]))} .")