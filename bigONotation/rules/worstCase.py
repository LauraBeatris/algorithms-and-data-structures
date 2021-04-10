"""
Big O is care more about the worst case scenario, but we can also think about best & average cases.
"""

companiesList = ['twitter', 'spotify', 'tiktok', 'tinder', 'google']
companiesLargeList = ['facebook'] * 100000
companiesLargeList.append('twitter')

def findTwitter(companies): 
    for company in companies:
        if company != 'twitter': continue 

        print('Found twitter')
        break # Breaking the loop doesn't matter for the worst case scenario because it's already the last loop

findTwitter(companiesLargeList)

"""
Big O Notation of findTwitter: O(n) - Linear time (Always based on the worst case scenario)

=== Why Linear time? === 

Because the worst-case scenario would be, for instance, an array of one million items with twitter as the last item
and the number of operations executed would increase linearly according to the input size 

- Best case: Constant time (Twitter is the first item of the companies list)
- Average case: Linear time (Twitter is in the middle of the companies list)
- Worst case: Linear time (Twitter is the last item of the companies list)
"""