class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        events = sorted(zip(timestamp, username, website))

        n_user = []
        n_time = []
        n_site = []

        for time, user, site in events:
            n_user.append(user)
            n_time.append(time)
            n_site.append(site)

        journey = {}

        for x in range(0, len(n_user)):
            user = n_user[x]
            site = n_site[x]

            if user not in journey:
                journey[user] = []

            journey[user].append(site)

        visits = {}

        for user in journey:
            history = journey[user]

            x = 0
            while x + 3 <= len(history):
                tmp = history[x:x + 3]
                tmp_tuple = tuple(tmp)
                visits[tmp_tuple] = visits.get(tmp_tuple, 0) + 1

                x += 1

        print(visits)
        visits_sorted = sorted(visits, reverse=True)
        new_map = {}

        for elem in visits_sorted:
            new_map[elem] = visits[elem]

        rev_dict = dict((v, k) for k, v in new_map.items())
        max_occ = max(rev_dict, key=int)

        return list(rev_dict[max_occ])
