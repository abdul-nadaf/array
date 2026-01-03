def main():
    score =[78,85,90,66,88]
    total=sum(score)
    average=total/len(score)
    print("===main/master branch output===")
    print(f"score: {score}")
    print(f"sum: {total}")
    print(f"average: {average}")
    print(f"--local branch--")
    print(f"maximum: {max(score)}")
    print(f"minimum: {min(score)}")
if __name__ == "__main__":
    main()