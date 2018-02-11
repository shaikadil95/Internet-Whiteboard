from flask import Flask, request, jsonify
#from flask.ext.mysql import MySQL

#mysql = MySQL()
app = Flask(__name__)


import pymysql

global ip
ip = "193.11.186.133"

@app.route('/getmoderator')



def getmoderator():
    connecttodb = pymysql.connect(host=ip, port=3306, user='sneha', passwd='sneha', db='Paint')
    cursor = connecttodb.cursor()
    
    cursor.execute("""select username from login1 where moderator=%s""",["TRUE"])
    moderator_name=cursor.fetchall()
    connecttodb.commit()
    connecttodb.close()

    return str(moderator_name)




@app.route('/getlock')

def getlock():
    name = request.args.get('name')
    connecttodb = pymysql.connect(host=ip, port=3306, user='sneha', passwd='sneha', db='Paint')
    cursor = connecttodb.cursor()
        
    cursor.execute("""select lok_flag from login1 where moderator = "FALSE" and username=%s""",[name]
                                               )
        
    xx=cursor.fetchone()
    print(xx)
    
    connecttodb.commit()
        
    connecttodb.close()
    if xx==('FALSE',):
        lock="FALSE"
    else:
        lock = "TRUE"
    print(lock)
 
    return lock


    
    


if __name__ == '__main__':
    app.run(host=ip)
