class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cheapest, second_cheapest, *_ = sorted(prices)
        money_after_buying = money - cheapest - second_cheapest
        if money_after_buying < 0:
            return money
        else:
            return money_after_buying