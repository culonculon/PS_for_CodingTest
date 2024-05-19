class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, reverse=True)

        print("points =",points)
        stage = points.pop()
        cnt = 1

        while points:
            print()
            print("stage =",stage)
            for i in range(stage[0], stage[1]+1):
                print("i =", i)
                print("points[ck] =",points[-1])
                if i in points[-1]:
                    if len(points) > 0:
                        points.pop()
                    break

            if len(points) > 0:
                stage = points.pop()
                cnt += 1
  


        return cnt