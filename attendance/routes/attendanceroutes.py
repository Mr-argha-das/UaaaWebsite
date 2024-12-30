from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from attendance.models.attendancemodel import AttendanceTable
from datetime import datetime
router = APIRouter()

@router.get('/api/addattendance/{userId}/{status}')
async def addAttendanceAPI(userId: str, status: str):
    savedata = AttendanceTable(userId=userId, status=status, date=datetime.now().strftime("%d-%m-%Y"))
    savedata.save()
    print(savedata.to_json())
    return RedirectResponse(url="/admin/addattendance")

@router.get('/api/get-alltendance')
async def getAttendanceData():
    findata = AttendanceTable.objects.all()
    return findata