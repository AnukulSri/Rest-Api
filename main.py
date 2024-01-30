# import pymysql as pm
from app import app
from config import mysql
from flask import jsonify
from flask import flash,request

@app.route('/create',methods=['POST'])
def create_emp():
    try:
        jsn = request.json
        n = jsn['name']
        em = jsn['email']
        ph = jsn['phone']
        ad= jsn['address']

        if n and em and ph and ad and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            query = 'Insert into employee(name,email,phone,address) Values(%s,%s,%s,%s)'
            bind_data = (n,em,ph,ad)
            cursor.execute(query,bind_data)
            conn.commit()
            response = jsonify('Employee Added Successfully')
            response.status_code = 200
            return response
        else:
            return show_Message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/emp')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('Select id, name, email, phone, address from employee')
        extract_row = cursor.fetchall()

        payload = []
        content = {}
        for result in extract_row:
            content = {'id': result[0], 'name': result[1], 'email': result[2],'phone': result[3],'address': result[4]}
            payload.append(content)
            content = {}
        
        response =  jsonify(payload)
        response.status_code = 200

        # response = jsonify(extract_row)
        return response
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

@app.route(' ')
def emp_detail(emp_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('Select * from employee where id=%s',emp_id)
        emp_row = cursor.fetchone()
        content = {}
        content = {'id': emp_row[0], 'name': emp_row[1], 'email': emp_row[2],'phone': emp_row[3],'address': emp_row[4]}
        response = jsonify(content)
        response.status_code = 200

        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update',methods=['PUT'])
def update_emp():
    try:
        jsn = request.json
        idd = jsn['id']
        n = jsn['name']
        em = jsn['email']
        ph = jsn['phone']
        ad = jsn['address']

        if n and em and ph and ad and idd and request.method == 'PUT':
            query = 'Update employee SET name = %s, email= %s, phone= %s, address=%s WHERE id = %s'
            bind_data = (n,em,ph,ad,idd)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(query,bind_data)
            conn.commit()
            response = jsonify('Employee updated Successfully')
            response.status_code = 200
            return response
        else:
            return show_Message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.commit()

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete_emp(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('Delete from employee where id = %s',(id,))
        conn.commit()
        response = jsonify("Employee deleted Successfully")
        response.status_code = 200
        return response
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def show_Message(error=None):
    message = {
        'status':404,
        'message':'Record not found: '+ request.url,
    }

    response = jsonify(message)
    response.status_code = 404
    return response




# class 



if __name__ == '__main__': # checking for main function
   app.run() # this is to run the Flask program
