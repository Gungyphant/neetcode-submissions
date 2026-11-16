class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        import itertools
        # import itertools
        # best = float("inf")
        # for number_removed in range(len(colors)):
        #     for removeds in itertools.combinations(range(len(colors)), number_removed):
        #         time = 0
        #         for r in removeds:
        #             time += neededTime[r]
        #             if time > best:
        #                 break
        #         else:
        #             with_removed = [c for i, c in enumerate(colors) if i not in removeds]
        #             if not any(c == with_removed[i + 1] for i, c in enumerate(with_removed[:-1])):
        #                 best = time
        # return best
        result = 0
        for c, group in itertools.groupby(enumerate(colors), key=lambda x: x[1]):
            # print(list(group))
            possibles = [neededTime[i] for i, _ in group]
            # print(c, possibles)
            tot = 0
            biggest = 0
            for n in possibles:
                tot += n
                if n > biggest:
                    biggest = n
            result += tot - biggest
        return result

