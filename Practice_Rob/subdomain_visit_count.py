"""
Author: Soumil Ramesh Kulkarni
Date: 03.02.2024

Question:
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.



Example 1:

Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
Explanation: We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
Example 2:

Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
"""


class Solution:

    # Clean Solution #######
    def subdomainVisits_clean_solution(self, cpdomains: List[str]) -> List[str]:
        domain_count = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)

            subdomains = domain.split(".")

            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                print(subdomain)
                if subdomain in domain_count:
                    domain_count[subdomain] += count
                else:
                    domain_count[subdomain] = count

        result = []
        for subdomain in domain_count:
            result.append("{} {}".format(domain_count[subdomain], subdomain))
        return result

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_tracker = {}
        for obj in cpdomains:
            temp = obj.split(" ")
            temp1 = temp[1].split(".")[::-1]
            for j in range(len(temp1) + 1):
                temp2 = temp1[:j][::-1]
                # print (".".join(temp2))
                temp3 = ".".join(temp2)
                if temp3 in domain_tracker:
                    domain_tracker[temp3] += int(temp[0])
                else:
                    domain_tracker[temp3] = int(temp[0])
        # print(domain_tracker)
        result = []
        for i in domain_tracker:
            if i != '':
                test = ""
                test += str(domain_tracker[i])
                test += " "
                test += str(i)
                result.append(test)
        return result
