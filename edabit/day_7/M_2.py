class FivesThreesOnes:

    def __init__(self, num):
        self.number = num

    def get_fives_threes_ones(self):

        count = {}
        for i in [1, 3, 5]:
            temp = self.number // i
            count[i] = temp

        return count


k = FivesThreesOnes(8)
print(k.get_fives_threes_ones())
