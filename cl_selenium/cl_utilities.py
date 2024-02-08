def split_investment_type(investment):
    """
    This function, split_investment_type, takes a string as input and splits it into two parts based on the '('
    character. It then returns the first part of the string without the last character and the second part of the
    string without the last character.

    :param investment: The input string that needs to be split.
    :return: investment_name (string): The first part of the input string without the last character.
    :return: investment_type (string): The second part of the input string without the last character.
    """
    strs = investment.split('(')
    return strs[0][:-1], strs[1][:-1]
