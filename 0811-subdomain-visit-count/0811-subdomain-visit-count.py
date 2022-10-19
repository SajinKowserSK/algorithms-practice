from collections import defaultdict 

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(lambda: 0)

        for domain in cpdomains:
            elems = domain.split(" ")
            count, string = int(elems[0]), elems[1]
            domSplit = string.split(".")
            
            domains[domSplit[-1]] += count
            domains[domSplit[-2]+"."+domSplit[-1]] += count 

            if len(domSplit) == 3:
                domains[domSplit[-3]+"."+domSplit[-2]+"."+domSplit[-1]] += count 

        retL = []
        for key in domains:
            retL.append(str(domains[key]) + " " + key)

        return retL