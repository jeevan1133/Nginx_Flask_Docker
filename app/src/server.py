from flask import Flask, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    content = "It's easier to ask forgiveness than it is to get permission."
    fwd_for = "X-Forwarded-For: {}".format(
        request.headers.get('x-forwarded-for', None)
    )
    real_ip = "X-Real-IP: {}".format(
        request.headers.get('x-real-ip', None)
    )
    fwd_proto = "X-Forwarded-Proto: {}".format(
        request.headers.get('x-forwarded-proto', None)
    )

    output = "\n".join([content, fwd_for, real_ip, fwd_proto])
    response = make_response(output, 200)
    response.headers["Content-Type"] = "text/plain"

    return response

if __name__=='__main__':
    import logging

    # Set the logger level
    app.logger.setLevel(logging.INFO)

    # And now to work
    app.logger.info("PythonFlaskApp starting....")

    # Run the flask app
    # Flask app default port is 5000
    app.run(debug=True,host='0.0.0.0')

    app.logger.info("PythonFlaskApp Finished.")
