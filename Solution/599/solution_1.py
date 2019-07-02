class Solution:
    def findRestaurant(self, list1, list2):
        d1 = dict(zip(list1, range(len(list1))))
        d2 = dict(zip(list2, range(len(list2))))
        results = d1.keys() & d2.keys()
        if len(results) == 1:
            return list(results)
        d = {key:d1[key] + d2[key] for key in results}
        temp = min(d.values())
        result = [key for key in d.keys() if d[key] == temp]
        return result

if __name__ == '__main__':
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["KFC", "Shogun", "Burger King"]
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    result = Solution().findRestaurant(list1, list2)
    print(result)
