import os
from pydantic import BaseModel
from connection import get_db_collection
from fastapi import APIRouter,Depends, HTTPException, status
from  dal import RecordRepository

collection = get_db_collection()
repo = RecordRepository(collection)

router = APIRouter()

@router.get("/",status_code=status.HTTP_200_OK)
def hello_masege():
        return {"masege":'HII'}


class JobRole(BaseModel):
    title: str
    department: str

class Employ(BaseModel):
    employee_id:str
    name: str
    age: int
    years_at_company: int
    salary: int
    job_role: JobRole

@router.post("/insert_list_employes")
def upload_list(employes: list[Employ]):
    data = [employe.model_dump() for employe in employes]
    print(data)
    try:
        result = repo.insert_to_coll(data)
        
        return {"message": f"ingaction in db {len(result.inserted_ids)} documents"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# 1
@router.get("/employees/engineering/high-salary", status_code=status.HTTP_200_OK)
def r_get_engineering_high_salary_employees():
        try:
            result = repo.get_engineering_high_salary_employees()
            return [result]
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# 2
@router.get("//employees/by-age-and-role", status_code=status.HTTP_200_OK)
def r_get_employees_by_age_and_role():
        try:
            result = repo.get_employees_by_age_and_role()
            return [result]
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
# 3
@router.get("/employees/top-seniority", status_code=status.HTTP_200_OK)
def r_get_top_seniority_employees_excluding_hr():
    try:
        result = repo.get_top_seniority_employees_excluding_hr()
        return result
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


# 4
@router.get("/employees/age-or-seniority", status_code=status.HTTP_200_OK)
def r_get_employees_by_age_or_seniority():
    try:
        result = repo.get_employees_by_age_or_seniority()
        return result
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

     
# 5
@router.get("/employees/managers/excluding-departments")
def r_get_managers_excluding_departments():
    try:
        result = repo.get_managers_excluding_departments()
        return result
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# 6
@router.get("/employees/by-lastname-and-age")
def r_get_employees_by_lastname_and_age():
    try:
        result = repo.get_employees_by_lastname_and_age()
        return result
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


