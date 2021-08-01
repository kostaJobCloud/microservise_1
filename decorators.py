from flask import jsonify


def error_handler(fun):
    def wrapper(*args, **kwargs):
        try:
            try_result = fun(*args, **kwargs)
            return try_result
        except KeyError as e:
            error_warning = {'error_warning': 'A key error has occurred. ' 
                                              'Please check if the keys of the uploaded json are correct.'}
            return jsonify(error_warning)
        except TypeError as e:
            error_warning = {'error_warning': 'A type error has occurred. '
                                              'Please check if the uploaded json data type is correct.'}
            return jsonify(error_warning)
        except Exception as e:
            error_warning = {'error_warning': repr(e)}
            return jsonify(error_warning)

    wrapper.__name__ = fun.__name__
    return wrapper