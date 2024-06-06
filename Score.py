from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Points for winning a game based on difficulty
POINTS_OF_WINNING = {
    "EASY": (3 * 3) + 5,  # Difficulty X 3 + 5
    "MEDIUM": (5 * 3) + 5,
    "HARD": (7 * 3) + 5
}

DATABASE_URL = "mysql+pymysql://root:dalit@mysql/games"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class UserScore(Base):
    __tablename__ = 'user_scores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Integer, nullable=False)

class ScoreManager:
    def __init__(self):
        self.session = Session()

    def add_score(self, difficulty):
        points = POINTS_OF_WINNING.get(difficulty, 0)

        user_score = self.session.query(UserScore).first()
        if user_score:
            user_score.score += points
        else:
            user_score = UserScore(score=points)

        self.session.add(user_score)
        self.session.commit()
