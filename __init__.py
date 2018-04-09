from werkzeug.utils import secure_filename
from flask import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '加密Session所需的密钥'

# --------ajax请求路由------------
# get请求
@app.route('/test_get',methods=['post','get'])
def test_get():
	# 获取get数据
	name = request.args.get('name')
	age = int(request.args.get('age'))
	# 返回
	if name == 'hyy' and age == 18:
		return jsonify({'result':'ok'})
	else:
		return jsonify({'result':'error'})

# post 请求
@app.route('/test_post',methods=['post','get'])
def test_post():
	# 获取post数据
	name = request.form.get('name')
	age = int(request.form.get('age'))
	# 返回
	if name == 'dyp' and age == 18:
		return jsonify({'result':'ok'})
	else:
		return jsonify({'result':'error'})

# json提交
@app.route('/test_json',methods=['post','get'])
def test_json():
	# 获取JSON数据
	data = request.get_json()
	name = data.get('name')
	age = int(data.get('age'))
	# 返回
	if name == 'keke' and age == 18:
		return jsonify({'result':'ok'})
	else:
		return jsonify({'result':'error'})
# --------------------

@app.route("/ajaxpage")
def ajaxpage():
	return render_template('ajax.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet/<name>')
def greet(name='admin'):
	return render_template('greet.html',name=name)


@app.route('/greet')
def greet2():
	name = len(request.args) and request.args['name'] or 'admin'
	return render_template('greet.html',name=name)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html')

@app.route('/redirect_to_index')
def redirect_to_index():
	return redirect(url_for('index'))

@app.route('/form',methods=['get'])
def get_form():
	return render_template('form.html')

@app.route('/form', methods=['post'])
def submit_form():
    form = request.form
    file = request.files['file']
    if file:
        app.logger.debug(f'filename:{file.filename}')
        app.logger.debug(f'secure_filename:{secure_filename(file.filename)}')
        file.save(f'uploaded_files/{file.filename}')

    return render_template('form-result.html', data=form)

@app.route("/get_request_data")
def get_request_data():
	data = request.values
	return render_template('form-result.html',data=data)


@app.route('/add_cookie')
def add_cookie():
	return render_template('add-cookie.html')

@app.route('/show_cookies',methods=['post','get'])
def show_cookies():
	name = request.values.get('cookie_name')
	value = request.values.get('cookie_value')
	if name is None:
		name = ''
	if value is None:
		value = ''

	cookies = request.cookies
	template = render_template('show-cookies.html',cookies=cookies)
	resp = make_response(template)
	resp.set_cookie(name,value)
	return resp

@app.route('/files')
def get_uploaded_file():
	filename = request.args['filename']
	return send_file(filename)

def before_request():
	import glob
	files = glob.glob('uploaded_files/*')
	flist = []
	for f in files:
		flist.append(f)
	session['files'] = flist

if __name__ == '__main__':
    app.before_request(before_request)
    app.run(host='0.0.0.0')
