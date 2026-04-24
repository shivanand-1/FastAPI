from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    1: {"name": "shiva", "age": 21, "marks": 71},
    2: {"name": "kehoo", "age": 22, "marks": 22}
}

@app.get("/student/{student_id}")
def get_student(student_id: int, field: str = None):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    if field:
        if field not in students[student_id]:
            raise HTTPException(status_code=404, detail="Field not found")
        return {field: students[student_id][field]}

    return students[student_id]