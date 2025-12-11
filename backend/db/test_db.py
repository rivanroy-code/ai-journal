from base import SessionLocal
from sqlalchemy import text

def test_db():
    db = SessionLocal()
    try:
        result = db.execute(text('SELECT 1;'))
        print("Database connection test successful:", result.scalar())
    finally:
        db.close()

if __name__ == "__main__":
    test_db()