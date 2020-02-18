#parameters
eth_price=100
new_eth_price=70
collat=3.5
debt=200
flash_fee=.01

#don't need to change anything below this line
print("initial collateral",collat)
print("initial debt",debt)
print("current ETH price",eth_price)
print("next oracle ETH price",new_eth_price)
print("flash loan fee",flash_fee)
print("initial collat_ratio",collat*eth_price/debt)
print("next collat_ratio",collat*new_eth_price/debt)
print("will be liquidated",collat*new_eth_price/debt<=1.5)
print("new collat value will be",new_eth_price*collat)
print("value to recover",new_eth_price*collat-debt)
if collat*new_eth_price/debt>1.5:
	print("not going to be liquidated, chill")
else:
	if new_eth_price*collat-debt<=0:
		print("not enough value to recover")
	else:

		flash_amount = (new_eth_price*collat-1.5*debt)/(flash_fee-.5)

		print("flash loan amount",flash_amount)
		if new_eth_price*collat-debt<=flash_fee*flash_amount:
			print("not worth the flash loan, get liquidated or liquidate yourself")
		else:
			amount_owed = flash_amount+flash_fee
			new_debt = debt-flash_amount

			print("new collat_ratio at old eth price",collat*eth_price/new_debt)
			print("new collat_ratio at new eth price would be",collat*new_eth_price/new_debt)
			print("need to pay back flash by selling",amount_owed/new_eth_price)

			new_collat = collat - amount_owed/new_eth_price
			print("new collateral amount is",new_collat)
			print("new collat_ratio is",new_collat*new_eth_price/new_debt)
			