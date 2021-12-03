object = {"a":{"b":{"c":"d"}}}
object={"x":{"y":{"z":"a"}}}
object={"x":"y"}
object={"x":{"y":{"d":{"c":{"q":"r"}}}}}

def vals(x):
    if isinstance(x, dict):
        result = []
        for v in x.values():
            result.extend(vals(v))
        return result
    else:
        return [x]
print(vals(object))
