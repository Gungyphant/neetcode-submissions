class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        _money = money
        money -= min(prices)
        prices.remove(min(prices))
        money -= min(prices)
        if money < 0:
            return _money
        return money