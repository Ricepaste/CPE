while True:
    try:
        testcase = int(input())
        note = {'c': [2, 3, 4, 7, 8, 9, 10],
                'd': [2, 3, 4, 7, 8, 9],
                'e': [2, 3, 4, 7, 8],
                'f': [2, 3, 4, 7],
                'g': [2, 3, 4],
                'a': [2, 3],
                'b': [2],
                'C': [3],
                'D': [1, 2, 3, 4, 7, 8, 9],
                'E': [1, 2, 3, 4, 7, 8],
                'F': [1, 2, 3, 4, 7],
                'G': [1, 2, 3, 4],
                'A': [1, 2, 3],
                'B': [1, 2]}

        for _ in range(testcase):
            last_finger = []
            finger_times = [0 for _ in range(10)]

            cmd = list(input())
            if (len(cmd) == 0):
                finger_times = list(map(str, finger_times))
                print(" ".join(finger_times))
                continue
            for cur in cmd:
                for finger in note[cur]:
                    if finger in last_finger:
                        continue
                    else:
                        finger_times[finger-1] += 1
                last_finger = note[cur]

            finger_times = list(map(str, finger_times))
            print(" ".join(finger_times))
    except:
        break
