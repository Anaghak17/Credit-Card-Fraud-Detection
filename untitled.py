import random

from flask import Flask, render_template, request, redirect,session
import datetime
from DBConnection import Db

app = Flask(__name__)
app.secret_key="lll"

@app.route('/',methods=['get','post'])
def login():
    db=Db()
    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        res=db.selectOne("select * from login WHERE username='"+username+"' and password='"+password+"'")
        if res is not None:
            session['lid']=res['lid']
            if res['usertype']=='admin':
                session['lg']="lin"
                return redirect('/adminhome')
            elif res['usertype'] == 'dealer':
                session['lg'] = "lin"
                return redirect('/dealerhome')
            elif res['usertype'] == 'user':
                session['lg'] = "lin"
                return redirect('/userhome')

            else:
                return '''<script>alert('user not found');window.location="/"</script>'''
        else:
            return '''<script>alert('user not found');window.location="/"</script>'''

    else:
         return render_template('loginindex.html',)

@app.route('/adminhome')
def adminhome():
    if session['lg']=="lin":
        return render_template("Admin/adminindex.html")
    else:
        return  redirect('/')

@app.route('/dealer_management',methods=['get','post'])
def dealer_management():
    if session['lg'] == "lin":
        db=Db()
        if request.method=="POST":
            name=request.form['textfield']
            shopname=request.form['textfield2']
            place=request.form['textfield3']
            district=request.form['select']
            phone=request.form['textfield5']
            password=random.randint(0000,9999)
            res=db.insert("insert into login VALUES ('','"+name+"','"+str(password)+"','dealer')")
            db.insert("insert into dealer VALUES ('"+str(res)+"','"+name+"','"+shopname+"','"+place+"','"+district+"','"+phone+"')")
            return '''<script>alert('Added Successfully');window.location="/adminhome"</script>'''
        else:
            return render_template('Admin/Dealer Management.html')
    else:
        return redirect('/')


@app.route('/feedback')
def  feedback():
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from feedback,user where feedback.uid=user.uid")
        return render_template('Admin/feedback.html',data=res)
    else:
        return redirect('/')
@app.route('/view_dealer')
def view_dealer():
    if session['lg'] == "lin":
        db = Db()
        res = db.select("select * from dealer")
        return render_template('Admin/view Dealer.html', data = res)
    else:
        return  redirect('/')


@app.route('/delete_dealer/<did>')
def deletedealer(did):
    if session['lg'] == "lin":
        db=Db()
        db.delete("delete from dealer where did='"+did+"'")
        return '''<script>alert('delete successful');window.location="/view_dealer"</script>'''
    else:
        return redirect('/')
@app.route('/edit_dealer/<did>',methods=['get','post'])
def editdealer(did):
    if session['lg'] == "lin":
        db=Db()
        if request.method=="POST":
            name=request.form['textfield']
            shopname=request.form['textfield2']
            place=request.form['textfield3']
            district=request.form['select']
            phone=request.form['textfield5']
            db=Db()
            db.update("update dealer set dealer='"+name+"',shope='"+shopname+"',place='"+place+"',district='"+district+"',phone='"+phone+"' where did='"+did+"'")

            return '''<script>alert('Update successful');window.location="/view_dealer"</script>'''
        else:
            res=db.selectOne("select * from dealer WHERE  did='"+did+"'")
        return render_template('Admin/editdealer.html',data=res)
    else:
        return redirect('/')

@app.route('/add_user', methods=['get', 'post'])
def add_user():
    if session['lg'] == "lin":
        db = Db()
        if request.method == "POST":
            username = request.form['textfield']
            password = request.form['textfield2']
            res = db.insert("insert into user VALUES ('" + username + "','" + password + "'")
            return '''<script>alert('Added Successfully');window.location="/adminhome"</script>'''
    else:
        return redirect('/')

@app.route('/view_user')
def view_user():
    if session['lg'] == "lin":
        db = Db();
        res = db.select("select * from user")
        return render_template('Admin/view user.html', data=res)
    else:
        return redirect('/')
# ------------------------------------------------------------------------------------------------------
@app.route('/dealerhome')
def dealerhome():
    if session['lg']=="lin":
        return render_template("Dealer/dealerindex.html")
    else:
        return redirect('/')

@app.route('/add_product',methods=['get','post'])
def  add_product():
    if session['lg'] == "lin":
        db=Db()
        if request.method=="POST":
            category=request.form['select']
            productname=request.form['textfield']
            price=request.form['textfield2']
            stock=request.form['textfield3']
            image=request.files['fileField']
            date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            image.save(r"C:\Users\ANAGHA\PycharmProjects\untitled\static\pic\\"+date+'.jpg')
            ss="/static/pic/"+date+'.jpg'
            res=db.insert("insert into product VALUES ('','"+category+"','"+productname+"','"+price+"','"+stock+"','"+str(ss)+"','"+str(session['lid'])+"')")
            return  '''<script>alert('Added Successfully');window.location="/dealerhome"</script>'''
        else:
            return render_template('Dealer/Add product.html')
    else:
        return redirect('/')

