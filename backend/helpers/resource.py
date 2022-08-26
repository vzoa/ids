def wrap_result_set(result):
    serialized_result = []

    for entry in result:
        serialized_result.append(entry.to_dict())

    return {
        'result': serialized_result,
        'size': len(serialized_result),
    }


def wrap_result_single(result):
    return {
        'result': result.to_dict()
    }


def wrap_standard_error(message: str):
    return {
        'message': message
    }
