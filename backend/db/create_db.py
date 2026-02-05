from base import Base, engine
from models import User, JournalEntry

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Successful.")


if __name__ == "__main__":
    init_db()