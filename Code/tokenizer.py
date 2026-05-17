import tiktoken

def main():

    # To get the tokeniser corresponding to a specific model in the OpenAI API:
    enc = tiktoken.encoding_for_model("gpt-4o-mini")
    print(enc.encode("Building Large Language Model from scratch"))
    print(enc.decode(enc.encode("This is Apple")))
    print("End of Text Token id: ", enc.eot_token)


if __name__ == "__main__":
    main()
