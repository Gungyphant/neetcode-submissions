class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        did_anything = True
        while did_anything:
            did_anything = False
            result = [accounts[0]]
            for account in accounts[1:]:
                name, *emails = account
                for oi, other_account in enumerate(result):
                    if any(e in other_account for e in emails):
                        result[oi] += emails
                        did_anything = True
                        break
                else:
                    result.append(account)
            accounts = result.copy()
        # Clean and sort
        clean_result = []
        for account in result:
            name, *emails = account
            emails = sorted(set(emails))
            # print(name, emails)
            clean_result.append([name, *emails])
        return clean_result

        