@app.route('/change_product/<pid>',methods=['get','post'])
def  change_product(pid):
    if session['lg'] == "lin":
        db=Db()
        if request.method=="POST":
            category=request.form['select']
            productname=request.form['textfield']
            price=request.form['textfield2']
            stock=request.form['textfield3']
            image=request.files['fileField']
            date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            image.save(r"C:\Users\ANAGHA\PycharmProjects\untitled\static\pic\\"+date+'.jpg')
            ss="/static/pic/"+date+'.jpg'
            if request.files!='None':
                if image.filename!="":

                    db.update("update product set category='"+category+"',pname='"+productname+"',price='"+price+"',stock='"+stock+"',image='"+ss+"' where pid='"+pid+"'")
                    return '''<script>alert('Updated Successfully');window.location="/view_product"</script>'''
                else:
                    db.update(
                        "update product set category='" + category + "',pname='" + productname + "',price='" + price + "',stock='" + stock + "'where pid='" + pid + "'")
                    return '''<script>alert('Updated Successfully');window.location="/view_product"</script>'''
            else:
                db.update(
                    "update product set category='" + category + "',pname='" + productname + "',price='" + price + "',stock='" + stock + "'where pid='" + pid + "'")
                return '''<script>alert('Updated Successfully');window.location="/view_product"</script>'''

        ss=db.selectOne("select * from product where pid='"+pid+"'")
        return render_template('Dealer/Change product.html',data=ss)
    else:
         return redirect('/')

@app.route('/delete_product/<pid>')
def deleteproduct(pid):
    if session['lg'] == "lin":
            db=Db()
            db.delete("delete from product where pid='"+pid+"'")
            return '''<script>alert('delete successful');window.location="/view_product"</script>'''
    else:
        return redirect('/')

@app.route('/view_complaint')
def  view_complaint():
    if session['lg'] == "lin":
        db = Db();
        res= db.select("select * from complaint,product,user where complaint.userid=user.uid and complaint.pid=product.pid and product.did='"+str(session['lid'])+"'")
        print(res)
        return render_template('Dealer/View Complaint.html',data = res)
    else:
        return redirect('/')
@app.route('/send_replay/<ulid>',methods=['get','post'])
def  send_replay(ulid):
    if session['lg'] == "lin":
        if request.method=='POST':
                c=request.form['textarea']
                db=Db()
                db.update("update complaint set reply='"+c+"',replydate=curdate() where cmid='"+ulid+"'")
                return redirect('/view_complaint')
        return render_template('Dealer/Complaint Reply.html')
    else:
        return redirect('/')
@app.route('/view_product')
def  view_product():
    if session['lg'] == "lin":
        db = Db();
        res=db.select("select * from product where did='"+str(session['lid'])+"'")
        print(res)
        return render_template('Dealer/View Product.html',data = res)
    else:
        return redirect('/')

@app.route('/view_stock')
def  view_stock():
    if session['lg'] == "lin":
        db = Db();
        res=db.select("select * from product where did='"+str(session['lid'])+"'")
        print(res)
        return render_template('Dealer/View Stock.html',data = res)
    else:
        return redirect('/')


# ////////////////////////////////////////////////////////////////USER//////////////////////////////////////////////





@app.route('/userhome')
def userhome():
    if session['lg']=="lin":
        return render_template("User/userindex.html")
    else:
        return redirect('/')

@app.route('/user_registration', methods=['get', 'post'])
def user_registration():
    db = Db()
    if request.method == "POST":

        name = request.form['textfield2']
        housename=request.form['textfield6']
        place=request.form['textfield3']
        post=request.form['textfield4']
        district=request.form['select']
        email=request.form['textfield']
        phone=request.form['textfield7']
        password=request.form['textfield5']
        res = db.insert("insert into login VALUES ('','" + email + "','" + str(password) + "','user')")
        db.insert("insert into user VALUES('"+str(res)+"','" + name + "','" + housename + "','"+ place + "','"+ post +"','"+ district +"','"+phone+"')")

        return '''<script>alert('Registered successful');window.location="/"</script>'''
    else:

        return render_template('User/User Registration.html')



@app.route('/user_view_products')
def user_view_products():
    if session['lg'] == "lin":
         db=Db()
         res = db.select("select * from product,dealer where product.did=dealer.did ")
         return render_template('User/user_View_Product.html',data=res)
    else:
        return redirect('/')


