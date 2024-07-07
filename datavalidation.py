from fastapi import FastAPI,status,HTTPException
from fastapi import Body
from fastapi import Body
from datetime import datetime
import re
from typing import Union
from re import search
from sqlalchemy.orm import Session
import models



app=FastAPI()
@app.get('/') # احتمالا این تابع باید حذف شود 
def chacknumbers(STID:str):
    if len(STID)!=11 or STID.isdigit()==False:
        raise HTTPException(detail='شماره دانشجویی باید 11 رقم باید . تعداد ارقام وارد شده درست نمی باشد.',status_code=400)
    elif int(STID[0:3]) not in range(400,403):
        raise HTTPException(detail='قسمت سال نادرست است .',status_code=400)
    elif int(STID[3:9])!=114150:
        raise HTTPException(detail='قسمت ثابت نادرست است',status_code=400)
    elif int(STID[9:]) not in range(1,100):
        raise HTTPException(detail='قسمت اندیس نادرست است .',status_code=400)
    return  f'{STID} شماره دانشجویی درست است'

@app.get('/{STID}')
def chacknumbers(STID:str):
    if len(STID)!=11 or STI.isdigit()==False:
        raise HTTPException(detail='شماره دانشجویی باید 11 رقم باید . تعداد ارقام وارد شده درست نمی باشد.',status_code=400)
    elif int(STID[0:3]) not in range(400,403):
        raise HTTPException(detail='قسمت سال نادرست است .',status_code=400)
    elif int(STID[3:9])!=114150:
        raise HTTPException(detail='قسمت ثابت نادرست است',status_code=400)
    elif int(STID[9:]) not in range(1,100):
        raise HTTPException(detail='قسمت اندیس نادرست است .',status_code=400)
    return  f'{STID} شماره دانشجویی درست است'

    

