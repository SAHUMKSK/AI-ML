# 28. Check whether "Apple" exists before removing it.

techBrands = ["Apple", "Samsung", "MSI", "MI", "Dell", "HP", "Asus", "Lenovo"]

if "Apple" in techBrands:
    print("Apple was in the list.")
    techBrands.remove("Apple")
else:
    print("Apple was not present in the list.")