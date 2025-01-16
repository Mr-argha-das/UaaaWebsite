from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from attendance.models.attendancemodel import AttendanceTable
from datetime import datetime
router = APIRouter()

@router.get('/api/addattendance/')
async def addAttendanceAPI(request: Request):
    userData = request.session.get('userdata')
    findata = AttendanceTable.objects(date=f"{datetime.now().strftime("%d-%m-%Y")}",userId=str(userData['data']['_id']['\u0024oid']) ).first()
    if findata :
        current_time = datetime.now()
        starttime = datetime.strptime(findata.intime, '%H:%M')
        endtime = datetime.strptime(current_time.strftime('%H:%M'), '%H:%M')
        duration = endtime-starttime
        hours = duration.seconds // 3600  # Total seconds divided by 3600 (seconds per hour)
        minutes = (duration.seconds % 3600) // 60
        findata.duration = f"{hours}:{minutes}"
        findata.outtime = current_time.strftime('%H:%M')
        findata.save()
        return RedirectResponse(url="/admin/dashboard")
    else:
         current_time = datetime.now()
         savedata = AttendanceTable(
             userId=str(userData['data']['_id']['\u0024oid']), 
             intime=current_time.strftime('%H:%M'),
             outtime="-",
             duration="-",
             date=datetime.now().strftime("%d-%m-%Y"))
         savedata.save()
         print(savedata.to_json())
         return RedirectResponse(url="/admin/dashboard")

@router.post('/api/addattendance/')
async def addAttendanceAPI(request: Request):
    userData = request.session.get('userdata')
    findata = AttendanceTable.objects(date=f"{datetime.now().strftime("%d-%m-%Y")}",userId=str(userData['data']['_id']['\u0024oid']) ).first()
    if findata :
        current_time = datetime.now()
        starttime = datetime.strptime(findata.intime, '%H:%M')
        endtime = datetime.strptime(current_time.strftime('%H:%M'), '%H:%M')
        duration = endtime-starttime
        hours = duration.seconds // 3600  # Total seconds divided by 3600 (seconds per hour)
        minutes = (duration.seconds % 3600) // 60
        findata.duration = f"{hours}:{minutes}"
        findata.outitme = current_time.strftime('%H:%M')
        findata.save()
        return RedirectResponse(url="/admin/dashboard")
    else:
         current_time = datetime.now()
         savedata = AttendanceTable(
             userId=str(userData['data']['_id']['\u0024oid']), 
             intime=current_time.strftime('%H:%M'),
             outtime="-",
             duration="-",
             date=datetime.now().strftime("%d-%m-%Y"))
         savedata.save()
         print(savedata.to_json())
         return RedirectResponse(url="/admin/dashboard")
   
    
    

@router.get('/api/get-alltendance')
async def getAttendanceData():
    findata = AttendanceTable.objects.all()
    return findata