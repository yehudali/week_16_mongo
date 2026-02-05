from bson import ObjectId
from bson.errors import InvalidId

from pymongo.collection import Collection


class RecordRepository:
    def __init__(self, collection: Collection) :
        self.collection =  collection


    def insert_to_coll(self,data):
            self.collection.delete_many({})
            result = self.collection.insert_many(data)
            return result
      
    def get_engineering_high_salary_employees(self):
        query = {"job_role.department":"Engineering", "salary":{"$gt": 65000}}
        fields = {"_id":0,"employee_id":1, "name":1, "salary":1}
        result = self.collection.find(query, fields)
        return(list(result))

    def get_employees_by_age_and_role(self):
        query = {"age":{"$gte":30, "$lte": 45},"job_role.title": {"$in": ["Specialist", "Engineer"]}  }
        fields = {"_id":0}
        result = self.collection.find(query, fields)
        result = list(result)
        return result
    
    def get_top_seniority_employees_excluding_hr(self):
        query = {"job_role.department": {"$ne":"HR"}}
        fields = {"_id":0}
        result = self.collection.find(query,fields).sort("years_at_company", -1).limit(7)
        result = list(result)
        print(result)
        return result

    def get_employees_by_age_or_seniority(self):
        query = {"age":{"gt":50},"years_at_company":{"$lt":3}} ##################!!!!!!!!!!!!!!!!!!!
        fields = {"_id":0, "employee_id": 1, "name":1, "age":1, "years_at_company":1}
        result = self.collection.find(query,fields)
        result = list(result)
        return(result)
     
    def get_managers_excluding_departments(self):
        query = {"job_role.department":["Sales", "Marketing"]}
        fields = {"_id":0}
        result = self.collection.find(query,fields)
        result = list(result)
        return(result)

    def get_employees_by_lastname_and_age(self):
        query = {"age":{"$lt":35}}
        fields = {"_id":0, "name":1, "age":1,"job_role.department":1}
        result = self.collection.find(query,fields)
        result = list(result)
        return(result)