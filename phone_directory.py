class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.avail_nums = set(range(maxNumbers))
        self.q = deque(range(maxNumbers))

    def get(self) -> int:
        if not self.q:
            return -1
        num = self.q.popleft()
        self.avail_nums.remove(num)
        return num

    def check(self, number: int) -> bool:
        return number in self.avail_nums

    def release(self, number: int) -> None:
        if number not in self.avail_nums:
            self.avail_nums.add(number)
            self.q.append(number)


# time complexity is O(1) for get, check and release
# space complexity is O(n)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
