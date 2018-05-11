class Dirs:
    """
    The directions should be in order
    to make turnleft/right in Robot more convient
    if need 8-dirs, the order becomes:
    D, DR, R, UR, U, UL, L, DL
    """
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3
    DELTA = (
        ( 1,  0),
        ( 0,  1),
        (-1,  0),
        ( 0, -1),
    )


class Room:
    EMPTY = 0
    CLEANUP = 1
    OBSTACLE = 2
    ROBOT = 3

    def __init__(self, grid):
        """
        :type grid: list[list[int]]
        """
        self.__room = grid
        self.__cleanups = 0
        self.__robot_at = (0, 0)

        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                if grid[x][y] == self.CLEANUP:
                    self.__cleanups += 1
                elif grid[x][y] == self.ROBOT:
                    grid[x][y] = self.EMPTY
                    self.__robot_at = (x, y)

    def is_clear(self):
        """
        :rtype: bool
        """
        return self.__cleanups == 0

    def move_robot(self, direction):
        """
        :type direction: int, defined in Dirs
        :rtype: bool
        """
        m, n = len(self.__room), len(self.__room[0])
        x, y = self.__robot_at
        dx, dy = Dirs.DELTA[direction]
        _x, _y = x + dx, y + dy

        if not (0 <= _x < m and 0 <= _y < n):
            return False

        if self.__room[_x][_y] == self.OBSTACLE:
            return False

        self.__robot_at = (_x, _y)
        return True

    def clean(self, robot):
        """
        :type robot: Robot
        :rtype: void
        """
        if not isinstance(robot, Robot):
            return

        x, y = self.__robot_at

        if self.__room[x][y] == self.CLEANUP:
            self.__room[x][y] = self.EMPTY
            self.__cleanups -= 1

    def _get_robot(self):
        # for testing
        return self.__robot_at

    def _print_room(self):
        # for testing
        print(
            '\n'.join(str(r) for r in self.__room),
            '\nRobot at: ', self.__robot_at,
            '\nCleanups: ', self.__cleanups,
            '\n'
        )


class Robot:
    def __init__(self, room):
        """
        :type room: Room
        """
        self.__room = room
        self.__face = Dirs.DOWN

    def move(self, direction=None):
        """
        :type direction: int, defined in Dirs
        :rtype: bool
        """
        if direction in range(len(Dirs.DELTA)):
            self.__face = direction

        return self.__room.move_robot(self.__face) is True

    def turnleft(self, k=1):
        """
        :type k: int
        :rtype: void
        """
        n = len(Dirs.DELTA)
        self.__face = (self.__face + k) % n

    def turnrigt(self, k=1):
        """
        :type k: int
        :rtype: void
        """
        # note that, -1 % 4 == 3 in Python, or just (x - k + n) % n
        n = len(Dirs.DELTA)
        self.__face = (self.__face - k) % n

    def clean(self):
        """
        :rtype: void
        """
        self.__room.clean(self)

    def _get_face(self):
        # for testing
        return self.__face


class RobotCleanerDFS:
    """
    this approach is for we need to adjust `dir` manually
    the `robot.move()` only can move forward with 1 step
    """
    def clean_room(self, robot):
        """
        :type robot: Robot
        """
        if not isinstance(robot, Robot):
            return

        """
        robot's direction and coord no needs to same as room
        just start as (0, 0),
        and face 0 (this 0 just ref of dirs, no needs to treat it as Dirs.DOWN)
        Dirs.DELTA => D, R, U, L
        (1, 0), (0, 1), (-1, 0), (0, -1)
        """
        self.dfs(0, 0, 0, robot, set())

    def dfs(self, x, y, to_dir, robot, visited):
        robot.clean()
        visited.add((x, y))

        # down
        d = to_dir
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
            robot.turnrigt()
        else:
            robot.turnleft()

        # right
        d = (to_dir + 1) % len(Dirs.DELTA)
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
        else:
            robot.turnleft(2)

        # left
        d = (to_dir + 3) % len(Dirs.DELTA)
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
            robot.turnleft()
        else:
            robot.turnrigt()

        # up
        d = (to_dir + 2) % len(Dirs.DELTA)
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
            robot.turnrigt(2)

        # move robot when the recursion is back
        robot.move()


class RobotCleanerDFS2:
    """
    this approach is for we can just pass `dir` into `robot.move(dir)`
    """
    def clean_room(self, robot):
        """
        :type robot: Robot
        """
        if not isinstance(robot, Robot):
            return

        """
        robot's direction and coord no needs to same as room
        just start as (0, 0),
        and face 0 (this 0 just ref of dirs, no needs to treat it as Dirs.DOWN)
        """
        self.dfs(0, 0, 0, robot, set())

    def dfs(self, x, y, from_dir, robot, visited):
        # is there a api to detect the cell need to clean?
        robot.clean()
        visited.add((x, y))

        for to_dir in range(len(Dirs.DELTA)):
            if to_dir == from_dir:
                continue

            # to_dir is index and also the direction defined in Dirs
            dx, dy = Dirs.DELTA[to_dir]
            _x = x + dx
            _y = y + dy

            if (_x, _y) in visited:
                continue
            
            if robot.move(to_dir):
                self.dfs(_x, _y, (to_dir + 2) % len(Dirs.DELTA), robot, visited)
            else:
                visited.add((_x, _y))
        robot.move(from_dir)

        




if __name__ == '__main__':
    # for debugging
    room = Room([
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 0, 2, 2, 2, 2],
        [0, 1, 0, 3, 0, 1, 0, 1],
    ])
    robot = Robot(room)
    s = RobotCleanerDFS2()

    room._print_room()
    s.clean_room(robot)
    room._print_room()