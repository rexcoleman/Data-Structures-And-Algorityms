
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        print(bin(n))
        print(bin(0xffffffff))
        print(bin(n >> 1))
        print(bin(n >> 2))
        print(bin(n >> 3))
        print(bin(n >> 4))
        print(bin(n >> 5))
        print(bin(n >> 6))
        print(bin(n >> 7))
        print(bin(n >> 8))
        print(bin(n >> 9))
        print(bin(n >> 10))
        print(bin(n >> 11))
        print(bin(n >> 12))
        print(bin(n >> 13))
        print(bin(n >> 14))
        print(bin(n >> 15))
        print(bin(n >> 16))
        print(bin(n))
        print(bin(n << 1))
        print(bin(n << 2))
        print(bin(n << 3))
        print(bin(n << 4))
        print(bin(n << 5))
        print(bin(n << 6))
        print(bin(n << 7))
        print(bin(n << 8))
        print(bin(n << 9))
        print(bin(n << 10))
        print(bin(n << 11))
        print(bin(n << 12))
        print(bin(n << 13))
        print(bin(n << 14))
        print(bin(n << 15))
        print(bin(n << 16))
        print(bin(n >> 16))
        print(bin((n & 0xffffffff) >> 16))
        print(bin(n))
        print(bin(0xffffffff))
        print(bin(n << 16))
        print(bin((n & 0xffffffff) << 16))
        # print(bin(n << 16))
        n = (n >> 16) | (n << 16)
        print("Apres 16")
        print(bin(n))
        print(bin(0xff00ff00))
        print(bin(n & 0xff00ff00))
        print(bin((n & 0xff00ff00) >> 1))
        print(bin((n & 0xff00ff00) >> 2))
        print(bin((n & 0xff00ff00) >> 3))
        print(bin((n & 0xff00ff00) >> 4))
        print(bin((n & 0xff00ff00) >> 5))
        print(bin((n & 0xff00ff00) >> 6))
        print(bin((n & 0xff00ff00) >> 7))
        print(bin((n & 0xff00ff00) >> 8))
        print(bin((n & 0x00ff00ff) << 1))
        print(bin((n & 0x00ff00ff) << 2))
        print(bin((n & 0x00ff00ff) << 3))
        print(bin((n & 0x00ff00ff) << 4))
        print(bin((n & 0x00ff00ff) << 5))
        print(bin((n & 0x00ff00ff) << 6))
        print(bin((n & 0x00ff00ff) << 7))
        print(bin((n & 0x00ff00ff) << 8))
        print(bin(n))
        print(bin((n & 0xff00ff00) >> 8))
        print(bin((n & 0x00ff00ff) << 8))
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        print("Apres 8")
        print(bin(n))
        print(bin(0xf0f0f0f0))
        print(bin(n & 0xf0f0f0f0))
        print(bin((n & 0xf0f0f0f0) >> 4))
        print(bin(n))
        print(bin(0x0f0f0f0f))
        print(bin(n & 0x0f0f0f0f))
        print(bin((n & 0x0f0f0f0f) << 4))
        print(bin((n & 0xf0f0f0f0) >> 4))
        print(bin((n & 0x0f0f0f0f) << 4))
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        print("Apres 4")
        print(bin(n))
        print(bin(0xcccccccc))
        print(bin(n & 0xcccccccc))
        print(bin((n & 0xcccccccc) >> 2))
        print(bin((n & 0xcccccccc) << 2))
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        print("Apres 2")
        print(bin(n))
        print(bin(0xcccccccc))
        print(bin(0x33333333))
        print(bin(n & 0xcccccccc))
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        print("Apres 1")
        print(bin(n))
        print(bin(0xaaaaaaaa))
        print(bin(0x55555555))
        print(bin(n & 0x55555555))


        return n

if __name__ == '__main__':

    # Inputs
    # n0 = 0b00000010100101000001111010011100
    n1 = 0b00000010100101000001111010011100
    n2 = 0b11111111111111111111111111111101

    bin_n_1 = bin(0x0202020202)[2:]
    # print(bin_n_1)
    bin_n_2 = bin(0x010884422010)[2:]
    # print(bin_n_2)

    # Expected Outputs:
    # 1: 964176192
    # 2: 3221225471

    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.reverseBits(n1)
    # t_2 = test_2.reverseBits(n2)

    print(f"Test 1: {t_1}")
    # print(f"Test 2: {t_2}")