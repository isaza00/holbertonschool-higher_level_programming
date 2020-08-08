#!/usr/bin/python3
"""query finds state id of a given state in State model"""

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
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
