import numpy as np

PLAYS_NUM=1000

def krap_expected_win(n_dice, \
                      res_values, \
                      win_values_repeat, \
                      loose_values_repeat):
    def krap_play():
       dices = np.random.randint(1, 7, n_dice) 
       value = np.sum(dices)

       if value in res_values.keys():
           return res_values[value]
       else:
           our_value = value
           while True:
              dices = np.random.randint(1, 7, n_dice) 
              value = np.sum(dices)
              if value in loose_values_repeat.keys():
                  return loose_values_repeat[value]
              elif value == our_value:
                  return win_values_repeat[our_value]

    res = np.zeros(PLAYS_NUM)
    for i in range(PLAYS_NUM):
        res[i] = krap_play()
        
    return np.sum(res) / PLAYS_NUM

if __name__ == '__main__':
    exp_value = krap_expected_win(2, \
                            {7:1, 11:1, 2:-1, 3:-1, 12:-1}, \
                            {6:1, 8:1, 4:2, 10:2, 5:1.5, 9:1.5}, \
                            {7:-1})
    print(exp_value)
