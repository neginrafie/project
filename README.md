
بسم الله الرحمن الرحیم
گزارش پروژه پایانی

نگین رفیعی (40211415038)









در مرحله اول یک پگیج به اسم
 sql_app
میسازیم و ماژول های زیر را در ان ایجاد میکنیم


init.py
Schemas.py
Database.py
Router
Main.py
Models.py
Validation.py
Crud.py















__init__.py
 

این ماژول خالی است و برای تشکیل یک پکیج ایجاد میشود


database.py
 
در این ماژول ادرس دیتا بیس مشخص میشود در خط اول
Create_engin 
را ایمپورت میکنیم و به کمک ان در خط هشتم 
Engine 
را میسازیم و ان را به ادرس دیتا بیس متصل میکنیم
در خط دوم 
Declaractive_base 
را ایمپورت میکنیم و در خط یازدهم از ان یک شی میسازیم تمام کلاس هایی که این شی را به ارث ببرند در ادرس ذکر شده در دیتا بیس به عنوان یک جدول شناسایی میشوند


Models.py

 

این ماژول محل ساختن جداول دیتا بیس است
در این ماژول یک سری کلاس ایجاد میشوند که همگی 
Base(obj of declaractive_base)
را به ارث میبرند دارای نام و ستون هستند 
هر خط از این جدول یک ستون را در جدول دیتا بیس تشکیل میشود

Schsmas.py
 

در این ماژول نوع دیتا های ورودی بررسی میشود 
تمام کلاس ها در این ماژول از 
Basemodel 
ارث بری میکنند


Crud.py
 
در این ماژول توابعی برای ساخت جداول حذف اپدیت کردن و خواندن اطلاعات برای هر سه جدول مورد نظر ساخته شده است




Dependencies.py

در این ماژول تنها یک تابع وجود دارد که تمام 
db 
ها به ان بستگی دارند و وابسته هستند
در این تابع ابتدا یک متغییر به نام 
db 
ساخته میشود یک 
Session 
است
هنگام اجرا شدن 
db 
رابرمیگرداند و در نهایت ان را میبندد

 


Router

یک پکیج با نام 
Router
ایجاد میکنیم 
و ماژول های زیر را در ان ایجاد میکنیم
__init__.py
Student.py
Course.py
Professor.py




course.py

ابتدا 
Apirouter 
را از 
Fastapi
ایمپورت میکنیم و از ان یک شی میسازیم

 

با استفاده از شی ساخته شده و به کمک متود 
Post 
یک 
URL
تعریف میکنیم و به کمک 
Response_model
از تابع میخواهیم که در پایان جدول ساخته شده را به کاربر برگرداند
تابعی تعریف میکنیم که در ان بتوانیم اطلاعات را در جدول ایجاد کنیم
این تابع دو ارگومان ورودی دارد
Course and db
که به ترتیب مدل پایدانتیکی و 
Session 
هستند
بعد از ان تابعی که برای اعتبار سنجی در 
ماژول 
Validation 
را فراخوانی میکنیم و مقدار ارگومان ورودی انرا با مدل پایدانتیکی ارسال شده توسط کاربر برابر قرار میدهیم
یک متغییر میسازیم و به کمک ان تابع 
Get_course
در ماژول 
Crud 
را فراخوانی میکنیم وارگومان های ورودی انرا با مقدار هایی که کاربر ارسال کرده برابر قرار میدهیم
این بخش از تابع بررسی میکند که ایا هیچ رکوردی از پیش با 
Id 
وارد شده در جدول موجود است یا خیر در صورت وجود ارور میدهد
در غیر این صورت تابع 
Create_course 
را ازهمان ماژول فرا خوانی میکند و ارگومان های ان را با مقادیر ارسال شده توسط کاربر برابر قرار میدهد و رکورد جدید میسازد
مراحل ذکر شده را در ماژول های 
Student and teacher 
برای جدول های دانشجو و استاد تکرار میکنیم

 با استفاده از شی ساخته شده با کمک متود 
Get 
یک 
URL
جدید تعریف میکنیم و در ان یک 
Id 
به عنوان 
Pathparameter
تعریف میکنیم و 
Response_model 
راهم مدل پایدانتیکی موجود در جدول قرار میدهیم
تابعی برای خواندن اطلاعات تعریف میکنیم کهدو ارگومان ورودی دارد 
Id and db
یک متغییر تعریف میکنیم به نام 
Db_course 
و به کمک ان تابع 
Get_course 
در ماژول 
Crud 
را فراخوانی میکنیم و ارگومان انرا با id ارسال شده به عنوان پارامتر مسیر برابر قرار میدهیم و اگر چیزی برنگرداند ارور برمیگردانیم 
این بخش از تابع به دنبال یک رکورد در جدول با 
Id
وارد شده توسط کاربر به عنوان پارامتر مسیر میگردد و در صورت عدم وجود ارور میدهد
در غیر این صورت تابع را مقدار دهی میکند و در متغییر قرار میدهد و انرا برمیگرداند

