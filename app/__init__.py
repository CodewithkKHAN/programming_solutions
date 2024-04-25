from flask import Flask, render_template,request
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///codes.db"
db=SQLAlchemy(app)
path=r"app\python_codes"
def create_db():
    with app.app_context():

        db.create_all()

class code(db.Model):
        __tablename__="python_code"
        id=db.Column(db.Integer,primary_key=True,autoincrement=True)
        name=db.Column(db.String,unique=True)
        def __repr__(self):
            return '<python_code %r>' % self.id
# Define routes
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/checkfun',methods=["POST","GET"])
def checkfun():
    # keyword="matrix"
    # with open(path+"\\"+"titles.txt",'r',newline="\n") as t:
    #     list_titles_raw=t.readlines()
    # list_titles=[]
    # for line in list_titles_raw:
    #     list_titles.append(line.strip('\r\n'))
    # title_dict={}
    # for i in list_titles:
    #     item=i.split("$$$")
    #     title_dict[item[-1]]=item[0]
    # # print(title_dict)
    # results_dict={}
    # for k,v in title_dict.items():
    #     if keyword.lower() in v.lower():
    #         results_dict[k]=v
    # print(results_dict)
    # # print(list_titles_raw)
    # # print(list_titles)
    # with app.app_context():
    #      pass
        # user = code(name="item["name"]")
        # db.session.add(user)
        # db.session.commit()
        # codes=code.query.all()
        # specific_users = code.query.filter_by(name="sund").all()
        # suffix_of_file=specific_users[0].id
        # name_of_file=f"py{suffix_of_file}.py)"
        # print(name_of_file)
        # return specific_users

    # item=request.form["item"]
    # return item
       
#     # item=request.form
#     # with open("py1.py","r") as p:
        
#         # title=p.readline()
#         # text=p.read()
#         # t1=text.split("\n")
#         # t2=repr(t1)
#         # text.split()
#     #     highlighted_code = highlight(text, PythonLexer(), HtmlFormatter())
#     # return render_template('pythonresults.html'
#     #                        ,highlighted_code=highlighted_code,
#     #                        title=title,
#     #                        item=item)
    k=request.args.get("key1")
    # return k
    return render_template("pythonresults.html")
@app.route("/pythonresults",methods=["POST","GET"])
def pythonresults():
    k=request.args.get("key1")
    fname="app\\python_codes\\"+k
    with open(fname,"r") as p:
        
        title=p.readline()
        text=p.read()
        # t1=text.split("\n")
        # t2=repr(t1)
        # text.split()
        highlighted_code = highlight(text, PythonLexer(), HtmlFormatter())
    return render_template('pythonresults.html'
                           ,highlighted_code=highlighted_code,
                           title=title,
                           )
@app.route('/formtodata',methods=["POST","GET"])
def formtodata():
   
    item=request.form
    
    with app.app_context():

        user = code(name=item["name"])
        db.session.add(user)
        db.session.commit()
        # codes=code.query.all()
        specific_users = code.query.filter_by(name=item["name"]).all()
        suffix_of_file=specific_users[0].id
        name_of_file=f"py{suffix_of_file}.py"
        print(name_of_file)
    title=item['title']
    pcode=item['code']
    fname=path+"\\"+name_of_file
    with open(path+"\\"+"titles.txt",'a') as t:
        t.write(f"# {title}$$${name_of_file}\n")
    
    with open(fname,'w', newline="") as writer:
        writer.write("#"+title+"\n")
        writer.writelines(pcode)
    return f"{name_of_file},{title},{pcode}"
    # with open("py"+)
    # return render_template("addcode.html")
@app.route('/addcode')
def addcode():
    return render_template("addcode.html")

@app.route("/see_results",methods=["POST","GET"])
def see_results():
    keyword=request.form['item']
    with open(path+"\\"+"titles.txt",'r',newline="\n") as t:
        list_titles_raw=t.readlines()
    list_titles=[]
    for line in list_titles_raw:
        list_titles.append(line.strip('\r\n'))
    title_dict={}
    for i in list_titles:
        item=i.split("$$$")
        title_dict[item[-1]]=item[0]
    # print(title_dict)
    results_dict={}
    for k,v in title_dict.items():
        if keyword.lower() in v.lower():
            results_dict[k]=v
    return render_template("results.html",results=results_dict)
def delete_all_users():
    with app.app_context():
        try:
            db.session.query(code).delete()
            db.session.commit()
            return "All users have been deleted."
        except Exception as e:
            db.session.rollback()
            return f"Error deleting users: {str(e)}"
@app.route('/python')
def python_solutions():
    # Retrieve and display Python solutions
    return render_template('python.html')

@app.route('/javascript')
def javascript_solutions():
    # Retrieve and display JavaScript solutions
    return render_template('javascript.html')

# Add more routes for other programming languages
# create_db()
if __name__ == '__main__':
    app.run(debug=True)
# checkfun()
# delete_all_users()