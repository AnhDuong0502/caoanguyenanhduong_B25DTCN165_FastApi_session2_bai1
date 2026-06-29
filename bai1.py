from fastapi import FastAPI

app = FastAPI()
students = ["An", "Binh", "Cuong"]


@app.get("/Students")
def get_students():
    return {"Danh sach sinh vien: ": ",".join(students)}
