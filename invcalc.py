def investment_calculator(investment, init_pop, popularity):
    rate = (popularity-init_pop)/init_pop
    new_amount = (rate*1.2+1)*investment
    return float('{:.2f}'.format(new_amount))