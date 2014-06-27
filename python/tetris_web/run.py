from app import app

if __name__ == '__main__':
    app.debug = False
    
    # To run on a public interface address
    #app.run(host='0.0.0.0')
    
    # to run on localhost only
    app.run()