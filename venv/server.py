
from flask import Flask, render_template, request
from twilio.rest import Client
import requests
import requests_cache
account_sid='ACff37049fd0542d15997d04d37a75bc91'
auth_token ='e33b1e4337c4e01fc82e90d2a443a930'
client =Client(account_sid,auth_token)
app= Flask(__name__, static_url_path='/static')      #its a flask object

@app.route('/')
def registration_form():
    name = 'Rosalia'
    return render_template("sample.html")
    #return render_template("index.html", "spandana")

@app.route('/display', methods=['POST','GET'])
def login_register():
    print("method 2")
    fname= request.form['fname']
    print("fname captured")
    lname= request.form['lname']
    fullname= fname+" "+lname
    phno= request.form['pno']
    emno= request.form['ephno']
    why= request.form.get('ypass')
    grporin= request.form.get('ig') #.value
    email= request.form['email']
    vtype= request.form.get('vehtype')#.value
    vno= request.form.get('vehno')#.value
    srcstate= request.form.get('locality')#.value
    srcdist= request.form.get('sdlocality')#.value
    dstate= request.form.get('dslocality')#.value
    ddist= request.form.get('ddlocality')#.value
    passfrom= request.form['fromdate']
    passto= request.form['todate']
    url= request.form['link']
    r=requests.get('https://api.covid19india.org/v4/data.json')
    json_data= r.json()
    #print(json_data[dstate])
    print(ddist)
    print("after whole data")
    print(json_data[dstate]['districts'])
    print("line ")
    print(json_data[dstate]['districts'][ddist])
    print("new line 2")
    print(json_data[dstate]['districts'][ddist]['total'])
    print("new line")
    print(json_data[dstate]['districts'][ddist]['total']['confirmed'])
    cnt= json_data[dstate]['districts'][ddist]['total']['confirmed']
    pop= json_data[dstate]['districts'][ddist]['meta']['population']
    #link='localhost://127.0.0.1:4500/display'
    tpass=(cnt/pop)*100
    if tpass <40 and request.method=='POST':
        status="CONFIRMED"
        '''client.messages.create(to="whatsapp:9440XXXXX",
                               from_="whatsapp:+1 (415) 523-8XXX",
                            body="Hey "+fullname+" , EPass for your travel from"+ srcstate +" to "+dstate+ " has been "+status +" . pack your bags for "+ passfrom )'''

        message = client.messages.create(
            from_='whatsapp:+1415523XXX',
            body="Hey "+fullname+" , EPass for your travel from "+ srcstate +" to "+dstate+ " has been "+status +" . pack your bags for "+ passfrom ,
            to='whatsapp:+919440XXXXX',
            #media_url= 'http://127.0.0.1:4500/display'
            media_url='https://th.bing.com/th/id/OIP.f4L6n5x8RGuklx8Wl0RPCQHaGm?pid=ImgDet&rs=1'
        )
        return render_template('display.html', fullname=fullname, fname=fname, lname=lname, phno=phno, emno=emno, link=url, email=email , vtype=vtype, vno=vno , goi= grporin  , ss= srcstate, sd= srcdist, ds= dstate, dd=ddist, vf=passfrom, vt=passto, ig=grporin)


    else:
        status='DECLINED'
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="Hey "+fullname+" , EPass for your travel from"+ srcstate +" to "+dstate+ " has been "+status +" . please apply later. " ,
            to='whatsapp:+919440455577'
        )
        '''client.message.create(to="whatsapp:9440455577",
                               from_="whatsapp:+1 (415) 523-8886",
                            body="Hey "+fullname+" , EPass for your travel from "+ srcstate +" to "+dstate+ " has been "+status +" . please apply later. " )'''
        return render_template('display.html', fullname= fullname , fname= fname, lname=lname, phno=phno, emno=emno, email=email, link=url, vtype=vtype, vno=vno , goi= grporin  , ss= srcstate, sd= srcdist, ds= dstate, dd=ddist,vf=passfrom, vt=passto , ig=grporin)




if __name__== "__main__":
    app.run(port=4500, debug=True)
