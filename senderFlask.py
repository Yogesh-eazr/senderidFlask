from flask import Flask, jsonify
import re
app = Flask(__name__)


@app.route("/displayy")
def displayy():
    with open('data_newest.json','r') as f:
        data = f.read()
        return jsonify({'DATA':data})
count = 0
@app.route("/selectsender <string:element_purpose>", methods= ['GET'])
def selectSender(element_purpose):
    with open('data_newest.json','r') as f:
        data = f.read()
        mm = data.replace('\\',"")
        stt = element_purpose.upper()
        po = {}
        qw = []
        pa = '((?:"[^"]*"|[^:,])*):((?:"[^"]*"|[^:,])*)'
        b = re.findall(pa, mm)
        for i in range(len(b)):
            k,v = b[i]
            if (f"{stt}" in v):
                qw.append(k)
            else:
                continue
        print(f"{stt} ::",len(qw))
        return jsonify(qw)


        # bb = data.split(','),
        # nm = (),,
        #
        # count =0 +
        # promo_education = []
        # for i in range(len(bb)):
        #     mn = bb[i]
        #     lo = mn.split(':')
        #     try:
        #         for k, v in zip(lo[0], lo[1]):
        #             po[k] = v
        #     except:
        #         count +=1
        #         continue
        #         # print(lo, type(lo), len(lo))
        # a = po.keys()
        # b = po.values()
        # print(count)
        # print("AAAA",type(a),len(a))
        # print("BBBB",type(b),len(a))


if __name__=='__main__':
    app.run('localhost', 8080)

### LIST OF KEYWORDS To be searched from url

# PROMOTIONAL , BANKING+,,  FINANCIAL PRODUCTS,,, PROMOTIONAL , REAL ESTATE,,, PROMOTIONAL , EDUCATION,,
# HEALTH, PROMOTIONAL,,, PROMOTIONAL , HEALTH,,, PROMOTIONAL , CONSUMER GOODS AND AUTOMOBILES,
# PROMOTIONAL , COMMUNICATION, PROMOTIONAL , COMMUNICATION, TRANSACTIONAL , COMMUNICATION, TRANSACTION,SERVICE,
# TRANSACTIONAL , EDUCATION, TOURISM AND LEISURE,, TRANSACTIONAL , HEALTH
