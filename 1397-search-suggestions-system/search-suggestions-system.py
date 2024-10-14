class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        res = []
        products.sort() # sort the products

        # we'll follow a 2 pointer approach as we have a sorted list of products
        l,r = 0, len(products)-1

        # Iterate through the search word
        for i in range(len(searchWord)):
            c = searchWord[i]

            while l <=r and (len(products[l]) <= i or products[l][i] !=c ): # while there's no overlap, and the product at index l has an ith character and the ith char of product l is not same as the character c of searchWord:
                l += 1

            while l <=r and (len(products[r]) <= i or products[r][i] !=c ): # while there's no overlap, and the product at index l has an ith character and the ith char of product l is not same as the character c of searchWord:
                r -= 1
            
            res.append([])
            remain = r - l + 1

            for j in range(min(3, remain)):
                res[-1].append(products[l+j])
        
        return res
