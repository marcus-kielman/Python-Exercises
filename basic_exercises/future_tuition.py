def main():
    tuition = 10000
    year = 0

    while tuition < 20000:
        year += 1
        tuition += tuition * 0.07
    print("Tuition will be doubled in {} years".format(year))

if __name__=="__main__":
    main()
