# -*- coding: utf-8 -*-
from .forms import UploadFileForm
from .models import CoinsAvailableModel, CoinsDeterminedModel

""" Return a dictionary
Receive the text file, transform into array of integer and remove numbers 
duplicated. Search if number was calculated. If not will calculate and save 
in database.
"""
def handle_uploaded_file(document):
    list_error = []     #Numbers out of range(1,250)
    list_done = []      #Objects of the model CoinsDeterminedModel
    error_msg = ""      #Error messages.
    if document.content_type == 'text/plain':
        numbers = document.read().split()
        try:
            numbers = [int(number) for number in numbers]
            numbers = set(numbers)
            for number in numbers:
                if 1 <= number <= 250:
                    try:
                        num_coins = CoinsDeterminedModel.objects.get(
                                        number=number
                                    )
                        list_done.append(num_coins)
                    except CoinsDeterminedModel.DoesNotExist:
                        number_of_coins = coin_determiner(number)
                        coins_determined = CoinsDeterminedModel(
                                            number=number,
                                            num_coins=number_of_coins
                                            )
                        coins_determined.save()
                        list_done.append(coins_determined)
                else: 
                   list_error.append(number)
        except ValueError:
            if not bool(number.strip()):
                number = "Empty line"
            error_msg = "Please check your file. Error found: " + number
    else:
        error_msg = "Failure! Text file required."
    dict_final = {
                    "done": list_done, "error": list_error, 
                    "error_msg": error_msg
                }
    return dict_final

"""Return a interger
Calculate all the possibilities and return the least number of coins, that when
added, equal the input integer.
"""
def coin_determiner(number):
    coins = CoinsAvailableModel.objects.all()
    coins = [coin.coin for coin in coins]
    list_num_coins = []
    for coin in coins:
        if coin <= number:
            num_coins = number/coin
            rest = number%coin
            if rest > 0:
                num_coins += coin_determiner(rest)
            list_num_coins.append(num_coins)
            num_coins = 0
    list_num_coins.sort()
    return list_num_coins[0]