@app.post('/')
def checkinformacion(student : dict=Body()):
    error={}
    patern=r"^[آ-ی]+S"
    patern2=r"^\d{6}-\d{2}-{آ-ی}"
    patern3=r"\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b"#post
    patern4=r"^0[0-9]{2,}[0-9]{7,}$"  #Hphon
    patern5=r"09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}" #Cphon
    patern6=r"^[0-9]{10}$" #ID

    BornCity={"آذربایجان شرقی":"تبریز","آذربایجان غربی":"ارومیه","اردبیل":"اردبیل","اصفهان":"اصفهان","البرز":"کرج","ایلام":"ایلام","بوشهر":"بندر بوشهر",
    "تهران":"تهران","چهار محال و بختیاری":"شهرکر","خراسان جنوبی":"بیرجند","خراسان رضوی":"مشهد","خراسان شمالی":"یجنورد","خوزستان":"اهواز",
    "زنجان":"زنجان","سمنان":"سمنان","سیستان و بلوچستان":"زاهدان","فارس":"شیراز","قزوین":"قزوین","قم":"قم","کردستان":"سنندج","کرمان":"کرمان",
    "کرمانشاه":"کرمانشاه","کهکلویه و بویر احمد":"یاسوج","گلستان":"گرگان","گیلان":"رشت","لرستان":"خرم آباد","مازندران":"ساری","مرکزی":"اراک",
    "هرمزگان":"بندرعباس","همدان":"همدان","یزد":"یزد"}

    department=["فنی و مهندسی","علوم انسانی","اقتصاد","علوم پایه","دامپزشکی","کشاورزی","منابع طبیعی"]
    Mojor=["مهندسی کامپیوتر","مهندسی برق","مهندسی مکانیک","مهندسی عمران","مهندسی معدن","مهندسی هوافضا","مهندسی شیمی","مهندسی پزشکی",
    "مهندسی نرم افزار"]
    Marride=["مجرد","متاهل"]

    birthday=datetime.strptime
    student=["birthday"],'%Y-%m-%d'
    
    if len(student['ّFname','Lname','Fathername'])>10:
        error ['ّFname','Lname','Fathername']='حداکثر طول کاراکتر 10 می باشد'
    elif re.fullmatch(patern,student['ّFname','Lname','Fathername'])==None:
       error['ّFname','Lname','Fathername']="نام فقط حروف فارسی باشد"
    elif Union.int(patern,student['ّFname','Lname','Fathername'])==None:
        error['ّFname','Lname','Fathername']="نام نباید عدد باشد "

    if (birthday.year > 1402) or (birthday.month>12 and birthday.month<1) or (birthday.day>31 and birthday.day<1):
        error["birthday"]="تاریخ تولد صحیح نمی باشد "

    if re.match(patern2,student["IDS"])==None:  
        error["IDS"]="سریال شناسنامه معتبر نیست"
    
    if re.search(patern3,student["Post"])==None:  
        error["Post"]="کد پستی معتبر نیست"

    if re.search(patern4,student["Hphon"])==None:  # CHECK MACH OR SEARCH
        error["Hphon"]=" تلفن ثابت معتبر نیست "

    if re.search(patern5,student["Cphon"])==None:  
        error["Cphon"]="تلفن همراه معتبر نیست"

    if re.search(patern5,student["ID"])==None:  
        error["ID"]="کد ملی معتبر نیست"

    if len(student["STID"])!=11 or student["STID"].isdigit()==False:
        error['STID']="شماره دانشجویی باید 11 رقم باید . تعداد ارقام وارد شده درست نمی باشد"
    elif int(student["STID"][0:3]) not in range(400, 403):
        error['STIDr']="قسمت سال نادرست است "
    elif int(student['STID'][3:9])!=114150:
        error["STID"]="قسمت ثابت نادرست است"
    elif int(student['STID'][9:]) not in range(0,109):
        error["STID"]="قسمت اندیس نادرست است"

    if BornCity.get(student["BornCity"])==None:
        error["BornCity"]="  محل تولد شناخته شده نیست "
    elif BornCity.get(student["BornCity"])!=student["BornCity"]:
        error["BornCity"]=" محل تولد شناخته شده نیست "

    if len(student["Addres"])>100 or re.fullmatch(patern,student["Addres"])==None:
        error["Addres"]="ادرس معتبر نیست"

    if len(student["Post"])!=10 or student["Post"].isdigit()==False:
        error["Post"]="کد پستی نامعتبر"

    if len(student["Cphone"])!=11 or student["Cphon"].isdigit()==False:
        error["Cphon"]="تلفن همراه نامعتبر"
    if len(student["Hphone"])!=11 or student["Hphon"].isdigit()==False:
        error["Hphon"]="تلفن ثابت نامعتبر"
    if len(student["ID"])!=10 or student["ID"].isdigit()==False:
        error["ID"]="کدملی  نامعتبر"

#Professor
@app.get('/{LID}')
def chacknumbers(LID:str):
    if len(LID)!=6 or LID.isdigit()==False:
        raise HTTPException(detail='کد استاد باید 6 رقم باید . تعداد ارقام وارد شده درست نمی باشد.',status_code=400)

