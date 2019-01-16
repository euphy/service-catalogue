from bottle import route, run
import yaml


def get_data():
    data_stream = open('data.yml')
    data = yaml.load_safe(data_stream)
    data_stream.close()
    return data

@route('/services')
def services():
    response = {'data': get_data().get('Services', [])}
    return response

@route('/service/<service_name>')
def service_by_name(service_name):
    data = get_data().get('Services', {})
    service = data.get(service_name, {})

    response = {'data': service}
    return response




run(host='localhost', port=8080, debug=True)
