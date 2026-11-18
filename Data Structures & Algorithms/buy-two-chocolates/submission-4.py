class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cheapest, second_cheapest = float("inf"), float("inf")
        for p in prices:
            if p < cheapest:
                second_cheapest = cheapest
                cheapest = p
            elif p < second_cheapest:
                second_cheapest = p
        money_after_buying = money - cheapest - second_cheapest
        if money_after_buying < 0:
            return money
        else:
            return money_after_buying