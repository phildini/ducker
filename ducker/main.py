def prompt_for_text(text):
    answer = input(text)
    return answer


def run(input=None):
    answer = prompt_for_text("Hello! Do you have a question? ")
    return answer

if __name__ == '__main__':
    run()
