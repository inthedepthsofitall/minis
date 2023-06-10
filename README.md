# minis
mini projects


 def bracket_combinations(numbers):
    def combo_possibilities(open, shut):
        if open == 0 and shut == 0:
            return 1
        result = 0
        if open > 0:
            result += combo_possibilities(open - 1, shut)
        if closed > open:
            result += combo_possibilities(open, shut - 1)
        return result

    return calculate_possibilities(numbers, numbers)
