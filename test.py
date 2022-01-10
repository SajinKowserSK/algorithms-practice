class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            if len(stk) == 0 or ast > 0:
                stk.append(ast)

            else:  # for collision, peak has to be going right and curr has to be going left
                while stk and stk[-1] > 0 and ast < 0:
                    print(stk[-1], ast)
                    collision = stk[-1] + ast
                    if collision > 0:  # peak is greater, keep just peak
                        continue

                    elif collision == 0:
                        stk.pop(-1)

                    else:  # incoming is greater
                        stk.pop(-1)
                        stk.append(collision)
        return stk




    print(self.asteroidCollision())