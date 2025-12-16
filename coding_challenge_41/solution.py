def number_to_words(number: int) -> str:
    words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return ' '.join(words[int(d)] for d in str(number))

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("In words:", number_to_words(num))
