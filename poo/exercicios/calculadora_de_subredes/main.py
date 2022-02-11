from calc_ipv4 import CalcIpv4

CASE_ONE_ADDRESS = "192.168.0.25"
CASE_ONE_MASK = "255.255.255.192"
CASE_TWO_ADDRESS = "10.20.12.45"
CASE_TWO_MASK = "255.255.255.192"


network1_info = CalcIpv4(address=CASE_ONE_ADDRESS, mask=CASE_ONE_MASK)
print("##### Net 1 ############")
network1_info.print_info()
print()
network1_info = CalcIpv4(address=CASE_ONE_ADDRESS, prefix=26)
print("##### Net 1 ############")
network1_info.print_info()
print()
network2_info = CalcIpv4(address=CASE_TWO_ADDRESS, mask=CASE_TWO_MASK)
print("##### Net 2 ############")
network2_info.print_info()
print()
network2_info = CalcIpv4(address=CASE_TWO_ADDRESS, prefix=26)
print("##### Net 2 ############")
network2_info.print_info()
