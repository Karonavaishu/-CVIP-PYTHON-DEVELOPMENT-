import time

def typing_speed_test():
    text = "The quick brown fox jumps over the lazy dog"
    print("Type the following text as fast as you can:")
    print(text)
    input("Press Enter when you're ready...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = words_typed / (elapsed_time / 60)  # Words per minute
    
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Typing speed: {typing_speed:.2f} words per minute")

if __name__ == "__main__":
    typing_speed_test()

