from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
app = FastAPI()
templates = Jinja2Templates(directory='templates/')
from  sklearn import  datasets
iris=datasets.load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
from sklearn import tree
classifier=tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)
from sklearn.metrics import accuracy_score
@app.get('/')
def read_form():
    return 'hello world'
@app.get('/test')
def form_post(request: Request):
    result = 'Please Enter a Numbers'
    return templates.TemplateResponse('test.html', context={'request': request, 'result': result})
@app.post('/test')
def form_post(request: Request, num1: float = Form(...),num2: float = Form(...),num3: float = Form(...),num4: float = Form(...)):
    result=classifier.predict([[num1,num2,num3,num4]])
    if result == 0:
        res1 = 'Versicolor'
    elif result == 1:
        res1 = 'Setosa'
    else:
        res1 = 'Virginica'
    return templates.TemplateResponse('test.html', context={'request': request, 'result': res1, 'num1': num1,'num2': num2,'num3': num3,'num4': num4})