@app.route('/add_to_cart/<p>',methods=['get','post'])
def add_to_cart(p):
    if session['lg'] == "lin":
         if request.method=="POST":
             quantity=request.form['textfield']
             db=Db()
             ss=db.selectOne("select * from booking where userid='"+str(session['lid'])+"' and status='add_to_cart'")
             if ss is None:
                b= db.insert("insert into booking VALUES('','"+str(session ['lid'])+"','add_to_cart','pending','0')")
                db.insert("insert into cart VALUES ('','"+p+"','"+str(b)+"','"+quantity+"')")
                return redirect('/viewcart')
             else:
                 q3=db.selectOne("select * from cart WHERE pid='"+str(p)+"' and bid='"+str(ss['bid'])+"'")
                 if q3 is None:
                     db.insert("insert into cart VALUES('','"+p+"','"+str(ss['bid'])+"','"+quantity+"')")

                 else:
                     db.update("update cart set quantity=quantity+'"+quantity+"' where cartid='"+str(q3['cartid'])+"'")
                 return redirect('/viewcart')
         else:
             return render_template('User/quantity.html')
    else:
        return redirect('/')

@app.route('/payment_mode',methods=['get','post'])
def payment_mode():
    # if session['lg'] == "lin":
    if request.method=="POST":
        mode=request.form['RadioGroup1']
        db=Db()
        if mode=='Offline':
            db.update("update booking set payment_methods='offline' WHERE booking.userid='" + str(session['lid']) + "' and payment_methods='pending'")
            return "updated"
        elif mode=='Online':
            return redirect('/bookingpayment')
    else:

            return render_template('User/payment mode.html')
    # else:
    #     return redirect('/')


@app.route('/bookingpayment',methods=['get','post'])
def bookingpaymen():
    if session['lg'] == "lin":
        db=Db()
        q2 = db.selectOne(
            "select sum(quantity*price) as s,booking.bid from cart,booking,product where booking.bid=cart.bid and userid='" + str(
                session[
                    'lid']) + "' and product.pid=cart.pid and booking.status='booked' and payment_methods='pending'")

        if request.method=="POST":
            cardnumber=request.form['textfield']
            CVV=request.form['textfield2']
            Expirydate=request.form['textfield3']
            Holdername=request.form['textfield4']
            Amount=request.form['textfield5']
            db=Db()
            q=db.selectOne("select * from card where uid='"+str(session['lid'])+"' and card_no='"+cardnumber+"' and cvv='"+CVV+"' and expiry='"+Expirydate+"' and holder='"+Holdername+"'")
            print("select * from card where uid='"+str(session['lid'])+"' and card_no='"+cardnumber+" ' and cvv='"+CVV+"' and expiry='"+Expirydate+" ' and holder=' "+Holdername+"'")
            if q is not None:
                if int(Amount)<=int(q['amount']):
                    bal=q['amount']
                    db=Db()
                    tobs=db.select("SELECT `transaction`.*, booking.amount  FROM `transaction` JOIN booking ON booking.bid=`transaction`.bill_id where booking.`userid`='"+str(session['lid'])+"'")
                    print("Totttt   ", len(tobs))
                    resamount=[]
                    if len(tobs) != 0:
                        for i in tobs:
                            print("i", i['date'])
                            print("f")
                            if i['finished'] == "success":
                                resamount.append(["0", i['amount']])
                                print("hello")
                    print("resamt", resamount)
                    resamount.append(["0", bal])
                    print("location")
                    resloc = outlier(resamount)
                    resll = resloc[len(resloc) - 1]
                    print("resl1", resll)
                    if resll != -1:
                        db=Db()
                        db.update("update card set amount=amount-'"+Amount+"' where cid='"+str(q['cid'])+"'")
                        db.update("update booking set payment_methods='Online' where bid='"+str(q2['bid'])+"'")
                        db.insert("insert into transaction values(null, '1', curdate(), curtime(), 'success')")
                        return '''<script>alert('Booked Successfully');window.location="/mybooking"</script>'''
                    else:
                        print("Fake detected")
                        db=Db()
                        db.insert("insert into transaction values(null, '1', curdate(), curtime(), 'fake')")
                        return '''<script>alert('Booked Successfully');window.location="/mybooking"</script>'''

                else:
                    return render_template('User/Bookingpayment.html', d1="Insufficient balance!!!",d=q2['s'])
            else:
                return '''<script>alert('Invalid');window.location="/bookingpayment"</script>'''
        db=Db()
        return render_template('User/Bookingpayment.html',d=q2['s'])
    else:
        return redirect('/')