مراحل ذکر شده را در ماژول های 
Student and teacher 
برای جدول های دانشجو و استاد تکرار میکنیم
 
با استفاده از شی ساخته شده و به کمک متود 
Delete
یک 
URL
جدید تعریف میکنیم و در ان 
Id
را به عنوان پارامتر مسیر در نظر میگیریم
یک تابع با نام
Update_course
برای به روز رسانی درس میسازیم و برای ان دو ارگومان ورودی 
id ,db 
در نظر میگیریم
یک متغیر به نام 
Get_db
تعریف میکنیم و در ان تابع 
Get_course 
را در ماژول 
Crud 
فراخوانی میکنیم و ارگومان های ورودی ان را با 
Id and db
ارسال شده مقدار دهی میکنیم این قسمت چک میکند که ایاهیچ رکوردی با ایدی وارد شده در جدول وجود دارد یا خیر اگر وجود نداشت ارور میدهد 
درغیر این صورت تابع 
Delete_course
را در ماژول 
Crud 
فراخوانی میکند و ارگومان های ورودی ان را با
Id and db 
ارسال شده مقدار دهی میکند و انرا حذف میکند 
سپس پیغام "درس حذف شد " را به کاربر برمیگرداند
مراحل قبل را در ماژول های 
Teacher , student
برای جداول دانشجو و استاد تکرار میکنیم
 
با استفاده از شی ساخته شده و به کمک متود 
Put 
یک 
URL 
جدید تعریف میکنیم و به عنوان یک پارامتر مسیر 
Id 
را تعریف میکنیم
سپس یک تابع برای به روزرسانی اطلاعات تعریف میکنیم که سه ارگومان ورودی دارد 
Course and int and db
که 
Course 
در اینجا یک مدل پایدانتیکی است یک متغیر به نام
Get_db
تعریف میکنیم که در ان تابع 
Get_course 
در ماژول 
Crud 
فراخوانی میشود و ارگومان های ورودی ان مقدار دهی میشود
اگه این تابع مقدار 
None 
برگرداند و رکوردی با ایدی وارد شده به عنوان پارامتر مسیر پیدا نکرد ارور میدهد
در خط بعدی یک شرط جدید تعریف میکنیم که اگر 
Id 
وارد شده به عنوان پارامتر مسیر و 
Cid
در مدل پایدانتیکی ارسال شده برابر نبودند 
تابع قبلی در ماژول 
Crud 
دوباره فراخوانی میشود ولی اینبار به دنبال رکوردی میگردد که با 
Cid 
وارد شده 
Id 
یکسانی داشته باشد چرا که رکورد ها با این ایتم شمارش شده و باید یکتا باشند 
اگر موردی یافت شد به معنای تکراری بودن رکورد است درنتیجه باید ارور به کاربر نمایش داده شود 
در غیر این صورت مدل پایدانتیکی ارسال شده باید اعتبار سنجی شود 
اینکار با فراخوانی تابع 
Checkcourse
در ماژول 
Validation 
انجام میشود و ارگومان ورودی انرا با مدل پایدانتیکی ارسال شده برابر قرار میدهیم و انرا اعتبار سنجی میکنیم بعد از ان تابع 
Update_course 
در ماژول 
Crud 
را فراخوانی میکنیم و انرا مقدار دهی میکنیم سپش پیام "به روز رسانی درس موفقیت امیز بود "را به کاربر نمایش میدهیم
مراحل انجام شده را برای ماژول های 
Student and teacher
برای جداول دانشجو و استاد تکرار میکنیم


Validation.py
اعتبار سنجی مقادیر ارسال شده توسط کاربر در این ماژول انجام میشود
توابع استفاده شده در روتر ها را در این ماژول میسازیم و مقادیر ارسال شده برای سه جدول را به صورت جدا گانه در سه تابع مختلف


Docerfile:
FROM   python:latest

WORKDIR /src


COPY ./requrements.txt/src


RUN pip install -r requrements.txt

COPY . .

CMD ["uvicorn","main.py:app","--host","8000"]


در نهایت ماژول داکر فایل را ایجاد میکنیم و در ان دستورات زیر را مینویسیم
این دستورات ابتدا 
Base image 
را نسخه 
Latest
از پایتون در نظر میگیرد 
سپس دایرکتوری ذکر شاده را میسازد و وارد ان میشود کل ماژول 
Requrement.txt 
را در دایرکتور کپی میکند 
این ماژول حاوی تمام نیازمندی های برنامه است
به کمک 
Run 
دستور ذکر شده را اجرا میکند
دیرکتوری فعلی را در دایرکتوری ساخته شده ذخیره میکند و در نهایت خط اخر اجرا میشود




  

در پایان فایل ها را مرتب و روتر میکنیم 
