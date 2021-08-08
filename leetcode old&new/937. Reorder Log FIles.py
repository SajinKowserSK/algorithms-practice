class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letterLogs = []
        digitLogs = []

        for log in logs:
            tmp = log.split()

            no_id = " ".join(tmp[1:])
            no_id = no_id + " " + tmp[0]

            if tmp[1].isalpha():
                letterLogs.append(no_id)

            else:
                digitLogs.append(log)

        letterLogs.sort()

        for x in range(0, len(letterLogs)):
            log = letterLogs[x]

            tmp = log.split()
            log_id = tmp[-1]
            tmp.pop(-1)

            new = " ".join(tmp)
            new = log_id + " " + new

            letterLogs[x] = new

        return letterLogs + digitLogs


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letterLogs = []
        map1 = {}

        for log in logs:
            tmp = log.split()

            no_id = " ".join(tmp[1:])

            if tmp[1].isalpha():

                if no_id not in map1:
                    map1[no_id] = [log]

                else:
                    map1[no_id].append(log)
                    map1[no_id].sort()

                letterLogs.append(no_id)

        letterLogs.sort()

        for x in range(0, len(letterLogs)):
            log = letterLogs[x]

            pull = map1[log]
            letterLogs[x] = pull[0]

            if len(pull) > 1:
                map1[log].pop(0)

        for log in logs:

            tmp = log.split()

            if tmp[1].isdigit():
                letterLogs.append(log)

        return letterLogs
