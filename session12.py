import pandas as pd
from collections import namedtuple
from faker import Faker
fake = Faker()

def create_rows_faker(num=1):
    output = [{"name":fake.name(),
#                   "blood type":fake.blood_group(),
                   "current location":fake.current_location(),
                   "dob":fake.birthdate(),
                   "date_time":fake.date_time(),
                   } for x in range(num)]
    return output


df_faker = pd.DataFrame(create_rows_faker(10000))




fake.profile().keys()

fake.blood-group
fake.name
  
fake.name()
