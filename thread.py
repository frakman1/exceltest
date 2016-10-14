import threading
import time
import bottle
from bottle import route, run, post, Response
from functools import wraps



#------------------------------------------------------------------------------------------------------------------------------
class callonce(object):

    def __init__(self, f):
        self.f = f
        self.called = False

    def __call__(self, *args, **kwargs):
        if not self.called:
            self.called = True
            return self.f(*args, **kwargs)
        print 'Function already called once.'


class Sample(threading.Thread):
    def __init__(self):
        print"Init"
        super(Sample, self).__init__()
        self.stop = False

    def run(self):
        print "Starting server."
        print self.stop
        while not(self.stop):
            print('running')
            run(host='127.0.0.1', port=8000, debug=True, reloader=True)
            time.sleep(1)

    def test(self):
        print('testing...')
        #time.sleep(2)
        
# ---------------------------------------------------------------------------------------------------------------------------



def callonce(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return f(*args, **kwargs)
        print 'Function already called once.'
    wrapper.called = False
    return wrapper

@callonce
def func():
    print "Running once"
    print "(1)"
    sample = Sample()
    print "(2)"
    sample.start()      # Initiates second thread which calls sample.run()
    print "(3)"
    sample.test()       # Main thread calls sample.test
    print "(4)"
    print "sleeping for 3 seconds"
    time.sleep(3)
    print "Here"
    exit(0)

    

if __name__ == '__main__':
    func()
    #run(host='127.0.0.1', port=8000, debug=True, reloader=True)
    # Specify the url
    url = 'http://ae2243f4.ngrok.io/'

    # This packages the request (it doesn't make it) 
    request = urllib2.Request(url)

    # Sends the request and catches the response
    response = urllib2.urlopen(request)

    # Extracts the response
    html = response.read()

    # Print it out
    print html 

    sample.stop=True    # Main thread sets sample.stop
    sample.join()       # Main thread waits for second thread to finish
        
'''
    wb = open_workbook ("C:\\Python27\\exceltest-master\\exceltest-master\sample1.xlsx")
    sheet = wb.sheet_by_index(1)
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []
    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Firm(*values)
        items.append(item)

    for item in items:
        print("Accessing Firm Name: {0}".format(item.name))
        print item
        print
    

    
    
    sample.stop=True    # Main thread sets sample.stop
    sample.join()       # Main thread waits for second thread to finish
    
'''
