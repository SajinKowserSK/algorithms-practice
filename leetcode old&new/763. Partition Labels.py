class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        map1 = {c: i for i, c in enumerate(S)}

        end = 0
        i = 0
        partitions = []

        while i < len(S):
            end = map1[S[i]]
            j = i

            while j < end:
                j += 1
                end = max(end, map1[S[j]])

            partitions.append(j - i + 1)

            i = j + 1

        return partitions