@app.post('/')
def checkinformacion(Professor : dict=Body()):
    error={}
    patern=r"^[آ-ی]+S"
    patern3=r"\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b"#post
    patern4=r"^0[0-9]{2,}[0-9]{7,}$"  #Hphon
    patern5=r"09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}" #Cphon
    patern6=r"^[0-9]{10}$" #ID

    BornCity={"آذربایجان شرقی":"تبریز","آذربایجان غربی":"ارومیه","اردبیل":"اردبیل","اصفهان":"اصفهان","البرز":"کرج","ایلام":"ایلام","بوشهر":"بندر بوشهر",
    "تهران":"تهران","چهار محال و بختیاری":"شهرکر","خراسان جنوبی":"بیرجند","خراسان رضوی":"مشهد","خراسان شمالی":"یجنورد","خوزستان":"اهواز",
    "زنجان":"زنجان","سمنان":"سمنان","سیستان و بلوچستان":"زاهدان","فارس":"شیراز","قزوین":"قزوین","قم":"قم","کردستان":"سنندج","کرمان":"کرمان",
    "کرمانشاه":"کرمانشاه","کهکلویه و بویر احمد":"یاسوج","گلستان":"گرگان","گیلان":"رشت","لرستان":"خرم آباد","مازندران":"ساری","مرکزی":"اراک",
    "هرمزگان":"بندرعباس","همدان":"همدان","یزد":"یزد"}

    department=["فنی و مهندسی","علوم انسانی","اقتصاد","علوم پایه","دامپزشکی","کشاورزی","منابع طبیعی"]
    Mojor=["مهندسی کامپیوتر","مهندسی برق","مهندسی مکانیک","مهندسی عمران","مهندسی معدن","مهندسی هوافضا","مهندسی شیمی","مهندسی پزشکی",
    "مهندسی نرم افزار"]
    Marride=["مجرد","متاهل"]
    LCourseIDs=[Course.cid]
    birthday=datetime.strptime
    Professor=["birthday"],'%Y-%m-%d' 
    
    if len(Professor['ّFname','Lname'])>10:
        error ['ّFname','Lname']='حداکثر طول کاراکتر 10 می باشد'
    elif re.fullmatch(patern,student['ّFname','Lname'])==None:
       error['ّFname','Lname']="نام فقط حروف فارسی باشد"
    elif Union.int(patern,student['ّFname','Lname'])==None:
        error['ّFname','Lname']="نام نباید عدد باشد "

    if (birthday.year > 1402) or (birthday.month>12 and birthday.month<1) or (birthday.day>31 and birthday.day<1):
        error["birthday"]="تاریخ تولد صحیح نمی باشد "

    if re.search(patern3,Professor["Post"])==None:  
        error["Post"]="کد پستی معتبر نیست"

    if re.search(patern4,Professor["Hphon"])==None:  # CHECK MACH OR SEARCH
        error["Hphon"]=" تلفن ثابت معتبر نیست "

    if re.search(patern5,Professor["Cphon"])==None:  
        error["Cphon"]="تلفن همراه معتبر نیست"

    if re.search(patern5,Professor["ID"])==None:  
        error["ID"]="کد ملی معتبر نیست"

    if len(Professor["LID"])!=11 or Professor["LID"].isdigit()==False:
        error['LID']="کد استاد باید 6 رقم باید . تعداد ارقام وارد شده درست نمی باشد"

    if BornCity.get(Professor["BornCity"])==None:
        error["BornCity"]="  محل تولد شناخته شده نیست "
    elif BornCity.get(Professor["BornCity"])!=Professor["BornCity"]:
        error["BornCity"]=" محل تولد شناخته شده نیست "

    if len(Professor["Addres"])>100 or re.fullmatch(patern,Professor["Addres"])==None:
        error["Addres"]="ادرس معتبر نیست"

    if len(Professor["Post"])!=10 or Professor["Post"].isdigit()==False:
        error["Post"]="کد پستی نامعتبر"

    if len(Professor["Cphone"])!=11 or Professor["Cphon"].isdigit()==False:
        error["Cphon"]="تلفن همراه نامعتبر"
    if len(Professor["Hphone"])!=11 or Professor["Hphon"].isdigit()==False:
        error["Hphon"]="تلفن ثابت نامعتبر"
    if len(Professor["ID"])!=10 or Professor["ID"].isdigit()==False:
        error["ID"]="کدملی  نامعتبر"



# course
def chacknumbers(cid:str):
    if len(cid)!=5 or cid.isdigit()==False:
        raise HTTPException(detail='کد درس باید 5 رقم باید . تعداد ارقام وارد شده درست نمی باشد.',status_code=400)

@app.post('/')
def checkinformacion(Course : dict=Body()):
    error={}
    patern=r"^[آ-ی]+S"
    patern0=r"\d[1-4]" #Credit


    if len(Course['ّcname'])>25:
        error ['ّcname']='حداکثر طول کاراکتر 25 می باشد'
    elif re.fullmatch(patern,Course['ّcname'])==None:
       error['ّcname']="نام درس فقط حروف فارسی باشد"
    elif Union.int(patern,Course['ّcname'])==None:
        error['ّcname']="نام درس نباید عدد باشد "

    department=["فنی و مهندسی","علوم انسانی","اقتصاد","علوم پایه","دامپزشکی","کشاورزی","منابع طبیعی"]

    if len(Course["credit"])!=1 or Course["redit"].isdigit()==False:
        error["redit"]="تعداد واحد  نامعتبر"