@app.route('/add_carddetails',methods=['get','post'])
def add_carddetails():
    if session['lg'] == "lin":
        if request.method=="POST":
            cardnumber = request.form['textfield']
            cvv = request.form['textfield2']
            expirydate = request.form['textfield3']
            holdername = request.form['textfield4']

            db = Db()
            db.insert("insert into card VALUES('' ,'"+ str(session['lid'])+"' ,'" + cardnumber + "','" + cvv + "','" + expirydate + "','" + holdername + "','"+str(random.randint(00000,99999))+"')")
        return render_template('User/Add card details.html')
    else:
        return redirect('/')

@app.route('/add_complaint/<p>',methods=['get','post'])
def add_complaint(p):
    if session['lg'] == "lin":
        if request.method=="POST":
            complaint=request.form['textarea']
            db=Db()
            db.insert("insert into complaint values ('','"+str(session['lid'])+"','"+complaint+"',curdate(),'"+str(p)+"','pending','pending')")
            return '''<script>alert('Added Successfully');window.location="/userhome"</script>'''
        else:
            return render_template('User/Add Complaint.html')
    else:
        return redirect('/')

@app.route('/view_complaint_reply')
def view_complaint_reply():
    if session['lg'] == "lin":
        db = Db()
        q=db.select("select * from complaint where userid='"+str(session['lid'])+"'")
        return render_template('User/View complaint reply.html',data=q)
    else:
        return redirect('/')


@app.route('/add_feedback',methods=['get','post'])
def add_feedback():
    if session['lg'] == "lin":
        if request.method == "POST":
            feedback=request.form['textarea']
            db=Db()
            db.insert("insert into feedback VALUES ('','"+str(session['lid'])+"','"+feedback+"',curdate())")
            return '''<script>alert('Added Successfully');window.location="/userhome"</script>'''
        else:
            return render_template('User/Add feedback.html')
    else:
        return redirect('/')

@app.route('/mybooking')
def mybooking():
    if session['lg'] == "lin":
        db = Db();
        res = db.select("select * from booking,cart,product where booking.bid=cart.bid and cart.pid=product.pid and userid='"+str(session['lid'])+"' and status='booked'")
        return render_template('User/My Bookings.html',data=res)
    else:
        return redirect('/')


@app.route('/totalamount')
def totalamount():


     return render_template('User/Total Amount.html')

@app.route('/view_carddetails')
def view_carddetails():
    if session['lg'] == "lin":
        db = Db();
        res = db.select("select * from Card details")
        print(res)
        return render_template('User/View Card details.html',data = res)
    else:
        return redirect('/')

@app.route('/viewcart')
def viewcart():
    if session['lg'] == "lin":
        db = Db()
        res = db.select("select * from booking,cart,product where booking.bid=cart.bid and cart.pid=product.pid and userid='"+str(session['lid'])+"' and status='add_to_cart'")
        print(res)
        return render_template('User/View Cart.html',data = res)
    else:
        return redirect('/')


@app.route('/booknow',methods=['post'])
def booknow():
    if session['lg'] == "lin":
        db = Db()
        q=db.select("select * from booking,cart, product where booking.bid=cart.bid and cart.pid=product.pid and userid='"+str(session['lid'])+"' and status='add_to_cart'")
        tot=0
        for i in q:
            qty=i['quantity']
            price=i['price']
            tot=tot+float(qty)*float(price)
            q1=db.update("update product set stock=stock-'"+str(i['quantity'])+"' where pid='"+str(i['pid'])+"'")
            db.update("update booking set status='booked', amount='"+str(tot)+"' WHERE booking.bid='"+str(i['bid'])+"'")
            # db.update("update booking set status='booked' WHERE booking.bid='"+str(i['bid'])+"' and status='add_to_cart'")


        return "<script>alert('Booked Sucessfully!!');window.location='/payment_mode'</script>"


    else:
        return redirect('/')



@app.route('/aa')
def a():
    return render_template('loginindex.html')


@app.route('/bb')
def b():
    return render_template('Admin/adminindex.html')

@app.route('/dd')
def d():
    return render_template('User/userindex.html')

@app.route('/cc')
def c():
    return render_template('Dealer/dealerindex.html')

@app.route('/logout',methods=['get','post'])
def logout():
       session.clear()
       session['lg']=""
       return redirect('/')





# import sklearn
from sklearn.ensemble import IsolationForest
######################################
def outlier(res):
    print("outlier")
    ano = []
    print(res)

    model = IsolationForest(n_estimators=50, max_samples='auto'
                                            , contamination=float(0.1), max_features=1.0)
    model.fit(res)
    ano.append(model.predict(res))
    print(ano)
    anomaly = []
    idvalue = 0
    for ij in ano:
        print(ij)
    res=[]
    for index, value in enumerate(ij, start=1):
        # print(list((index, value)))  # print(k)
        res.append(value)
    print(res)
    return res



if __name__ == '__main__':
    app.run()
