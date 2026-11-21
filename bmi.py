def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print(f"bmi: {bmi:.2f}")

    if bmi < 18.5:
        print("category: under weight")
        return -1
    elif bmi <= 25.0:
        print("category: normal weight")
        return 0
    else:
        print("category: over weight")
        return 1


if __name__ == "__main__":
    calculate_bmi(weight=101, height=1.80)