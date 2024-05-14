from quart import Quart, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/youtube_data'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

app = Quart(__name__)

class ViewerAgeTable(Base):
    __tablename__ = 'viewer_age_table'
    id = Column(Integer, primary_key=True)
    viewer_age = Column(String)

@app.route('/')
async def hello_world():
    return 'Hello, World!'

@app.route('/data', methods=['GET'])
async def get_data():
    try:
        async with Session() as session:
            data = session.query(ViewerAgeTable).all()
            # return jsonify({'data': [item.to_dict() for item in data]})
            return data
    except Exception as e:
        app.logger.error(f"Error fetching data: {e}")
        return jsonify({'error': 'An error occurred while fetching datssa'}), 500