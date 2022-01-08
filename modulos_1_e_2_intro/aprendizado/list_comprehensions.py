str = "0123401234012340123401234"
period = len(str[: str.index(str[0], 1)])
list = [str[i : i + period] for i in range(0, len(str), period)]
print(".".join(list))
