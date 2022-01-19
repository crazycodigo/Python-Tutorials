def usd_to_inr(usd):
    inr = usd * 74
    return inr

usd_input = [100, 60, 87, 93.45]
for i in usd_input:
    output_inr = usd_to_inr(i)
    print("Amount in INR: Rs.", output_inr)
