# python
import os
import sys;
import math
from io import BytesIO, IOBase


# ----------------------------Manual Functions Begin----------------------------------------#
def upperbound(arr, val):
    start = 0;
    end = len(arr) - 1;
    ans = -1
    while (start <= end):
        mid = (start + end) // 2
        if (arr[mid] <= val):
            start = mid + 1
        else:
            ans = mid
            end = mid - 1
    return ans


def lowerbound(arr, val):
    length = len(arr);
    answer = -1;
    start = 0;
    end = length - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == val:
            answer = middle
            end = middle - 1
        elif arr[middle] > val:
            end = middle - 1
        else:
            start = middle + 1
    return answer


def D2B(n):
    arr = []
    while (n > 0):
        temp = n;
        m = 0;
        p = 1
        while (temp):
            rem = temp % 10;
            temp = int(temp / 10)
            if (rem != 0):
                m += p;
            p *= 10;
        arr.append(m);
        n = n - m;
    return arr


def sort2D(arr, axis):
    arr = sorted(arr, key=lambda x: x[axis]);
    return arr


def DD(rows, cols):
    arr = [[0 for i in range(cols)] for j in range(rows)];
    return arr


# ----------------------------Manual Functions End----------------------------------------#

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion
if (os.path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


# ------------------------------------------------Templete Ends------------------------------------------------------#

def solve():

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'w', 'x', 'y', 'z']

    n, q = map(int, input().split())

    s = input()

    for i in range(q):

        l, r = map(int, input().split())

        sub_segment = s[l - 1:r]  # generate sub sequence

        result = 0

        set_sub_segment = list(dict.fromkeys(sub_segment))

        for j in set_sub_segment:
            count = sub_segment.count(j)
            data = alphabets.index(j) + 1
            data = count * data
            result += data

        print(result)


f = 0

if __name__ == "__main__":
    if f == 1:
        t = int(input())
        while (t):
            solve();
            t -= 1
    else:
        solve()