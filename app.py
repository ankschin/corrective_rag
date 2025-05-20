from dotenv import load_dotenv

from graphs.graph import app

load_dotenv()




if __name__== "__main__":
    print("hello!!!")
    print(app.invoke({"question": "what is agent memory?"}))

    