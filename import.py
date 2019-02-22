import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://kzjankntmihkdd:6317d9e49054dd42b6c376fcbdf9b1b4b5b2e15ca865ee68de52d1ee4afb82c1@ec2-54-204-41-109.compute-1.amazonaws.com:5432/d48jtpn37eflvj")
# db = scoped_session(sessionmaker(engine))
db = scoped_session(sessionmaker(bind=engine))


def main():
    file = open('books.csv', 'r')
    f = csv.reader(file)
    for isbn,title,author,year in f:
        db.execute(
            "INSERT INTO books (isbn, title, author,year) VALUES (:isbn, :title, :author, :year)",
            {"isbn": isbn, "title": title, "author": author, "year":year})
       
        db.commit()
               
        print(isbn, title, author, year)

if __name__ == '__main__':
    main()