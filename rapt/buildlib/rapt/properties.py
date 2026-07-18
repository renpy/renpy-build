#!/usr/bin/env python


from . import plat

__ = plat.__


local_properties = plat.path("project/local.properties")
bundle_properties = plat.path("project/bundle.properties")


def set_property(properties, key, value, replace=False):
    """
    Sets the property `key` in local/bundle.properties to `value`. If replace is True,
    replaces the value.
    """

    lines = []

    try:
        with open(properties) as f:
            for l in f:
                k = l.partition("=")[0].strip()

                if k == key:
                    if not replace:
                        return
                    else:
                        continue

                lines.append(l)

    except:
        pass

    with open(properties, "w") as f:
        for l in lines:
            f.write(l)

        f.write(f"{key}={value}\n")


def get_property(properties, key, default=""):  # type: (str, str, str) -> str

    with open(properties) as f:
        for l in f:
            k, _, v = l.partition("=")

            if k.strip() == key:
                return v.strip()

    return default
