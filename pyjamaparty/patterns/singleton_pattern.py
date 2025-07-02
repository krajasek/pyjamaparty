

from threading import Lock


def singleton(klass):
    """
    A thread-safe singleton decorator.

    Usage:
    @singleton
    class MyClass(object):
        pass
    """
    instances = {}
    lock = Lock()

    def get_instance(*args, **kwargs):
        if klass not in instances:
            with lock:
                # Another thread could have created the instance
                # before we acquired the lock.
                if klass not in instances:
                    instances[klass] = klass(*args, **kwargs)
        return instances[klass]

    return get_instance
