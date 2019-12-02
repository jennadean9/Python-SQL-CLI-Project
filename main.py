from peewee import PostgresDatabase, Model, CharField, DateField
import random

db = PostgresDatabase('flashcards', user='postgres',
                      password='',           host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Flashcard(BaseModel):
    question = CharField()
    answer = CharField()


db.create_tables([Flashcard])

length = Flashcard(
    question='What method returns the length of a list?', answer='len()')
length.save()

uppercase = Flashcard(
    question='What method takes every character in a string and converts it to uppercase?', answer='.upper()')
uppercase.save()

lowercase = Flashcard(
    question='What method takes every character in a string and converts it to lowercase?', answer='.lower()')
lowercase.save()

string = Flashcard(
    question='What is the string interpolation for "Hi #{name}"?', answer='"Hi %s" %(name)')
string.save()

current_datetime = Flashcard(
    question='What method can you use to get the current datetime from DateTime?', answer='datetime.now()')
current_datetime.save()

push_to_list = Flashcard(
    question='What method pushes an element to the end of a list?', answer='.append()')
push_to_list.save()

range_method = Flashcard(
    question='What method returns a sequence of numbers where its arguments consist of (start (of numbers), stop, by increments)', answer='range()')
range_method.save()


# def flash_quiz():
#     print("Welcome to Python Flashcards! I give you a question about Python, and you guess the answer. Here we go!")


res = input("would you like to create a new flashcard (type "new") or quiz youself with existing flashcards (type "quiz")? (new / quiz) ")
if res == 'new':
    new_question = input("please type the new flashcard question: ")
    new_answer = int(input("please type the answer to the new flashcard: "))
    new_flashcard = Flashcard(question=new_question, answer=new_answer
    new_flashcard.save()  # new person is stored in the db
    print(
        f"\nYou saved a new flashcard!\n{new_flashcard.question}\n{new_flashcard.answer} \n ")

elif res == 'quiz':
    flash_quiz()
