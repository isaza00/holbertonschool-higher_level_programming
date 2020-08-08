#!/usr/bin/python3
"""prints all cities from db"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(City.state_id == State.id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
